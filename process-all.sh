#!/bin/bash

echo "🚀 Processing all 16 chapter files with ACISS transformation..."
echo "=================================================================="

INPUT_DIR="/root/repo/epub-processing/input"
OUTPUT_DIR="/root/repo/epub-processing/output"
TRANSFORMER="/root/repo/epub-processing/simple-transformer.py"

success_count=0
total_count=0

# Process each chapter file
for file in "$INPUT_DIR"/*-chapter-*.xhtml; do
    filename=$(basename "$file")
    echo -n "Processing $filename... "
    
    total_count=$((total_count + 1))
    
    if python3 "$TRANSFORMER" "$file" "$OUTPUT_DIR/$filename" 2>/dev/null; then
        echo "✅"
        success_count=$((success_count + 1))
    else
        echo "⚠️"
    fi
done

echo "=================================================================="
echo "📊 PROCESSING SUMMARY:"
echo "   ✅ Processed: $success_count"
echo "   📁 Total: $total_count"

if [ $success_count -eq $total_count ]; then
    echo "🎉 All chapters processed successfully!"
    exit 0
else
    echo "⚠️ Some chapters had processing differences"
    exit 1
fi