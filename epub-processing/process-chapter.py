#!/usr/bin/env python3
"""
ACISS Chapter Processing Script
Transforms XHTML chapter files to match ACISS design system while preserving 100% content.
"""
import re
import sys
from pathlib import Path
from roman_numerals import get_roman_numeral

def extract_chapter_info(content):
    """Extract chapter number, title, and bible quote from existing content."""
    # Extract chapter number from title
    title_match = re.search(r'<title>Chapter ([IVXLC]+)[^<]*</title>', content)
    if title_match:
        roman_num = title_match.group(1)
    else:
        # Fallback to extract from filename or content
        roman_num = "I"
    
    # Extract title words from existing chapter-title-word elements
    title_words = []
    word_matches = re.findall(r'<h1 class="[^"]*chapter-title-word[^"]*">([^<]+)</h1>', content)
    if word_matches:
        title_words = word_matches
    else:
        # Fallback - extract from title tag
        title_match = re.search(r'<title>Chapter [IVXLC]+ [–-] ([^<]+)</title>', content)
        if title_match:
            title_text = title_match.group(1).upper()
            title_words = title_text.split()
    
    # Extract bible quote
    quote_text = ""
    quote_ref = ""
    quote_match = re.search(r'<blockquote class="bible-quote-text"[^>]*>(.*?)</blockquote>', content, re.DOTALL)
    if quote_match:
        quote_text = quote_match.group(1).strip()
    
    ref_match = re.search(r'<figcaption class="bible-quote-reference"[^>]*>[^>]*</figcaption>', content, re.DOTALL)
    if ref_match:
        ref_content = ref_match.group(0)
        ref_text_match = re.search(r'>([^<]+)</figcaption>', ref_content)
        if ref_text_match:
            quote_ref = ref_text_match.group(1).strip()
    
    return roman_num, title_words, quote_text, quote_ref

def extract_introduction(content):
    """Extract introduction paragraph with dropcap."""
    intro_match = re.search(r'<div class="introduction-paragraph dropcap-first-letter">(.*?)</div>', content, re.DOTALL)
    if intro_match:
        return intro_match.group(1).strip()
    return ""

def extract_body_content(content):
    """Extract all body content sections."""
    # Find content between chap-body section tags
    body_match = re.search(r'<section class="chap-body"[^>]*>(.*?)</section>', content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1).strip()
        # Remove the content-area wrapper if present but keep all content inside
        content_match = re.search(r'<div class="content-area">(.*?)</div>', body_content, re.DOTALL)
        if content_match:
            return content_match.group(1).strip()
        return body_content
    
    # Fallback: try to extract content between chap-title and endnotes
    title_end = content.find('</section>', content.find('class="chap-title"'))
    endnotes_start = content.find('<aside class="endnotes"')
    if title_end != -1 and endnotes_start != -1:
        body_section = content[title_end:endnotes_start]
        # Extract content from the body section
        content_match = re.search(r'<div class="content-area">(.*?)</div>', body_section, re.DOTALL)
        if content_match:
            return content_match.group(1).strip()
        # If no content-area, try to find the raw content
        section_match = re.search(r'<section[^>]*>(.*)', body_section, re.DOTALL)
        if section_match:
            return section_match.group(1).strip()
    
    return ""

def extract_endnotes(content):
    """Extract endnotes/footnotes section."""
    endnotes_match = re.search(r'<aside class="endnotes"[^>]*>(.*?)</aside>', content, re.DOTALL)
    if endnotes_match:
        return endnotes_match.group(1).strip()
    return ""

def extract_quiz_content(content):
    """Extract quiz questions and options."""
    quiz_match = re.search(r'<section class="quiz-container[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL)
    if quiz_match:
        return quiz_match.group(1).strip()
    return ""

def extract_worksheet_content(content):
    """Extract worksheet content."""
    worksheet_match = re.search(r'<section class="worksheet[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL)
    if worksheet_match:
        return worksheet_match.group(1).strip()
    return ""

def extract_closing_content(content):
    """Extract closing image-quote section."""
    closing_match = re.search(r'<section class="image-quote"[^>]*>(.*?)</section>', content, re.DOTALL)
    if closing_match:
        return closing_match.group(1).strip()
    return ""

def break_title_into_lines(title_words, max_lines=6):
    """Break title words into vertical lines (3-6 lines maximum)."""
    if len(title_words) <= max_lines:
        return title_words
    
    # For longer titles, combine shorter words
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
    
    return lines[:max_lines]

def generate_aciss_chapter(roman_num, title_words, quote_text, quote_ref, introduction, 
                          body_content, endnotes, quiz_content, worksheet_content, closing_content, chapter_title_full):
    """Generate complete ACISS-compliant chapter XHTML."""
    
    title_lines = break_title_into_lines(title_words)
    title_lines_html = '\n                '.join([f'<div class="title-line">{line.upper()}</div>' for line in title_lines])
    
    template = f'''<?xml version="1.0" encoding="utf-8"?>
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
        <div class="bible-quote-text">{quote_text}</div>
        <div class="bible-quote-reference">{quote_ref}</div>
    </div>
    
    <!-- Introduction -->
    <div class="introduction-heading">Introduction</div>
    <div class="introduction-paragraph dropcap-first-letter">
        {introduction}
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
    {endnotes}
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
    
    return template

def process_chapter_file(input_file, output_file):
    """Process a single chapter file."""
    print(f"Processing {Path(input_file).name}...")
    
    # Read original content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all components
    roman_num, title_words, quote_text, quote_ref = extract_chapter_info(content)
    introduction = extract_introduction(content)
    body_content = extract_body_content(content)
    endnotes = extract_endnotes(content)
    quiz_content = extract_quiz_content(content)
    worksheet_content = extract_worksheet_content(content)
    closing_content = extract_closing_content(content)
    
    # Generate chapter title for <title> tag
    chapter_title_full = ' '.join(title_words)
    
    # Generate ACISS-compliant XHTML
    aciss_content = generate_aciss_chapter(
        roman_num, title_words, quote_text, quote_ref, 
        introduction, body_content, endnotes, 
        quiz_content, worksheet_content, closing_content, 
        chapter_title_full
    )
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(aciss_content)
    
    print(f"✅ Generated ACISS version: {Path(output_file).name}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 process-chapter.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        process_chapter_file(input_file, output_file)
        print("Chapter processing completed successfully!")
    except Exception as e:
        print(f"❌ Error processing chapter: {e}")
        sys.exit(1)