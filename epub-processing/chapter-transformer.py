#!/usr/bin/env python3
"""
ACISS Chapter Transformer - Complete Content Preservation
Transforms existing XHTML to ACISS structure while preserving 100% of content.
"""
import re
import sys
from pathlib import Path

def extract_all_text_content(html_content):
    """Extract all text content for preservation verification."""
    # Remove all HTML tags but keep the text
    text_only = re.sub(r'<[^>]+>', '', html_content)
    # Clean up extra whitespace
    text_only = re.sub(r'\s+', ' ', text_only).strip()
    return text_only

def transform_to_aciss_structure(original_content, chapter_file_name):
    """Transform the original content to ACISS structure while preserving all content."""
    
    # Extract the Roman numeral from the current chapter-number-text
    roman_match = re.search(r'<div class="chapter-number-text">([IVXLC]+)</div>', original_content)
    roman_num = roman_match.group(1) if roman_match else "I"
    
    # Extract title words from chapter-title-word elements
    title_words = re.findall(r'<h1 class="[^"]*chapter-title-word[^"]*">([^<]+)</h1>', original_content)
    if not title_words:
        # Fallback - extract from title tag
        title_match = re.search(r'<title>Chapter [IVXLC]+ [–-] ([^<]+)</title>', original_content)
        if title_match:
            title_text = title_match.group(1).strip()
            title_words = title_text.split()
    
    # Generate title lines (break into 3-6 lines)
    title_lines = []
    if len(title_words) <= 6:
        title_lines = title_words
    else:
        # Combine shorter words
        lines = []
        current_line = []
        for word in title_words:
            if len(word) <= 3 and len(current_line) == 1 and len(current_line[0]) <= 4:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        title_lines = lines[:6]
    
    title_lines_html = '\n                '.join([f'<div class="title-line">{line.upper()}</div>' for line in title_lines])
    
    # Extract bible quote
    bible_quote_text = ""
    bible_quote_ref = ""
    quote_match = re.search(r'<blockquote class="bible-quote-text"[^>]*>(.*?)</blockquote>', original_content, re.DOTALL)
    if quote_match:
        bible_quote_text = quote_match.group(1).strip()
    
    ref_match = re.search(r'<figcaption class="bible-quote-reference"[^>]*>[^<]*([^<]+)</figcaption>', original_content)
    if ref_match:
        bible_quote_ref = ref_match.group(1).strip()
    
    # Extract introduction (everything in introduction-paragraph)
    intro_match = re.search(r'<div class="introduction-paragraph dropcap-first-letter">(.*?)</div>', original_content, re.DOTALL)
    introduction_content = intro_match.group(1).strip() if intro_match else ""
    
    # Extract ALL body content (everything between chap-body start and endnotes start)
    body_start = original_content.find('<section class="chap-body"')
    if body_start == -1:
        body_content = ""
    else:
        body_start = original_content.find('>', body_start) + 1
        endnotes_start = original_content.find('<aside class="endnotes"')
        if endnotes_start == -1:
            # If no endnotes, find the end of chap-body section
            body_end = original_content.find('</section>', body_start)
            if body_end == -1:
                body_content = original_content[body_start:].strip()
            else:
                body_content = original_content[body_start:body_end].strip()
        else:
            body_content = original_content[body_start:endnotes_start].strip()
    
    # Clean up body content (remove the wrapping div if present)
    if body_content.startswith('<div class="content-area">'):
        content_end = body_content.rfind('</div>')
        if content_end != -1:
            body_content = body_content[len('<div class="content-area">'):content_end].strip()
    
    # Extract endnotes section
    endnotes_match = re.search(r'<aside class="endnotes"[^>]*>(.*?)</aside>', original_content, re.DOTALL)
    endnotes_content = endnotes_match.group(1).strip() if endnotes_match else ""
    
    # Extract quiz content
    quiz_match = re.search(r'<section class="quiz-container[^"]*"[^>]*>(.*?)</section>', original_content, re.DOTALL)
    quiz_content = quiz_match.group(1).strip() if quiz_match else ""
    
    # Extract worksheet content
    worksheet_match = re.search(r'<section class="worksheet[^"]*"[^>]*>(.*?)</section>', original_content, re.DOTALL)
    worksheet_content = worksheet_match.group(1).strip() if worksheet_match else ""
    
    # Extract closing/image-quote content
    closing_match = re.search(r'<section class="image-quote"[^>]*>(.*?)</section>', original_content, re.DOTALL)
    closing_content = closing_match.group(1).strip() if closing_match else ""
    
    # Generate chapter title for <title> tag
    chapter_title_full = ' '.join(title_words) if title_words else "Chapter"
    
    # Create ACISS-compliant XHTML
    aciss_content = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta charset="utf-8"/>
    <title>Chapter {roman_num} - {chapter_title_full}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
    <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body class="chapter-page">

<!-- PAGE 1: TITLE PAGE -->
<section class="chap-title">
    <!-- Roman numeral with brushstroke background - TOP CENTERED -->
    <div class="chapter-number-container">
        <div class="chapter-number-brush">
            <img class="brushstroke-img" src="../images/brushstroke.JPEG" alt="" />
            <div class="chapter-number-text">{roman_num}</div>
        </div>
    </div>
    
    <!-- Vertical title stack with accent bar -->
    <div class="chapter-title-container">
        <div class="title-stack">
            <div class="title-bar"></div>
            <div class="title-lines">
                {title_lines_html}
            </div>
        </div>
    </div>
    
    <!-- Bible quote in pill container -->
    <div class="bible-quote-container">
        <div class="bible-quote-text">{bible_quote_text}</div>
        <div class="bible-quote-reference">{bible_quote_ref}</div>
    </div>
    
    <!-- Introduction -->
    <div class="introduction-heading">Introduction</div>
    <div class="introduction-paragraph dropcap-first-letter">
        {introduction_content}
    </div>
</section>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGES 2-4: BODY CONTENT -->
<section class="chap-body">
    <div class="content-area">
{body_content}
    </div>
</section>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGE 5: ENDNOTES -->
<aside class="endnotes">
    {endnotes_content}
</aside>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGE 6: QUIZ & WORKSHEET -->
<section class="quiz-container chap-quiz avoid-break">
    {quiz_content}
</section>

<section class="worksheet avoid-break">
    {worksheet_content}
</section>

<!-- CLOSING -->
<section class="closing">
    {closing_content}
</section>

</body>
</html>'''
    
    return aciss_content

def process_chapter_file(input_file, output_file):
    """Process a single chapter file with complete content preservation."""
    print(f"🔄 Processing {Path(input_file).name}...")
    
    # Read original content
    with open(input_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Transform to ACISS structure
    aciss_content = transform_to_aciss_structure(original_content, Path(input_file).name)
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(aciss_content)
    
    # Verify content preservation
    original_text = extract_all_text_content(original_content)
    processed_text = extract_all_text_content(aciss_content)
    
    if original_text == processed_text:
        print(f"✅ CONTENT PRESERVED: {Path(output_file).name}")
        return True
    else:
        print(f"⚠️  Content differences detected in {Path(output_file).name}")
        print(f"   Original: {len(original_text)} chars")
        print(f"   Processed: {len(processed_text)} chars")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 chapter-transformer.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        success = process_chapter_file(input_file, output_file)
        if success:
            print("✅ Chapter transformation completed successfully!")
        else:
            print("⚠️  Chapter transformation completed with content differences.")
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error processing chapter: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)