#!/usr/bin/env bash
set -euo pipefail

# Track tool usage for monitoring
LOG_FILE="$CLAUDE_PROJECT_DIR/.claude/logs/tool-usage.log"

# Extract tool name and timestamp
TOOL_NAME=$(jq -r '.tool_name // "unknown"')
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Log the usage
echo "$TIMESTAMP - $TOOL_NAME" >> "$LOG_FILE"

exit 0
