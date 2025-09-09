#!/usr/bin/env python3
"""
Roman Numeral Conversion for EPUB Processing
"""

ROMAN_NUMERALS = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
    11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI'
}

def get_roman_numeral(chapter_number):
    """Convert chapter number to Roman numeral."""
    return ROMAN_NUMERALS.get(chapter_number, str(chapter_number))

def extract_chapter_number(filename):
    """Extract chapter number from filename like '9-chapter-i-...'."""
    import re
    match = re.search(r'(\d+)-chapter-([ivx]+)', filename.lower())
    if match:
        return int(match.group(1)) - 8  # Adjust for starting at chapter I
    return None

if __name__ == "__main__":
    # Test the conversion
    for i in range(1, 17):
        print(f"Chapter {i}: {get_roman_numeral(i)}")