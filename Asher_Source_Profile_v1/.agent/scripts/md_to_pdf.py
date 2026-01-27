#!/usr/bin/env python3
"""
Markdown to PDF with Automated Layout Control & Professional Symbols
====================================================================

设计原则:
1. 自动化版面控制: 图片最大高度 40% 页面高度，最大宽度 100% 正文宽度
2. 字体规范: 中文-楷体，英文-Times New Roman，代码-Menlo
3. 符号规范: 
   - 将常用 Emoji (✅, ⚠️, ❌) 替换为矢量 LaTeX 符号，确保文档专业性
   - 避免位图 Emoji 导致的模糊或缺失问题

Usage:
    python3 md_to_pdf.py <markdown_file> [output_pdf]
"""

import os
import re
import subprocess
from pathlib import Path

# LaTeX Header
LATEX_HEADER = r'''
% ===== 字体设置 =====
\usepackage{fontspec}
\usepackage{xeCJK}

% 英文: Times New Roman
\setmainfont{Times New Roman}
\setmonofont{Menlo}[Scale=0.85]

% 中文: 楷体 (Kaiti SC)
\setCJKmainfont{Kaiti SC}
\setCJKsansfont{PingFang SC}
\setCJKmonofont{Menlo}

% ===== 符号包 =====
\usepackage{amssymb} 
\usepackage{pifont}  % 提供更多符号

% ===== 页面布局 =====
\usepackage[top=2.5cm, bottom=3cm, left=2.8cm, right=2.8cm]{geometry}

% ===== 行距与段落 =====
\linespread{1.5}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.8em}

% ===== 图片尺寸自动控制 =====
\usepackage{graphicx}
\graphicspath{{./}}

\makeatletter
\def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
\def\maxheight{\ifdim\Gin@nat@height>0.4\textheight 0.4\textheight\else\Gin@nat@height\fi}
\makeatother

\setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}

% ===== 表格 =====
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\renewcommand{\arraystretch}{1.4}

% ===== 代码 =====
\usepackage{xcolor}
\usepackage{listings}
\definecolor{codebg}{RGB}{250, 250, 250}
\definecolor{codeborder}{RGB}{230, 230, 230}
\definecolor{symgreen}{RGB}{30, 160, 30}
\definecolor{symred}{RGB}{200, 30, 30}
\definecolor{symorange}{RGB}{220, 120, 0}
\definecolor{symblue}{RGB}{0, 100, 200}

\lstset{
    basicstyle=\small\ttfamily,
    backgroundcolor=\color{codebg},
    frame=single,
    rulecolor=\color{codeborder},
    breaklines=true,
    breakatwhitespace=true,
    xleftmargin=0.5em,
    xrightmargin=0.5em,
    aboveskip=1em,
    belowskip=1em,
    tabsize=4
}

% ===== 链接 =====
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=blue
}

\pagestyle{plain}
'''

def extract_mermaid_blocks(md_content):
    """Extract mermaid blocks"""
    pattern = r'```mermaid\n(.*?)\n```'
    return re.findall(pattern, md_content, re.DOTALL)

def render_mermaid_to_png(mermaid_code, output_path, index):
    """Render mermaid to PNG"""
    mmd_file = output_path / f"_mermaid_{index}.mmd"
    png_file = output_path / f"_mermaid_{index}.png"
    
    with open(mmd_file, 'w', encoding='utf-8') as f:
        f.write(mermaid_code)
    
    try:
        subprocess.run([
            'mmdc', '-i', str(mmd_file), '-o', str(png_file),
            '-b', 'white', '-w', '1200', '-H', '800', '-s', '2'
        ], check=True, capture_output=True)
        os.remove(mmd_file)
        return png_file
    except subprocess.CalledProcessError:
        if mmd_file.exists(): os.remove(mmd_file)
        return None

def replace_mermaid_with_images(md_content, image_paths):
    """Replace blocks with image syntax"""
    pattern = r'```mermaid\n.*?\n```'
    idx = [0]
    def replacer(match):
        if idx[0] < len(image_paths) and image_paths[idx[0]]:
            rel_path = os.path.basename(image_paths[idx[0]])
            idx[0] += 1
            return f'![diagram]({rel_path})'
        idx[0] += 1
        return match.group(0)
    return re.sub(pattern, replacer, md_content, flags=re.DOTALL)

