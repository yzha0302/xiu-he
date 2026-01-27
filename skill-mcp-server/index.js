#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import fs from "fs/promises";
import path from "path";

// 技能库路径配置
const SKILL_SOURCES = [
  {
    name: "Claude Specific",
    path: "/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/AI_Skills_Library/.claude/skills",
    type: "skills",
  },
  {
    name: "Local Custom",
    path: "/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/AI_Skills_Library/.agent/skills",
    type: "skills",
  },
  {
    name: "General Library",
    path: "/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/AI_Skills_Library/.agents/skills",
    type: "skills",
  },
  {
    name: "Asher Workflows",
    path: "/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/Asher_Source_Profile_v1/.agent/workflows",
    type: "workflows",
  },
];

// 创建 MCP Server
const server = new Server(
  {
    name: "skill-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 列出所有可用技能 (去重)
async function listSkills() {
  const skillMap = new Map(); // name -> skill info

  for (const source of SKILL_SOURCES) {
    try {
      const entries = await fs.readdir(source.path, { withFileTypes: true });

      if (source.type === "skills") {
        for (const entry of entries) {
          if (entry.name.startsWith(".")) continue;

          // 检查是否为目录或指向目录的软链接
          let isDir = entry.isDirectory();
          if (entry.isSymbolicLink()) {
            try {
              const stat = await fs.stat(path.join(source.path, entry.name));
              isDir = stat.isDirectory();
            } catch {
              isDir = false;
            }
          }

          if (isDir) {
            // 如果高优先级的源已经添加过同名技能，则跳过
            if (skillMap.has(entry.name)) continue;

            const skillPath = path.join(source.path, entry.name, "SKILL.md");
            try {
              await fs.access(skillPath);
              skillMap.set(entry.name, {
                name: entry.name,
                source: source.name,
                type: "skill",
              });
            } catch {
              // SKILL.md 不存在，跳过
            }
          }
        }
      } else if (source.type === "workflows") {
        for (const entry of entries) {
          if (
            entry.isFile() &&
            entry.name.endsWith(".md") &&
            entry.name !== "README.md"
          ) {
            const name = entry.name.replace(".md", "");
            if (skillMap.has(name)) continue;

            skillMap.set(name, {
              name: name,
              source: source.name,
              type: "workflow",
            });
          }
        }
      }
    } catch (err) {
      // 忽略无法读取的源 (比如目录不存在)
      // console.error(`Error reading ${source.name}: ${err.message}`);
    }
  }

  return Array.from(skillMap.values());
}

// 读取指定技能的内容
async function readSkill(skillName) {
  // 按照优先级遍历所有源
  for (const source of SKILL_SOURCES) {
    try {
      if (source.type === "skills") {
        const skillDirPath = path.join(source.path, skillName);
        const skillMdPath = path.join(skillDirPath, "SKILL.md");

        try {
          // 检查文件是否存在
          await fs.access(skillMdPath);

          const content = await fs.readFile(skillMdPath, "utf-8");

          // 读取附属文件
          const entries = await fs.readdir(skillDirPath, { withFileTypes: true });
          const additionalFiles = [];

          for (const entry of entries) {
            // 这里我们不需要特别处理软链接，readdir 配合 join 路径会自动处理读取
            // 但如果是目录，需要递归读取

            // 简单起见，我们只处理一层子目录或文件，且忽略 . 开头的
            if (entry.name.startsWith(".")) continue;
            if (entry.name === "SKILL.md") continue;

            const entryPath = path.join(skillDirPath, entry.name);
            const stat = await fs.stat(entryPath);

            if (stat.isDirectory()) {
              const subEntries = await fs.readdir(entryPath);
              for (const subEntry of subEntries) {
                if (subEntry.endsWith(".md") && !subEntry.startsWith(".")) {
                  const subContent = await fs.readFile(path.join(entryPath, subEntry), "utf-8");
                  additionalFiles.push({
                    path: `${entry.name}/${subEntry}`,
                    content: subContent
                  });
                }
              }
            } else if (stat.isFile() && entry.name.endsWith(".md")) {
              const fileContent = await fs.readFile(entryPath, "utf-8");
              additionalFiles.push({
                path: entry.name,
                content: fileContent
              });
            }
          }

          return {
            found: true,
            source: source.name,
            type: "skill",
            content,
            additionalFiles,
          };
        } catch (e) {
          // 在当前源未找到，继续下一个源
          continue;
        }
      } else if (source.type === "workflows") {
        const workflowMdPath = path.join(source.path, `${skillName}.md`);
        try {
          await fs.access(workflowMdPath);
          const content = await fs.readFile(workflowMdPath, "utf-8");
          return {
            found: true,
            source: source.name,
            type: "workflow",
            content,
            additionalFiles: [],
          };
        } catch {
          continue;
        }
      }
    } catch {
      continue;
    }
  }

  return {
    found: false,
    error: `Skill "${skillName}" not found in any source.`,
  };
}

// 注册工具列表
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "list_skills",
        description:
          "列出所有可用的 AI 技能和工作流。返回技能名称、来源和类型。",
        inputSchema: {
          type: "object",
          properties: {},
          required: [],
        },
      },
      {
        name: "use_skill",
        description:
          "加载并返回指定技能或工作流的完整内容。包括主文件和所有附属文件。",
        inputSchema: {
          type: "object",
          properties: {
            skill_name: {
              type: "string",
              description: "技能或工作流的名称（如 pdf、meeting-analysis）",
            },
          },
          required: ["skill_name"],
        },
      },
      {
        name: "read_file",
        description: "读取指定路径的文件内容（仅限技能库目录内的文件）",
        inputSchema: {
          type: "object",
          properties: {
            file_path: {
              type: "string",
              description: "文件的相对路径或绝对路径",
            },
          },
          required: ["file_path"],
        },
      },
    ],
  };
});

