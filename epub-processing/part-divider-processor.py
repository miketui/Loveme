#!/usr/bin/env python3
"""
Part Divider File Processor
Cleans and standardizes part divider files while preserving content.
"""
import re
import sys
from pathlib import Path

def process_part_divider(content):
    """Process part divider file to clean structure and fix references."""
    
    # Clean up empty whitespace sections
    content = re.sub(r'\s*\n\s*\n\s*\n', '\n\n', content)
    
    # Fix CSS link references (ensure they're properly formatted)
    content = re.sub(
        r'<link rel="stylesheet" type="text/css" href="../styles/fonts\.css"\s*/>\s*<link rel="stylesheet" type="text/css" href="../styles/style\.css"\s*/>',
        '<link rel="stylesheet" type="text/css" href="../styles/fonts.css" />\n    <link rel="stylesheet" type="text/css" href="../styles/style.css" />',
        content
    )
    
    # Ensure proper meta charset formatting
    content = re.sub(
        r'<meta charset="utf-8"\s*/>',
        '<meta charset="utf-8" />',
        content
    )
    
    # Remove any extra empty comment blocks
    content = re.sub(r'<!--\s*-->', '', content)
    
    # Clean up excessive whitespace but preserve structure
    content = re.sub(r'(\n\s*){3,}', '\n\n', content)
    
    # Ensure proper DOCTYPE and HTML structure
    if not content.strip().startswith('<!DOCTYPE html>'):
        # Fix DOCTYPE if it's missing
        content = re.sub(r'<!DOCTYPE[^>]*>', '<!DOCTYPE html>', content)
    
    return content

def verify_part_content(original, processed):
    """Verify part divider content is preserved."""
    def extract_text(html):
        # Remove HTML tags and comments
        text = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    orig_text = extract_text(original)
    proc_text = extract_text(processed)
    
    return orig_text == proc_text

def process_part_file(input_file, output_file):
    """Process a part divider file."""
    print(f"🔄 Processing part divider: {Path(input_file).name}")
    
    # Read original content
    with open(input_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Process content
    processed_content = process_part_divider(original_content)
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed_content)
    
    # Verify content preservation
    preserved = verify_part_content(original_content, processed_content)
    
    if preserved:
        print(f"✅ Part divider processed successfully: {Path(output_file).name}")
        return True
    else:
        print(f"⚠️  Content verification issue: {Path(output_file).name}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 part-divider-processor.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        success = process_part_file(input_file, output_file)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error processing part divider: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)