def replace_emojis_with_latex(text):
    """
    Replace common emojis with professional LaTeX vector symbols
    """
    # Map common emojis to LaTeX
    replacements = {
        # Stars and Ratings - Use simple ASCII (LaTeX symbols don't work in tables)
        '★★★★★': '[5/5]',
        '★★★★': '[4/5]',
        '★★★': '[3/5]',
        '★★': '[2/5]',
        '★': '[1/5]',
        '☆': '[0/5]',
        '○': '[-]',
        
        # Checkmarks & Status (Use raw inline latex)
        '✅': r'`{\color{symgreen}\Large$\checkmark$}`{=latex}',
        '✓': r'`{\color{symgreen}$\checkmark$}`{=latex}',
        '❌': r'`{\color{symred}\Large$\times$}`{=latex}',
        '⚠️': r'`{\color{symorange}\Large\textbf{!}}`{=latex}',
        '⏳': r'`{\color{symblue}\small(Wait)}`{=latex}',
        
        # Information
        '💡': r'`{\color{symorange}\textbf{[Idea]}}`{=latex}',
        '🔍': r'`{\color{symblue}\textbf{[Q]}}`{=latex}',
        '📌': r'`{\color{symred}\textbf{*}}`{=latex}',
        '🚀': r'`{\textbf{[Go]}}`{=latex}',
        'ℹ️': r'`{\color{symblue}\textbf{i}}`{=latex}',
        
        # Misc
        '📊': r'`\textbf{[Chart]}`{=latex}',
        '🗑️': r'',
        '📄': r'',
        '🔧': r'',
    }
    
    for emoji, latex in replacements.items():
        text = text.replace(emoji, latex)
        
    # Regex removal for other miscellaneous emojis to prevent errors
    # IMPORTANT: Preserve common text symbols that are NOT problematic:
    # - ★ (U+2605) Black Star - used for ratings
    # - ☆ (U+2606) White Star
    # - ○ (U+25CB) White Circle
    # - × (U+00D7) Multiplication Sign
    # - → (U+2192) Arrows
    
    # Only remove actual emoji ranges, not general symbols
    other_emojis = re.compile(
        "["
        "\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "]+", 
        flags=re.UNICODE
    )
    text = other_emojis.sub('', text)
    
    return text

def fix_chinese_inline_code(text):
    """
    Fix inline code (backticks) containing Chinese characters.
    
    Problem: Monospace fonts (e.g., Menlo) don't support Chinese characters,
    causing them to render as empty boxes in PDFs.
    
    Solution: Convert inline code containing Chinese to bold formatting.
    Example: `内容价值 = X × Y` → **内容价值 = X × Y**
    """
    import re
    
    # Pattern to match inline code (single backticks, not code blocks)
    # Matches: `content here` but not ```code block```
    inline_code_pattern = r'(?<!`)`([^`\n]+?)`(?!`)'
    
    def has_chinese(s):
        """Check if string contains Chinese characters"""
        return bool(re.search(r'[\u4e00-\u9fff]', s))
    
    def replacer(match):
        content = match.group(1)
        if has_chinese(content):
            # Convert to bold
            return f'**{content}**'
        else:
            # Keep as inline code
            return match.group(0)
    
    return re.sub(inline_code_pattern, replacer, text)

def preprocess_markdown(md_content):
    """Preprocess content"""
    # Fix Chinese in inline code FIRST (before emoji processing)
    md_content = fix_chinese_inline_code(md_content)
    # Handle Emojis -> LaTeX
    md_content = replace_emojis_with_latex(md_content)
    return md_content

def convert_md_to_pdf(md_file_path, output_pdf_path):
    """Main process"""
    md_file = Path(md_file_path).resolve()
    output_pdf = Path(output_pdf_path).resolve()
    output_dir = md_file.parent
    
    print(f"📄 Processing: {md_file.name}")
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 1. Render Mermaid
    mermaid_blocks = extract_mermaid_blocks(md_content)
    print(f"🔧 Found {len(mermaid_blocks)} diagrams")
    
    image_paths = []
    for i, code in enumerate(mermaid_blocks):
        img = render_mermaid_to_png(code, output_dir, i)
        image_paths.append(img)
        if img: print(f"  ✓ Rendered diagram {i+1}")
    
    # 2. Replaces
    md_content = replace_mermaid_with_images(md_content, image_paths)
    md_content = preprocess_markdown(md_content)
    
    # 3. Write temp
    temp_md = output_dir / "_temp_export.md"
    header_file = output_dir / "_header.tex"
    
    with open(temp_md, 'w', encoding='utf-8') as f:
        f.write(md_content)
    with open(header_file, 'w', encoding='utf-8') as f:
        f.write(LATEX_HEADER)
    
    # 4. Generate PDF
    print("📐 Converting to PDF (Professional Symbols)...")
    try:
        subprocess.run([
            'pandoc', str(temp_md),
            '-o', str(output_pdf),
            '--pdf-engine=xelatex',
            '-H', str(header_file),
            '--standalone',
            '--highlight-style=tango'
        ], check=True, capture_output=True, cwd=str(output_dir))
        
        if output_pdf.exists():
            size_kb = output_pdf.stat().st_size / 1024
            print(f"✅ Success: {output_pdf.name} ({size_kb:.0f} KB)")
        else:
            raise Exception("PDF not created")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.stderr.decode()}")
        raise
        
    finally:
        for f in [temp_md, header_file]:
            if f.exists(): os.remove(f)
    
    return [p for p in image_paths if p and Path(p).exists()]

def cleanup_images(image_paths):
    for img in image_paths:
        if img and Path(img).exists():
            os.remove(img)
    if image_paths: print("🗑️ Cleaned temp images")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("MD -> PDF (Layout + Pro Symbols)")
        sys.exit(1)
    md = sys.argv[1]
    pdf = sys.argv[2] if len(sys.argv) >= 3 else Path(md).with_suffix('.pdf')
    imgs = convert_md_to_pdf(md, pdf)
    if imgs: cleanup_images(imgs)