// 处理工具调用
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "list_skills") {
    const skills = await listSkills();
    const formatted = skills
      .map((s) => `- ${s.name} (${s.source}, ${s.type})`)
      .join("\n");
    return {
      content: [
        {
          type: "text",
          text: `## 可用技能列表\n\n${formatted}\n\n共 ${skills.length} 个技能/工作流可用。\n使用 use_skill 工具加载具体技能。`,
        },
      ],
    };
  }

  if (name === "use_skill") {
    const skillName = args?.skill_name;
    if (!skillName) {
      return {
        content: [
          {
            type: "text",
            text: "错误：请提供技能名称 (skill_name)",
          },
        ],
      };
    }

    const result = await readSkill(skillName);

    if (!result.found) {
      const skills = await listSkills();
      const suggestions = skills
        .slice(0, 10)
        .map((s) => s.name)
        .join(", ");
      return {
        content: [
          {
            type: "text",
            text: `${result.error}\n\n可用技能示例：${suggestions}`,
          },
        ],
      };
    }

    let response = `## 技能：${skillName}\n来源：${result.source}\n类型：${result.type}\n\n---\n\n${result.content}`;

    if (result.additionalFiles.length > 0) {
      response += "\n\n---\n\n## 附属文件\n\n";
      for (const file of result.additionalFiles) {
        response += `### ${file.path}\n\n${file.content}\n\n`;
      }
    }

    return {
      content: [
        {
          type: "text",
          text: response,
        },
      ],
    };
  }

  if (name === "read_file") {
    const filePath = args?.file_path;
    if (!filePath) {
      return {
        content: [
          {
            type: "text",
            text: "错误：请提供文件路径 (file_path)",
          },
        ],
      };
    }

    // 安全检查：只允许读取技能库目录内的文件
    const allowedPaths = SKILL_SOURCES.map((s) => s.path);
    const isAllowed = allowedPaths.some(
      (allowed) =>
        filePath.startsWith(allowed) ||
        filePath.startsWith("/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/")
    );

    if (!isAllowed) {
      return {
        content: [
          {
            type: "text",
            text: "错误：只能读取技能库目录内的文件",
          },
        ],
      };
    }

    try {
      const content = await fs.readFile(filePath, "utf-8");
      return {
        content: [
          {
            type: "text",
            text: content,
          },
        ],
      };
    } catch (err) {
      return {
        content: [
          {
            type: "text",
            text: `错误：无法读取文件 - ${err.message}`,
          },
        ],
      };
    }
  }

  return {
    content: [
      {
        type: "text",
        text: `未知工具：${name}`,
      },
    ],
  };
});

// 启动服务器
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Skill MCP Server running on stdio");
}

main().catch(console.error);
