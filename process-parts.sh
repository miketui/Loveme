#!/bin/bash

echo "🚀 Processing 4 part divider files..."
echo "====================================="

INPUT_DIR="/root/repo/epub-processing/input"
OUTPUT_DIR="/root/repo/epub-processing/output"
PROCESSOR="/root/repo/epub-processing/part-divider-processor.py"

success_count=0
total_count=0

# Process each part divider file
for file in "$INPUT_DIR"/*-Part-*.xhtml; do
    filename=$(basename "$file")
    echo -n "Processing $filename... "
    
    total_count=$((total_count + 1))
    
    if python3 "$PROCESSOR" "$file" "$OUTPUT_DIR/$filename" 2>/dev/null; then
        echo "✅"
        success_count=$((success_count + 1))
    else
        echo "⚠️"
    fi
done

echo "====================================="
echo "📊 PART DIVIDERS SUMMARY:"
echo "   ✅ Processed: $success_count"
echo "   📁 Total: $total_count"

if [ $success_count -eq $total_count ]; then
    echo "🎉 All part dividers processed successfully!"
    exit 0
else
    echo "⚠️ Some part dividers had processing issues"
    exit 1
fi