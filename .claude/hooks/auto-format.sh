#!/usr/bin/env bash
set -euo pipefail

# Auto-format files after edits
# Reads file path from JSON input

# Extract file path from tool input
FILE_PATH=$(jq -r '.tool_input.file_path // ""')

if [[ -z "$FILE_PATH" ]]; then
    exit 0
fi

# TypeScript/JavaScript files
if [[ "$FILE_PATH" =~ \.(ts|tsx|js|jsx)$ ]]; then
    if command -v prettier >/dev/null 2>&1; then
        prettier --write "$FILE_PATH" 2>/dev/null || true
    fi
    if command -v eslint >/dev/null 2>&1; then
        eslint --fix "$FILE_PATH" 2>/dev/null || true
    fi
fi

# Python files
if [[ "$FILE_PATH" =~ \.py$ ]]; then
    if command -v black >/dev/null 2>&1; then
        black "$FILE_PATH" 2>/dev/null || true
    fi
    if command -v isort >/dev/null 2>&1; then
        isort "$FILE_PATH" 2>/dev/null || true
    fi
fi

# Go files
if [[ "$FILE_PATH" =~ \.go$ ]]; then
    if command -v gofmt >/dev/null 2>&1; then
        gofmt -w "$FILE_PATH" 2>/dev/null || true
    fi
fi

# Rust files
if [[ "$FILE_PATH" =~ \.rs$ ]]; then
    if command -v rustfmt >/dev/null 2>&1; then
        rustfmt "$FILE_PATH" 2>/dev/null || true
    fi
fi

exit 0
