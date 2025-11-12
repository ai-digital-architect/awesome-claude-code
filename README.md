# 🚀 awesome-claude-code

> 📝 **Quick Start**: This project is configured with [Claude Code](https://docs.claude.com/claude-code) for AI-assisted development.

## 📋 Table of Contents

- [Overview](#-overview)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Claude Code Integration](#-claude-code-integration)
- [Available Commands](#-available-commands)
- [Quality Workflows](#-quality-workflows)
- [Security & Monitoring](#-security--monitoring)
- [Documentation](#-documentation)
- [Contributing](#-contributing)

## 🎯 Overview

Set of awesome skills, hooks, commands and agents for claude code inspired by awesome-copilot prompts,instructions , chatmodes and workflows

### ✨ Key Features

- 🔒 **Security**: Automatic protection of sensitive files
- 📊 **Token Tracking**: Built-in usage monitoring
- 🎨 **Auto-Formatting**: Automatic code formatting on save
- 📝 **Activity Logging**: Complete audit trail
- 🤖 **AI Agents**: Specialized agents for different tasks
- ✅ **Quality Commands**: Built-in quality checkpoints

## 🚀 Quick Start

### Prerequisites

- [Claude Code](https://docs.claude.com/claude-code) installed
- Git configured

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd awesome-claude-code

# Install dependencies

# Optional: Install token tracking
npm install -g ccusage

# Start using Claude Code
claude code
```

### First Steps

1. 📖 Read [CLAUDE.md](CLAUDE.md) for project-specific guidelines
2. 🤖 Review [AGENTS.md](AGENTS.md) to understand available AI agents
3. 📚 Check [docs/onboarding/](docs/onboarding/) for detailed setup guides

## 📁 Project Structure

```
.
├── .claude/              # 🤖 Claude Code configuration
│   ├── agents/          # AI agent definitions
│   ├── commands/        # Slash commands
│   ├── hooks/           # Automation scripts
│   ├── logs/            # Activity logs
│   ├── skills/          # Domain expertise - claude skills
│   └── settings.json    # Configuration
│
├── dev/                 # 🛠️ Development workspace
│   ├── active/         # Current work context
│   ├── plans/          # Planning documents
│   └── scratch/        # Scratchpad for ideas
│
├── docs/                # 📚 Documentation
│   ├── architecture/   # Architecture docs
│   ├── decisions/      # ADRs (Architecture Decision Records)
│   └── onboarding/     # Setup & onboarding guides
│
├── src/                 # 💻 Source code
├── tests/               # 🧪 Test files
│
├── AGENTS.md            # 🤖 AI agent catalog
├── CLAUDE.md            # 📋 Project memory for Claude
└── README.md            # 📖 This file
```

## 💻 Development

### Running the Project

```bash
```

### Development Workflow

1. **Check Context**: Review `dev/active/context.md` for current work
2. **Plan**: Use `/plan-feature` or write plans in `dev/plans/`
3. **Implement**: Use quality commands (`/qplan`, `/qcode`, `/qcheck`)
4. **Test**: Run tests after each change
5. **Commit**: Use clear, descriptive commit messages

## 🤖 Claude Code Integration

### What is Claude Code?

Claude Code is an AI-powered development assistant that helps with:
- 🔍 Code exploration and understanding
- 📝 Planning and architecture
- ✍️ Implementation and refactoring
- 🐛 Debugging and troubleshooting
- 📚 Documentation generation

### Available AI Agents

This project includes specialized AI agents for different tasks:

| Agent | Use Case | Example |
|-------|----------|---------|
| 🔍 **Explore** | Find code patterns | `"Find all API endpoints (quick)"` |
| 📋 **Plan** | Design features | `"Plan authentication system (medium)"` |
| 🛠️ **General-Purpose** | Complex tasks | `"Research and implement OAuth2"` |
| ⚙️ **Statusline** | Configure UI | `"Setup status line with git info"` |

📖 **See [AGENTS.md](AGENTS.md) for complete agent documentation**

## 🎯 Available Commands

### Slash Commands

Run these commands in Claude Code with `/command-name`:

| Command | Description | Usage |
|---------|-------------|-------|
| `/qplan` | 📋 Analyze plan consistency | Plan validation before coding |
| `/qcode` | ✅ Implement with quality checks | Quality-focused implementation |
| `/qcheck` | 🔍 Skeptical code review | Comprehensive code review |
| `/tdd` | 🧪 Test-driven development | TDD workflow automation |
| `/create-prd` | 📄 Create PRD | Generate product requirements |
| `/plan-feature` | 🗺️ Plan feature | Complete feature planning |
| `/usage` | 📊 Token usage report | View Claude Code usage stats |

### Quick Command Reference

```bash
# Plan a feature
/plan-feature "user authentication"

# Implement with quality checks
/qcode

# Review code
/qcheck

# Check token usage
/usage
```

## ✨ Quality Workflows

### 1. Feature Development Workflow

```
📋 /qplan          → Validate approach
    ↓
✍️  /qcode         → Implement with quality
    ↓
🔍 /qcheck        → Review & verify
    ↓
✅ Commit         → Ship with confidence
```

### 2. Test-Driven Development

```
🧪 /tdd           → Write tests first
    ↓
✅ Implement      → Make tests pass
    ↓
♻️  Refactor      → Clean up code
    ↓
🔍 /qcheck        → Final review
```

### 3. Planning Workflow

```
🔍 Explore        → Understand codebase
    ↓
📋 /plan-feature  → Design solution
    ↓
👀 Review         → Get approval
    ↓
🛠️ Implement      → Build feature
```

## 🔒 Security & Monitoring

### Security Features

This project includes automatic security protections:

- 🚫 **Sensitive File Protection**: `.env`, `.key`, `.pem` files blocked
- 📝 **Command Logging**: All bash commands logged
- 🔐 **Sandboxed Execution**: Safe command isolation
- ⛔ **Restricted Commands**: `curl`, `wget`, `sudo` blocked

### Monitoring & Logging

Track all activity in `.claude/logs/`:

```bash
# View bash command history
cat .claude/logs/bash-commands.log

# View implementation steps (JSON)
tail -f .claude/logs/implementation-steps.jsonl

# View tool usage
cat .claude/logs/tool-usage.log
```

### Token Usage Tracking

Monitor your Claude Code usage:

```bash
# Daily usage summary
npx ccusage@latest daily

# Current 5-hour block
npx ccusage@latest blocks

# Monthly breakdown
npx ccusage@latest monthly

# Or use the slash command
/usage
```

## 📚 Documentation

### Key Documentation Files

| File | Purpose |
|------|---------|
| [CLAUDE.md](CLAUDE.md) | 📋 Project memory & guidelines for Claude |
| [AGENTS.md](AGENTS.md) | 🤖 AI agent catalog & usage guide |
| [docs/onboarding/CLAUDE_SETUP.md](docs/onboarding/CLAUDE_SETUP.md) | 🚀 Setup guide |
| [docs/onboarding/PROJECT_STRUCTURE.md](docs/onboarding/PROJECT_STRUCTURE.md) | 📁 Structure overview |

### Creating Documentation

```bash
# Architecture Decision Record
cp docs/decisions/ADR-template.md docs/decisions/ADR-001-my-decision.md

# Update project context
vim dev/active/context.md

# Add planning docs
vim dev/plans/feature-name-plan.md
```

## 🤝 Contributing

### Before Contributing

1. 📖 Read [CLAUDE.md](CLAUDE.md) for project standards
2. 🤖 Familiarize yourself with [AGENTS.md](AGENTS.md)
4. 🎨 Code is auto-formatted on save

### Contribution Workflow

```bash
# 1. Create feature branch
git checkout -b feature/my-feature

# 2. Use quality commands
/qplan          # Validate approach
/qcode          # Implement
/qcheck         # Review

# 3. Ensure tests pass

# 4. Commit with clear message
git commit -m "feat: add user authentication"

# 5. Push and create PR
git push origin feature/my-feature
```

### Commit Message Convention

```
feat: Add new feature
fix: Fix bug
docs: Update documentation
style: Format code
refactor: Refactor code
test: Add tests
chore: Maintenance tasks
```

## 🛠️ Customization

### Disabling Features

Edit `.claude/settings.json` to customize:

```json
{
  "hooks": {
    "PostToolUse": [
      // Comment out hooks you don't want
    ]
  }
}
```

### Personal Overrides

Create `.claude/settings.local.json` (gitignored):

```json
{
  "hooks": {
    "PostToolUse": []
  }
}
```

## 📊 Project Stats

<!-- Add badges here -->

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## 📞 Support

- 📖 **Documentation**: Check [docs/](docs/) folder
- 🐛 **Issues**: [GitHub Issues](../../issues)
- 💬 **Discussions**: [GitHub Discussions](../../discussions)
- 📧 **Contact**: [Add your contact]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**🚀 Built with [Claude Code](https://docs.claude.com/claude-code)**

*Enhance your development workflow with AI-powered assistance*

</div>
