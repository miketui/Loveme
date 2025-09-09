#!/usr/bin/env python3
"""
Content Validation Script for EPUB XHTML Processing
Ensures 100% content preservation by comparing text content between original and processed files.
"""
import sys
import re
from pathlib import Path

def extract_text_content(xhtml_file):
    """Extract only text content from XHTML file, ignoring markup and formatting."""
    try:
        with open(xhtml_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {xhtml_file}: {e}")
        return ""
    
    # Remove XML/HTML tags
    text = re.sub(r'<[^>]+>', '', content)
    
    # Remove XML declarations and DOCTYPE
    text = re.sub(r'<\?xml[^>]*\?>', '', text)
    text = re.sub(r'<!DOCTYPE[^>]*>', '', text)
    
    # Remove HTML entities
    html_entities = {
        '&quot;': '"',
        '&apos;': "'",
        '&lt;': '<',
        '&gt;': '>',
        '&amp;': '&',
        '&#x27;': "'",
        '&nbsp;': ' '
    }
    for entity, char in html_entities.items():
        text = text.replace(entity, char)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # Remove common formatting artifacts
    text = re.sub(r'^\s*→\s*', '', text, flags=re.MULTILINE)  # Line number prefixes
    text = re.sub(r'\s*___+\s*', '', text)  # Worksheet lines
    
    return text

def validate_preservation(original_file, processed_file):
    """Validate that all content from original file is preserved in processed file."""
    original_text = extract_text_content(original_file)
    processed_text = extract_text_content(processed_file)
    
    if not original_text:
        print(f"⚠️  WARNING: Could not extract content from {original_file}")
        return False
    
    if not processed_text:
        print(f"❌ ERROR: Could not extract content from {processed_file}")
        return False
    
    # Compare content
    if original_text == processed_text:
        print(f"✅ Content preservation VERIFIED: {Path(processed_file).name}")
        return True
    else:
        print(f"❌ Content preservation FAILED: {Path(processed_file).name}")
        
        # Show differences for debugging
        orig_len = len(original_text)
        proc_len = len(processed_text)
        print(f"   Original length: {orig_len} characters")
        print(f"   Processed length: {proc_len} characters")
        
        if abs(orig_len - proc_len) < 100:
            # Show character-by-character differences for small discrepancies
            for i, (o, p) in enumerate(zip(original_text, processed_text)):
                if o != p:
                    context_start = max(0, i-20)
                    context_end = min(len(original_text), i+20)
                    print(f"   First difference at position {i}:")
                    print(f"   Original: ...{original_text[context_start:context_end]}...")
                    print(f"   Processed: ...{processed_text[context_start:context_end]}...")
                    break
        
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 validate-content.py <original_file> <processed_file>")
        sys.exit(1)
    
    original_file = sys.argv[1]
    processed_file = sys.argv[2]
    
    if not Path(original_file).exists():
        print(f"❌ ERROR: Original file not found: {original_file}")
        sys.exit(1)
    
    if not Path(processed_file).exists():
        print(f"❌ ERROR: Processed file not found: {processed_file}")
        sys.exit(1)
    
    success = validate_preservation(original_file, processed_file)
    sys.exit(0 if success else 1)