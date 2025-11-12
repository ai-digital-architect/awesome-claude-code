# Hooks Directory

## What are Hooks?
Hooks are shell scripts or programs that execute automatically in response to Claude Code events.

## Common Hook Types
- **PreToolUse**: Runs before Claude uses a tool (security checks)
- **PostToolUse**: Runs after Claude uses a tool (formatting, logging)
- **PrePromptSubmission**: Runs before sending prompt to Claude
- **SessionEnd**: Runs when session ends (summaries)
- **Notification**: Runs when Claude waits for input
