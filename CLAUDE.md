# CLAUDE.md

## Project Overview
- **Name**: awesome-claude-code
- **Tech Stack**: React, Typescript, vite, java, spring, python
- **Description**: Set of awesome skills, hooks, commands and agents for claude code inspired by awesome-copilot prompts,instructions , chatmodes and workflows
- **Package Manager**: npm

## Architecture
- `src/` - Source code
- `tests/` - Test files
- `.claude/` - Claude Code configuration
- `dev/` - Development workspace
- `docs/` - Project documentation

## Key Commands

## Code Standards
- **Formatters**: Various
- **Linters**: Various
- Follow consistent naming conventions
- Write descriptive comments for complex logic
- Keep functions small and focused

## Testing Requirements
- Write tests for new functionality
- Maintain test coverage
- Test edge cases and error conditions
- Keep tests maintainable and readable

## Workflow Rules
- Always run tests before committing
- Use quality checkpoint commands (/qplan, /qcode, /qcheck)
- Follow TDD approach for new features

## Git Workflow
- Branch naming: `feature/description`, `fix/description`
- Commit messages: Clear, descriptive, present tense
- Always pull before pushing
- Review changes before committing

## Security
- Never commit sensitive files (.env, .key, .pem, etc.)
- Use environment variables for secrets
- Validate all user input
- Follow security best practices

## When Starting Work
1. Review dev/active/*.md for current context
2. Check dev/plans/*.md for roadmap
3. Ask questions before making assumptions
4. Plan in dev/scratch/SCRATCHPAD.md first

## Custom Commands Available
- `/qplan` - Analyze plan consistency
- `/qcode` - Implement with quality checks
- `/qcheck` - Skeptical code review
- `/tdd` - Test-driven development workflow
- `/create-prd` - Generate PRD from description
- `/plan-feature` - Plan feature implementation
- `/usage` - View token usage report

## Enhanced Features
- **Security Hooks**: Automatic protection of sensitive files
- **Auto-Format**: Code formatting after edits
- **Token Tracking**: Telemetry enabled for usage monitoring
  - Track usage: `npx ccusage@latest daily`
  - Monitor blocks: `npx ccusage@latest blocks`
- **Implementation Logging**: All actions logged to `.claude/logs/`
  - `bash-commands.log` - Command history
  - `implementation-steps.jsonl` - Detailed action log
  - `tool-usage.log` - Tool usage tracking
- **Sandboxing**: Safe command execution environment
