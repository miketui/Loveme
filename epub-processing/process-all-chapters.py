#!/usr/bin/env python3
"""
Batch Process All Chapters with ACISS Transformation
"""
import os
import sys
from pathlib import Path
import subprocess
import glob

def process_all_chapters():
    """Process all 16 chapter files."""
    
    input_dir = Path("/root/repo/epub-processing/input")
    output_dir = Path("/root/repo/epub-processing/output")
    transformer_script = Path("/root/repo/epub-processing/simple-transformer.py")
    
    # Find all chapter files (not part dividers)
    chapter_files = sorted(glob.glob(str(input_dir / "*-chapter-*.xhtml")))
    
    print(f"🚀 Starting batch processing of {len(chapter_files)} chapter files...")
    print("=" * 60)
    
    processed_count = 0
    failed_count = 0
    
    for chapter_file in chapter_files:
        input_path = Path(chapter_file)
        output_path = output_dir / input_path.name
        
        try:
            # Run the transformer
            result = subprocess.run([
                "python3", str(transformer_script),
                str(input_path), str(output_path)
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                processed_count += 1
                print(f"✅ {input_path.name}")
            else:
                failed_count += 1
                print(f"❌ {input_path.name}: {result.stderr.strip()}")
                
        except Exception as e:
            failed_count += 1
            print(f"❌ {input_path.name}: {e}")
    
    print("=" * 60)
    print(f"📊 Processing Summary:")
    print(f"   ✅ Successfully processed: {processed_count}")
    print(f"   ❌ Failed: {failed_count}")
    print(f"   📁 Total chapters: {len(chapter_files)}")
    
    if failed_count == 0:
        print("🎉 All chapters processed successfully!")
        return True
    else:
        print("⚠️  Some chapters failed processing.")
        return False

if __name__ == "__main__":
    try:
        success = process_all_chapters()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"💥 Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)