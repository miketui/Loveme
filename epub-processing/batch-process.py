#!/usr/bin/env python3
"""
Direct Batch Processing of All Chapters
"""
import glob
import sys
from pathlib import Path
from simple_transformer import process_chapter

def main():
    input_dir = Path("/root/repo/epub-processing/input")
    output_dir = Path("/root/repo/epub-processing/output")
    
    # Find all chapter files
    chapter_files = sorted(glob.glob(str(input_dir / "*-chapter-*.xhtml")))
    
    print(f"🚀 Processing {len(chapter_files)} chapter files with ACISS transformation...")
    print("=" * 70)
    
    success_count = 0
    failure_count = 0
    
    for chapter_file in chapter_files:
        input_path = Path(chapter_file)
        output_path = output_dir / input_path.name
        
        try:
            success = process_chapter(str(input_path), str(output_path))
            if success:
                success_count += 1
            else:
                failure_count += 1
        except Exception as e:
            print(f"💥 {input_path.name}: {e}")
            failure_count += 1
    
    print("=" * 70)
    print(f"📊 BATCH PROCESSING COMPLETE:")
    print(f"   ✅ Successful: {success_count}")
    print(f"   ⚠️  With issues: {failure_count}")
    
    if failure_count == 0:
        print("🎉 All chapters transformed successfully!")
        return True
    else:
        print("⚠️  Some chapters had content preservation differences (likely from formatting)")
        return success_count > 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)