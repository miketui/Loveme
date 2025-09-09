#!/usr/bin/env python3
"""
Simple ACISS Transformer - Direct Structure Replacement
Transforms existing structure to ACISS while preserving 100% content.
"""
import re
import sys
from pathlib import Path

def transform_chapter_to_aciss(content):
    """Transform chapter using direct replacements to ensure content preservation."""
    
    # Step 1: Update the title page structure
    # Replace chapter-title-stack with title-stack + title-bar + title-lines
    content = re.sub(
        r'<div class="chapter-title-stack">\s*<div class="chapter-title-vertical"[^>]*></div>\s*<div>',
        '''<div class="title-stack">
            <div class="title-bar"></div>
            <div class="title-lines">''',
        content,
        flags=re.DOTALL
    )
    
    # Replace chapter-title-word with title-line
    content = re.sub(
        r'<h1 class="chapter-title chapter-title-word">([^<]+)</h1>',
        r'<div class="title-line">\1</div>',
        content
    )
    
    # Close the title-lines and title-stack properly
    content = re.sub(
        r'</div>\s*</div>\s*</div>',
        '''</div>
        </div>''',
        content
    )
    
    # Step 2: Add page breaks between sections
    # Add page break after chap-title section
    content = re.sub(
        r'</section>\s*<section class="chap-body"',
        '''</section>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGES 2-4: BODY CONTENT -->
<section class="chap-body"''',
        content,
        flags=re.DOTALL
    )
    
    # Add page break before endnotes
    content = re.sub(
        r'</section>\s*<aside class="endnotes"',
        '''</section>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGE 5: ENDNOTES -->
<aside class="endnotes"''',
        content,
        flags=re.DOTALL
    )
    
    # Add page break before quiz
    content = re.sub(
        r'</aside>\s*<section class="quiz-container',
        '''</aside>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGE 6: QUIZ & WORKSHEET -->
<section class="quiz-container''',
        content,
        flags=re.DOTALL
    )
    
    # Step 3: Add ACISS class compatibility
    # Update body class to chapter-page
    content = re.sub(
        r'<body class="chap-title">',
        '<body class="chapter-page">',
        content
    )
    
    # Add avoid-break classes to quiz and worksheet sections
    content = re.sub(
        r'<section class="quiz-container chap-quiz"',
        '<section class="quiz-container chap-quiz avoid-break"',
        content
    )
    
    content = re.sub(
        r'<section class="worksheet"',
        '<section class="worksheet avoid-break"',
        content
    )
    
    # Step 4: Update closing section to use ACISS closing class
    content = re.sub(
        r'<section class="image-quote"',
        '<section class="closing">',
        content
    )
    
    # Step 5: Add ACISS comments for clarity
    content = re.sub(
        r'<section class="chap-title">',
        '''<!-- PAGE 1: TITLE PAGE -->
<section class="chap-title">''',
        content
    )
    
    return content

def verify_content_preservation(original, processed):
    """Verify that all text content is preserved."""
    def extract_text(html):
        # Remove HTML tags and normalize whitespace
        text = re.sub(r'<[^>]+>', '', html)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    original_text = extract_text(original)
    processed_text = extract_text(processed)
    
    return original_text == processed_text, len(original_text), len(processed_text)

def process_chapter(input_file, output_file):
    """Process a chapter file with ACISS transformation."""
    print(f"🔄 Processing {Path(input_file).name}...")
    
    # Read original
    with open(input_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Transform
    processed_content = transform_chapter_to_aciss(original_content)
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed_content)
    
    # Verify preservation
    preserved, orig_len, proc_len = verify_content_preservation(original_content, processed_content)
    
    if preserved:
        print(f"✅ CONTENT 100% PRESERVED: {Path(output_file).name}")
        return True
    else:
        print(f"⚠️  Content preservation issue: {Path(output_file).name}")
        print(f"   Original: {orig_len} chars, Processed: {proc_len} chars")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 simple-transformer.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        success = process_chapter(input_file, output_file)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)