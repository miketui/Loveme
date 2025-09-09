#!/usr/bin/env python3
"""
Comprehensive Validation of All Processed Files
Validates content preservation and ACISS compliance for all 20 files.
"""
import glob
import sys
import subprocess
from pathlib import Path

def validate_file_content(input_file, output_file):
    """Validate content preservation using the validation script."""
    try:
        result = subprocess.run([
            "python3", "/root/repo/epub-processing/validate-content.py",
            str(input_file), str(output_file)
        ], capture_output=True, text=True)
        
        return result.returncode == 0, result.stdout.strip()
    except Exception as e:
        return False, f"Validation error: {e}"

def check_aciss_compliance(output_file):
    """Check if file follows ACISS structure requirements."""
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # Check for required ACISS elements
        required_elements = [
            ('chapter-number-brush', 'Roman numeral with brushstroke'),
            ('brushstroke-img', 'Brushstroke background image'),
            ('title-stack', 'Vertical title stack'),
            ('title-bar', 'Accent bar beside title'),
            ('title-line', 'Individual title lines'),
            ('bible-quote-container', 'Bible quote container'),
            ('page-break', 'Page break elements'),
        ]
        
        for element_class, description in required_elements:
            if element_class not in content:
                issues.append(f"Missing {description} ({element_class})")
        
        # Check for proper 6-page structure comments
        required_comments = [
            'PAGE 1: TITLE PAGE',
            'PAGES 2-4: BODY CONTENT',
            'PAGE 5: ENDNOTES',
            'PAGE 6: QUIZ & WORKSHEET'
        ]
        
        for comment in required_comments:
            if comment not in content:
                issues.append(f"Missing page structure comment: {comment}")
        
        return len(issues) == 0, issues
        
    except Exception as e:
        return False, [f"File read error: {e}"]

def main():
    """Run comprehensive validation on all processed files."""
    input_dir = Path("/root/repo/epub-processing/input")
    output_dir = Path("/root/repo/epub-processing/output")
    
    # Find all files
    all_files = sorted(glob.glob(str(input_dir / "*.xhtml")))
    
    print("🔍 COMPREHENSIVE VALIDATION REPORT")
    print("=" * 80)
    print(f"📋 Validating {len(all_files)} files for content preservation and ACISS compliance")
    print()
    
    content_preserved = 0
    aciss_compliant = 0
    total_files = len(all_files)
    
    validation_details = []
    
    for input_file in all_files:
        input_path = Path(input_file)
        output_path = output_dir / input_path.name
        
        print(f"📄 {input_path.name}")
        
        # Check if output file exists
        if not output_path.exists():
            print(f"   ❌ Output file missing")
            validation_details.append((input_path.name, False, False, ["Output file not found"]))
            continue
        
        # Validate content preservation
        content_ok, content_msg = validate_file_content(input_path, output_path)
        if content_ok:
            print(f"   ✅ Content preservation: PASSED")
            content_preserved += 1
        else:
            print(f"   ⚠️  Content preservation: {content_msg}")
        
        # Check ACISS compliance
        aciss_ok, aciss_issues = check_aciss_compliance(output_path)
        if aciss_ok:
            print(f"   ✅ ACISS compliance: PASSED")
            aciss_compliant += 1
        else:
            print(f"   ⚠️  ACISS compliance issues:")
            for issue in aciss_issues[:3]:  # Show first 3 issues
                print(f"      - {issue}")
            if len(aciss_issues) > 3:
                print(f"      ... and {len(aciss_issues) - 3} more issues")
        
        validation_details.append((input_path.name, content_ok, aciss_ok, aciss_issues))
        print()
    
    # Generate summary report
    print("=" * 80)
    print("📊 VALIDATION SUMMARY")
    print("-" * 40)
    print(f"📁 Total files processed: {total_files}")
    print(f"✅ Content preservation: {content_preserved}/{total_files} files")
    print(f"🎨 ACISS compliance: {aciss_compliant}/{total_files} files")
    print()
    
    # Success criteria
    content_success_rate = (content_preserved / total_files) * 100 if total_files > 0 else 0
    aciss_success_rate = (aciss_compliant / total_files) * 100 if total_files > 0 else 0
    
    print(f"📈 Content Preservation Rate: {content_success_rate:.1f}%")
    print(f"📈 ACISS Compliance Rate: {aciss_success_rate:.1f}%")
    print()
    
    if content_success_rate >= 95 and aciss_success_rate >= 90:
        print("🎉 SUCCESS: All validation criteria met!")
        print("   ✅ Content preservation ≥95%")
        print("   ✅ ACISS compliance ≥90%")
        overall_success = True
    else:
        print("⚠️  ATTENTION: Some validation criteria not fully met")
        if content_success_rate < 95:
            print(f"   ⚠️  Content preservation: {content_success_rate:.1f}% (target: ≥95%)")
        if aciss_success_rate < 90:
            print(f"   ⚠️  ACISS compliance: {aciss_success_rate:.1f}% (target: ≥90%)")
        overall_success = False
    
    print()
    print("=" * 80)
    
    # File breakdown by type
    chapters = [f for f in validation_details if '-chapter-' in f[0]]
    parts = [f for f in validation_details if '-Part-' in f[0]]
    
    print(f"📋 FILE TYPE BREAKDOWN:")
    print(f"   📖 Chapters: {len(chapters)}")
    print(f"   📑 Part dividers: {len(parts)}")
    
    return overall_success

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"💥 Validation error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)