# Claude Code Commands Reference

This document catalogs all Claude Code commands converted from the [awesome-copilot](https://github.com/github/awesome-copilot) prompts library.

## Overview

These commands provide reusable workflows for common development tasks, following the pattern established by GitHub Copilot's prompt system but adapted for Claude Code's command structure.

## Available Commands

### Planning & Documentation Commands

#### `/create-spec` - Create Specification
Generate comprehensive specification files optimized for AI consumption and human understanding.

**Use when:**
- Starting a new feature
- Documenting existing functionality
- Planning major refactoring
- Defining requirements

**Output:** `SPEC.md` or `docs/specs/{feature-name}.md`

---

#### `/create-impl-plan` - Create Implementation Plan
Generate detailed, phased implementation plans for features, refactoring, or system upgrades.

**Use when:**
- Breaking down large features
- Planning complex refactoring
- Estimating effort and timeline
- Coordinating team work

**Output:** `docs/plans/IMPLEMENTATION_PLAN.md`

---

#### `/arch-blueprint` - Architecture Blueprint Generator
Analyze the codebase to create detailed architectural documentation.

**Use when:**
- Onboarding new team members
- Planning major refactoring
- Documenting legacy systems
- Preparing for architecture reviews

**Output:** `docs/architecture/ARCHITECTURE.md`

---

#### `/adr` - Architectural Decision Record
Document significant technical and architectural decisions using the ADR format.

**Use when:**
- Making major technical decisions
- Choosing between alternatives
- Documenting trade-offs
- Establishing technical direction

**Output:** `docs/adr/ADR-{number}-{title}.md`

---

### Workflow Enhancement Commands

#### `/first-ask` - Interactive Scope Interrogation
Interactive workflow that interrogates project scope, deliverables, and constraints before starting implementation.

**Use when:**
- Starting new features or projects
- Requirements are unclear
- Multiple stakeholders involved
- Need to clarify expectations

**Output:** `docs/briefs/{project-name}-brief.md`

---

#### `/boost-prompt` - Refine Your Request
Improve the quality and clarity of user prompts through structured interrogation and refinement.

**Use when:**
- User requests are vague
- Multiple interpretations exist
- Need to surface hidden assumptions
- Want to improve prompt quality

**Output:** Refined, specific prompt for better results

---

### Code Quality Commands

#### `/add-edu-comments` - Add Educational Comments
Annotate code with instructional comments and explanations to help others understand the implementation.

**Use when:**
- Complex algorithms need explanation
- Onboarding new developers
- Documenting design patterns
- Creating learning resources

**Output:** Updated code files with educational comments

---

#### `/conventional-commit` - Conventional Commit Message Generator
Generate standardized commit messages following the Conventional Commits specification.

**Use when:**
- Creating commits
- Need consistent commit history
- Supporting automated changelog
- Following semantic versioning

**Output:** Formatted commit message for review

---

### Research & Exploration Commands

#### `/tech-spike` - Technical Spike Document
Create documentation for technical exploration, research, and proof-of-concept work.

**Use when:**
- Evaluating new technologies
- Investigating performance issues
- Planning complex features
- Reducing technical uncertainty

**Output:** `docs/spikes/spike-{date}-{title}.md`

---

### GitHub Integration Commands

#### `/github-issues-from-spec` - Create GitHub Issues from Specification
Generate GitHub issues from a specification document, breaking down requirements into trackable work items.

**Use when:**
- Converting specs to actionable tasks
- Planning sprint work
- Distributing work across team
- Tracking feature progress

**Output:** Set of GitHub issues or markdown files

---

## Command Categories

### 📋 Planning (4 commands)
- `/create-spec` - Specification documents
- `/create-impl-plan` - Implementation planning
- `/arch-blueprint` - Architecture documentation
- `/adr` - Decision records

### 🔄 Workflows (2 commands)
- `/first-ask` - Scope clarification
- `/boost-prompt` - Prompt refinement

### ✨ Code Quality (2 commands)
- `/add-edu-comments` - Educational annotations
- `/conventional-commit` - Commit messages

### 🔬 Research (1 command)
- `/tech-spike` - Technical investigation

### 🐙 GitHub (1 command)
- `/github-issues-from-spec` - Issue generation

## Usage Patterns

### Starting a New Feature

```bash
# 1. Clarify scope
/first-ask

# 2. Create specification
/create-spec

# 3. Create implementation plan
/create-impl-plan

# 4. Generate GitHub issues
/github-issues-from-spec

# 5. Begin development...
```

### Making Architectural Decisions

```bash
# 1. Research the options
/tech-spike

# 2. Document the decision
/adr

# 3. Update architecture docs
/arch-blueprint
```

### Improving Code Understanding

```bash
# 1. Add educational comments
/add-edu-comments

# 2. Document architecture
/arch-blueprint

# 3. Create learning materials
```

### Committing Changes

```bash
# 1. Generate commit message
/conventional-commit

# 2. Review and commit
git commit -m "..."
```

## Conversion from GitHub Copilot Prompts

These commands were converted from GitHub Copilot's `prompts/*.prompt.md` files following these principles:

1. **Structure**: Adapted from `.github/prompts/` to `.claude/commands/`
2. **Format**: Markdown-based with clear sections
3. **Usage**: Invoked via `/command-name` syntax
4. **Context**: Optimized for Claude Code's capabilities

### Mapping

| GitHub Copilot Prompt | Claude Code Command | Status |
|----------------------|---------------------|--------|
| create-specification.prompt.md | `/create-spec` | ✅ Converted |
| create-implementation-plan.prompt.md | `/create-impl-plan` | ✅ Converted |
| architecture-blueprint.prompt.md | `/arch-blueprint` | ✅ Converted |
| architectural-decision-record.prompt.md | `/adr` | ✅ Converted |
| first-ask.prompt.md | `/first-ask` | ✅ Converted |
| boost-prompt.prompt.md | `/boost-prompt` | ✅ Converted |
| add-educational-comments.prompt.md | `/add-edu-comments` | ✅ Converted |
| technical-spike.prompt.md | `/tech-spike` | ✅ Converted |
| conventional-commit.prompt.md | `/conventional-commit` | ✅ Converted |
| github-issues-from-spec.prompt.md | `/github-issues-from-spec` | ✅ Converted |

## Additional Prompts Available for Conversion

The following prompts from awesome-copilot are available but not yet converted:

### .NET/C# Development (8 prompts)
- .NET Upgrade Analysis
- .NET/C# Best Practices
- .NET/C# Design Pattern Review
- C# Async Programming
- C# Documentation
- ASP.NET Framework Containerization
- ASP.NET Core Docker
- ASP.NET Minimal API with OpenAPI

### Cloud & DevOps (3 prompts)
- Azure Cosmos DB Data Modeling
- Azure Cost Optimize
- Azure Resource Health Diagnosis

### Code Generation (3 prompts)
- Spring Boot Java Project
- Spring Boot Kotlin Project
- Playwright Automation

### GitHub Integration (4 prompts)
- GitHub Actions Workflow Specification
- Create GitHub Issues from Implementation Plan
- GitHub Pull Request from Specification
- Unmet Requirements Issues

### Documentation (3 prompts)
- Create README
- Create LLMs.txt
- AGENTS.md Generator

### AI & Prompt Engineering (2 prompts)
- AI Prompt Engineering Safety Review
- Model Recommendation

### Other (2 prompts)
- Technology Stack Blueprint
- Code Exemplars Blueprint

**Total:** 27 additional prompts available for future conversion

## Contributing

To add new commands:

1. Create a markdown file in `.claude/commands/{command-name}.md`
2. Follow the structure of existing commands
3. Include clear sections: Purpose, Task, Output Format, Examples
4. Test the command thoroughly
5. Update this documentation

## Best Practices

**Command Design:**
- Keep commands focused on one task
- Provide clear instructions
- Include examples
- Define output format
- Specify when to use

**Command Usage:**
- Read command documentation first
- Understand expected output
- Review generated content
- Customize for your needs
- Commit commands to version control

## Resources

- [awesome-copilot Repository](https://github.com/github/awesome-copilot)
- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Architectural Decision Records](https://adr.github.io/)

## Version History

- **v1.0** (2025-01-11) - Initial conversion of 10 core commands
  - Planning & documentation commands
  - Workflow enhancement commands
  - Code quality commands
  - Research commands
  - GitHub integration commands

---

**Note:** This is a living document. Commands will be added and updated as the awesome-copilot repository evolves and new use cases emerge.
