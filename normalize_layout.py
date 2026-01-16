
import os
import re

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
FOOTER_HTML_PATH = os.path.join(ASSETS_DIR, 'footer.html')
FOOTER_CSS_PATH = os.path.join(ASSETS_DIR, 'footer.css')

# Target files explicit list
TARGET_FILES = [
    'index.html',
    'development.html',
    'statistics.html',
    'versions.html',
    'changelog.html',
    'quality_report.html',
    'docs/index-pt.html',
    'docs/webvowl/index.html'
]

def load_asset(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def inject_footer(file_path, footer_html, footer_css_content):
    full_path = os.path.join(BASE_DIR, file_path)
    
    if not os.path.exists(full_path):
        print(f"Skipping missing file: {file_path}")
        return

    print(f"Processing: {file_path}")
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove existing Footer HTML
    # Regex to find <footer class="footer">...</footer> including multiline content
    # Using dotall flag
    footer_regex = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
    
    # Check if footer exists
    if footer_regex.search(content):
        print(f"  - Removing existing footer in {file_path}")
        content = footer_regex.sub('', content)
    else:
        print(f"  - No existing footer found to remove (or different class) in {file_path}")
        # Try finding generic footer if class is different, but user rule implies they should be this class.
        # Fallback: remove <footer ...>...</footer>
        fallback_regex = re.compile(r'<footer.*?>.*?</footer>', re.DOTALL)
        if fallback_regex.search(content):
             print(f"  - Removing generic footer found in {file_path}")
             content = fallback_regex.sub('', content)

    # 2. Inject Canonical Footer HTML before </body>
    if '</body>' in content:
        print(f"  - Injecting canonical footer HTML in {file_path}")
        content = content.replace('</body>', f'\n{footer_html}\n</body>')
    else:
        print(f"  WARNING: No </body> tag found in {file_path}. Appending footer to end.")
        content += f'\n{footer_html}'

    # 3. Ensure CSS is present
    # We will inject the CSS content directly into a <style> block in <head> 
    # OR replace existing footer styles.
    # User's previous edits injected footer css into <style> blocks.
    # To be robust, let's look for "/* Footer Styles */" and replace that block, or append to head.
    
    css_block = f"\n<style>\n{footer_css_content}\n</style>"
    
    # Remove existing Footer Styles block if identifiable
    # Assuming the structure "/* Footer Styles */ ... .footer-bottom-bar { ... }"
    # It's safer to just remove known footer classes if possible, but regexing CSS is hard.
    # We will simply look for the marker "/* Footer Styles */" and remove until closing brace of last element or </style>
    # Given the complexity, and the fact we want to enforce ONE truth,
    # We'll just define a standard ID or marker for our injected style?
    # No, let's just append the style to HEAD. CSS cascade will let last rule win if specificity is same.
    # However, to avoid duplication, let's try to remove previous injections.
   
    # Regex for our specific footer style block pattern (approximate)
    style_regex = re.compile(r'/\* Footer Styles \*/.*?(?=\</style\>)', re.DOTALL)
    
    if style_regex.search(content):
        print(f"  - Removing existing footer CSS block in {file_path}")
        # This regex might be risky if multiple styles share a block. 
        # But previous agents removed it successfully using file replacement.
        content = style_regex.sub('', content)
    
    # Also remove empty <style></style> if we caused it? No, keeping it simple.

    # Inject CSS
    if '</head>' in content:
        print(f"  - Injecting canonical footer CSS in {file_path}")
        content = content.replace('</head>', f'{css_block}\n</head>')
    else:
        print(f"  WARNING: No </head> tag. Appending CSS to start.")
        content = css_block + content

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    footer_html = load_asset(FOOTER_HTML_PATH)
    footer_css = load_asset(FOOTER_CSS_PATH)
    
    # Walk through all directories to find other HTML files if needed, 
    # but strictly following the list + any other htmls in public tree as requested.
    
    all_html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        if 'assets' in root: continue # Skip assets dir itself
        for file in files:
            if file.endswith('.html'):
                # relative path
                rel_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                all_html_files.append(rel_path)

    # Merge explicit targets with discovered ones
    targets = set(TARGET_FILES)
    for f in all_html_files:
        targets.add(f)
        
    for file_path in sorted(list(targets)):
        inject_footer(file_path, footer_html, footer_css)

if __name__ == "__main__":
    main()
