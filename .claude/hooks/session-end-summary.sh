#!/usr/bin/env bash
set -euo pipefail

# Generate session summary with token usage
echo "📊 Session Summary"
echo "=================="

# Display token usage if ccusage is available
if command -v npx >/dev/null 2>&1; then
    echo ""
    echo "Token Usage (Today):"
    npx --yes ccusage@latest daily 2>/dev/null | tail -n 5 || echo "Install ccusage: npm install -g ccusage"

    echo ""
    echo "Current 5-hour Block:"
    npx --yes ccusage@latest blocks 2>/dev/null | tail -n 5 || true
fi

# Show files modified this session
echo ""
echo "Files Modified:"
if [[ -f "$CLAUDE_PROJECT_DIR/.claude/logs/implementation-steps.jsonl" ]]; then
    tail -n 20 "$CLAUDE_PROJECT_DIR/.claude/logs/implementation-steps.jsonl" | \
        jq -r '.tool_input.file_path // empty' | \
        sort -u | \
        head -n 10 || echo "No files modified"
fi

echo ""
echo "📈 View full usage: npx ccusage@latest daily"
echo "🔍 Monitor live: npx ccusage@latest blocks --live"

exit 0
