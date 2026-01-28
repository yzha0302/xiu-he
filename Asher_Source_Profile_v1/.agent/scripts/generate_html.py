import os
import argparse
import base64

def generate_html(source_file, output_dir=None):
    if not os.path.exists(source_file):
        print(f"Error: Source file not found at {source_file}")
        return

    # Determine Output Path
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(source_file)), "Web_Export")
    
    os.makedirs(output_dir, exist_ok=True)
    file_name = os.path.splitext(os.path.basename(source_file))[0]
    output_file = os.path.join(output_dir, f"{file_name}.html")

    # Read Markdown
    with open(source_file, 'r', encoding='utf-8') as f:
        raw_markdown = f.read()

    # Encode Markdown (Base64 Safe Injection)
    encoded_markdown = base64.b64encode(raw_markdown.encode('utf-8')).decode('utf-8')

    # Template
    html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{file_name}</title>
    
    <!-- Libraries (Using Staticfile CDN for China reliability) -->
    <script src="https://cdn.staticfile.net/marked/12.0.0/marked.min.js"></script>
    <script src="https://cdn.staticfile.net/mermaid/10.9.0/mermaid.min.js"></script>
    <link rel="stylesheet" href="https://cdn.staticfile.net/highlight.js/11.9.0/styles/atom-one-dark.min.css">
    <script src="https://cdn.staticfile.net/highlight.js/11.9.0/highlight.min.js"></script>

    <style>
        :root {{
            --bg-color: #0f0f0f;
            --text-color: #e0e0e0;
            --accent-primary: #00f3ff; /* Cyan */
            --accent-secondary: #bc13fe; /* Purple */
            --sidebar-width: 280px;
            --content-width: 800px;
        }}

        * {{ box-sizing: border-box; }}

        body {{
            margin: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
            /* System Font Stack for performance and reliability */
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, "Noto Sans SC", sans-serif;
            display: flex;
            min-height: 100vh;
        }}

        /* Sidebar */
        .sidebar {{
            width: var(--sidebar-width);
            height: 100vh;
            position: fixed;
            left: 0;
            top: 0;
            overflow-y: auto;
            background: rgba(15, 15, 15, 0.95);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2rem;
            backdrop-filter: blur(10px);
            z-index: 100;
        }}

        .logo {{
            font-weight: 700;
            font-size: 1.2rem;
            letter-spacing: 2px;
            background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
            text-transform: uppercase;
        }}

        .toc ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .toc li {{
            margin-bottom: 0.8rem;
        }}

        .toc a {{
            color: #888;
            text-decoration: none;
            font-size: 0.9rem;
            transition: all 0.3s;
            display: block;
        }}

        .toc a:hover, .toc a.active {{
            color: var(--accent-primary);
            padding-left: 5px;
            border-left: 2px solid var(--accent-primary);
        }}

        .toc .sub-item {{
            padding-left: 1rem;
            font-size: 0.85rem;
        }}

        /* Main Content */
        .main-container {{
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 4rem 2rem;
            display: flex;
            justify-content: center;
        }}

        .markdown-body {{
            width: 100%;
            max-width: var(--content-width);
            line-height: 1.8;
            font-size: 1.05rem;
        }}

        /* Typography */
        h1, h2, h3, h4, h5, h6 {{
            color: #fff;
            margin-top: 2.5rem;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }}

        h1 {{ 
            font-size: 2.5rem; 
            background: linear-gradient(90deg, #fff, #888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding-bottom: 1rem;
        }}
        
        h2 {{ 
            font-size: 1.8rem; 
            color: var(--accent-primary);
        }}

        p {{ color: #ccc; }}

        strong {{ color: #fff; font-weight: 600; }}

        /* Code Blocks */
        pre {{
            background: #1a1a1a;
            border-radius: 8px;
            padding: 1.5rem;
            border: 1px solid rgba(255,255,255,0.05);
            overflow-x: auto;
        }}

        code {{
            font-family: "JetBrains Mono", Consolas, Monaco, "Andale Mono", monospace;
            font-size: 0.9rem;
        }}

        p code {{
            background: rgba(255, 255, 255, 0.1);
            padding: 2px 6px;
            border-radius: 4px;
            color: var(--accent-secondary);
        }}

        /* Blockquotes / Callouts */
        blockquote {{
            border-left: 4px solid var(--accent-secondary);
            margin: 1.5rem 0;
            padding: 1rem 1.5rem;
            background: rgba(188, 19, 254, 0.05); /* Tinted purple */
            border-radius: 0 8px 8px 0;
        }}
        
        /* Custom Alert Styles for Note/Tip/Important */
        .alert {{
            padding: 1rem 1.5rem;
            margin: 1.5rem 0;
            border-radius: 8px;
            border-left: 4px solid;
            background: rgba(255,255,255,0.03);
        }}
        
        .alert-note {{ border-color: #00f3ff; background: rgba(0, 243, 255, 0.05); }}
        .alert-tip {{ border-color: #00ff9d; background: rgba(0, 255, 157, 0.05); }}
        .alert-important {{ border-color: #bc13fe; background: rgba(188, 19, 254, 0.05); }}
        .alert-warning {{ border-color: #ffbd2e; background: rgba(255, 189, 46, 0.05); }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            background: rgba(255,255,255,0.02);
            border-radius: 8px;
            overflow: hidden;
        }}

        th, td {{
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}

        th {{
            background: rgba(255,255,255,0.05);
            color: var(--accent-primary);
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 1px;
        }}

        /* Mermaid */
        .mermaid {{
            margin: 2rem 0;
            text-align: center;
        }}

        /* Error Banner */
        #error-banner {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: #ff4444;
            color: white;
            padding: 10px;
            text-align: center;
            z-index: 9999;
            display: none;
        }}

        /* Scrollbar */
        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: #0f0f0f; }}
        ::-webkit-scrollbar-thumb {{ background: #333; border-radius: 4px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #555; }}

        @media (max-width: 1024px) {{
            .sidebar {{ display: none; }} /* Mobile: hide sidebar for now */
            .main-container {{ margin-left: 0; padding: 2rem; }}
        }}
    </style>
</head>
<body>

    <div id="error-banner"></div>

    <nav class="sidebar">
        <div class="logo">DOC<br>READER</div>
        <div class="toc" id="toc"></div>
    </nav>

    <main class="main-container">
        <div id="content" class="markdown-body"></div>
    </main>

    <script>
        try {{
            // 1. Get raw markdown from Base64
            const rawBase64 = "{encoded_markdown}";
            const markdown = new TextDecoder().decode(Uint8Array.from(atob(rawBase64), c => c.charCodeAt(0)));

            // 2. Configure Marked
            if (typeof marked === 'undefined') throw new Error("Marked.js failed to load. Please check your internet connection.");
            
            marked.use({{
                breaks: true,
                gfm: true,
                highlight: function(code, lang) {{
                    if (typeof hljs === 'undefined') return code;
                    const language = hljs.getLanguage(lang) ? lang : 'plaintext';
                    return hljs.highlight(code, {{ language }}).value;
                }}
            }});
            
            // Custom Renderer
            const renderer = new marked.Renderer();
            
            // Handle Blockquotes for Alerts
            renderer.blockquote = function(quote) {{
                const div = document.createElement('div');
                div.innerHTML = quote;
                const text = div.textContent.trim();
                
                if (text.startsWith('[!NOTE]')) {{
                    return `<div class="alert alert-note">${{quote.replace('[!NOTE]', '<strong>NOTE</strong>')}}</div>`;
                }} else if (text.startsWith('[!TIP]')) {{
                    return `<div class="alert alert-tip">${{quote.replace('[!TIP]', '<strong>TIP</strong>')}}</div>`;
                }} else if (text.startsWith('[!IMPORTANT]')) {{
                    return `<div class="alert alert-important">${{quote.replace('[!IMPORTANT]', '<strong>IMPORTANT</strong>')}}</div>`;
                }} else if (text.startsWith('[!WARNING]')) {{
                    return `<div class="alert alert-warning">${{quote.replace('[!WARNING]', '<strong>WARNING</strong>')}}</div>`;
                }}
                
                return `<blockquote>${{quote}}</blockquote>`;
            }};

            // Handle Code Blocks (Mermaid interception)
            renderer.code = function(code, language) {{
                if (language === 'mermaid') {{
                    return `<div class="mermaid">${{code}}</div>`;
                }}
                if (typeof hljs !== 'undefined') {{
                    const validLanguage = hljs.getLanguage(language) ? language : 'plaintext';
                    return `<pre><code class="hljs language-${{validLanguage}}">${{hljs.highlight(code, {{ language: validLanguage }}).value}}</code></pre>`;
                }}
                return `<pre><code>${{code}}</code></pre>`;
            }};

            // Render Markdown
            const contentDiv = document.getElementById('content');
            contentDiv.innerHTML = marked.parse(markdown, {{ renderer: renderer }});

            // 3. Initialize Mermaid
            if (typeof mermaid !== 'undefined') {{
                mermaid.initialize({{
                    startOnLoad: false,
                    theme: 'base',
                    securityLevel: 'loose',
                    themeVariables: {{
                        darkMode: true,
                        background: '#1a1a1a',
                        primaryColor: '#1a1a1a',
                        mainBkg: '#1a1a1a',
                        primaryBorderColor: '#00f3ff', // Cyan
                        primaryTextColor: '#e0e0e0',
                        lineColor: '#bc13fe', // Purple
                        secondaryColor: '#0f0f0f',
                        tertiaryColor: '#1a1a1a',
                        noteBkgColor: '#2a2a2a',
                        noteTextColor: '#fff',
                        nodeBorder: '#00f3ff',
                        clusterBkg: '#0f0f0f',
                        clusterBorder: '#bc13fe',
                        titleColor: '#fff',
                        edgeLabelBackground: '#1a1a1a'
                    }}
                }});

                // Run Mermaid
                mermaid.run({{
                    nodes: document.querySelectorAll('.mermaid')
                }});
            }}

            // 4. Generate TOC
            const tocContainer = document.getElementById('toc');
            const headers = contentDiv.querySelectorAll('h1, h2, h3');
            const tocList = document.createElement('ul');

            headers.forEach((header, index) => {{
                const id = 'header-' + index;
                header.id = id;

                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = '#' + id;
                a.textContent = header.textContent;
                
                if (header.tagName === 'H3') {{
                    li.classList.add('sub-item');
                }}
                
                li.appendChild(a);
                tocList.appendChild(li);
            }});
            tocContainer.appendChild(tocList);

            // Sidebar Active State
            const observer = new IntersectionObserver(entries => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        document.querySelectorAll('.toc a').forEach(link => link.classList.remove('active'));
                        const id = entry.target.id;
                        const link = document.querySelector(`.toc a[href="#${{id}}"]`);
                        if (link) link.classList.add('active');
                    }}
                }});
            }}, {{ rootMargin: '-10% 0px -80% 0px' }});

            headers.forEach(header => observer.observe(header));

        }} catch (e) {{
            const errorBanner = document.getElementById('error-banner');
            errorBanner.style.display = 'block';
            errorBanner.textContent = 'Error rendering page: ' + e.message;
            console.error(e);
        }}
    </script>
</body>
</html>
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"Success: Generated {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to Premium HTML")
    parser.add_argument("--input", required=True, help="Input markdown file path")
    parser.add_argument("--output_dir", help="Directory to save the HTML file")
    
    args = parser.parse_args()
    generate_html(args.input, args.output_dir)
