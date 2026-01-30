
import fetch from 'node-fetch';
import fs from 'fs';

const config = JSON.parse(fs.readFileSync('/Users/yixuanzhang/.dida-mcp-config.json', 'utf8'));
const token = config.access_token;
const inboxId = config.inboxId;

async function run() {
    console.log(`Checking project: ${inboxId}`);
    const res = await fetch(`https://api.dida365.com/open/v1/project/${inboxId}/task`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const data: any = await res.json();
    // console.log("DATA:", JSON.stringify(data,null,2));

    // V1 API might return array or object?
    // User previously said V1 finds tasks.

    // Try to find array
    let tasks = [];
    if (Array.isArray(data)) {
        tasks = data;
    } else if (data.tasks) {
        tasks = data.tasks;
    } else {
        console.log("Could not find tasks array. Data keys:", Object.keys(data));
        return;
    }

    const target = tasks.find((t: any) => t.title.includes('Coffee') || t.title.includes('咖啡') || t.title.includes('测试'));

    if (target) {
        console.log(`FOUND_TASK_ID: ${target.id}`);
        console.log(`FOUND_PROJECT_ID: ${target.projectId}`);
        console.log(`FOUND_TITLE: ${target.title}`);
    } else {
        console.log("Task 'Drink Coffee' not found. First 3 tasks:");
        tasks.slice(0, 3).forEach((t: any) => console.log(`- [${t.title}] ID: ${t.id}`));
    }
}
run();
