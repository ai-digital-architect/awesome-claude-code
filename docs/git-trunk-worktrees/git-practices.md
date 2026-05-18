# The Complete Developer's Workflow Guide

> Git, Git Worktrees, GitHub Actions, GitHub Workflows, and AI Coding Harnesses with Trunk-Based Development

A comprehensive reference based on official documentation and 2026 industry best practices.

---

## Table of Contents

- [Introduction](#introduction)
- [Part I: Git Fundamentals & Best Practices](#part-i-git-fundamentals--best-practices)
- [Part II: Git Worktrees Deep Dive](#part-ii-git-worktrees-deep-dive)
- [Part III: GitHub Actions](#part-iii-github-actions)
- [Part IV: GitHub Workflows](#part-iv-github-workflows)
- [Part V: How They All Relate](#part-v-how-they-all-relate)
- [Part VI: AI Coding Harnesses](#part-vi-ai-coding-harnesses)
  - [Claude Code](#claude-code)
  - [GitHub Copilot](#github-copilot)
  - [Google Antigravity](#google-antigravity)
  - [Windsurf](#windsurf)
- [Part VII: Trunk-Based Development with Coding Agent Swarms](#part-vii-trunk-based-development-with-coding-agent-swarms)
- [Part VIII: The Unified Workflow](#part-viii-the-unified-workflow)
- [Resources & References](#resources--references)

---

## Introduction

Modern software development in 2026 is characterized by a confluence of mature DevOps practices and rapidly maturing AI coding tools. This guide provides a comprehensive reference for developers and teams looking to understand and combine:

- **Git** — Distributed version control
- **Git Worktrees** — Multiple parallel working directories
- **GitHub Actions** — CI/CD automation platform
- **GitHub Workflows** — Specific automation pipelines
- **AI Coding Harnesses** — Claude Code, GitHub Copilot, Google Antigravity, Windsurf
- **Trunk-Based Development** — A branching strategy optimized for continuous delivery
- **Agent Swarms** — Multiple AI agents working in parallel

Together, these tools enable a development workflow where humans operate as orchestrators directing teams of AI agents, with all work continuously integrated into a stable trunk through robust automation.

---

## Part I: Git Fundamentals & Best Practices

### Getting Started with Git

#### Installation

```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt update && sudo apt install git

# Windows
# Download from https://git-scm.com/download/win
```

#### Initial Configuration

Set up Git with your identity and preferences:

```bash
# Identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Editor
git config --global core.editor "code --wait"  # VS Code

# Default branch name
git config --global init.defaultBranch main

# Pull strategy (rebase by default)
git config --global pull.rebase true

# Auto-prune deleted remote branches
git config --global fetch.prune true

# Use simple push (current branch only)
git config --global push.default simple

# Better diffs
git config --global diff.algorithm histogram

# Cache credentials
git config --global credential.helper cache
```

#### Useful Aliases

Add these to your `~/.gitconfig`:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    ds = diff --staged
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    amend = commit --amend --no-edit
    undo = reset HEAD~1 --soft
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = !gitk
    cleanup = !git branch --merged | grep -v '\\*\\|main\\|master\\|develop' | xargs -n 1 git branch -d
```

### Git Best Practices

#### Commit Message Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/) for consistent, machine-readable messages:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**

| Type | Purpose |
|------|---------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `style:` | Formatting, missing semicolons, etc. |
| `refactor:` | Code change that neither fixes a bug nor adds a feature |
| `perf:` | Performance improvements |
| `test:` | Adding or fixing tests |
| `chore:` | Build process or auxiliary tool changes |
| `ci:` | CI configuration changes |

**Best practices for commit messages:**

- Subject line under 50 characters
- Use imperative mood ("Add feature" not "Added feature")
- Separate subject from body with a blank line
- Body explains the _why_, not the _what_ — the diff shows what changed
- Wrap body at 72 characters
- Reference issues — `Closes #123`, `Fixes #456`, `Refs #789`

**Example of a great commit message:**

```
fix(payments): retry Stripe webhook on 5xx response

Stripe occasionally returns 503 during high traffic. Without retry
logic, failed webhooks cause orders to remain in "pending" state
indefinitely.

Added exponential backoff with 3 retries max.

Fixes #891
```

#### Branching Strategies

Choose based on your team and release cadence:

**1. Trunk-Based Development (Recommended for most teams)**

- Single `main` branch (`main` or `trunk`)
- Short-lived feature branches (hours to 1-2 days max)
- Direct commits to main for small teams (< 15 developers)
- Feature flags for incomplete features
- Used by Google, Meta, Amazon, Netflix
- Best for: Continuous deployment, high-velocity teams, AI-augmented development

**2. GitHub Flow**

- Single `main` branch
- Feature branches per change
- Pull request reviews
- Deploy after merge
- Best for: Small to medium teams, web applications

**3. GitFlow**

- Multiple long-lived branches: `main`, `develop`, `feature/*`, `release/*`, `hotfix/*`
- Formal release processes
- Best for: Versioned software, scheduled releases, multiple production versions

**4. GitLab Flow**

- Combines GitHub Flow with environment branches (`staging`, `production`)
- Best for: Teams needing environment-specific deployments

#### Branch Naming Conventions

Use descriptive prefixes:

```
feature/user-authentication
feature/PROJ-123-payment-integration
bugfix/login-timeout
hotfix/critical-security-patch
release/v2.1.0
experiment/new-caching-strategy
chore/update-dependencies
```

#### Atomic Commits

Each commit should represent one logical change.

**Good:**

- One commit: "Add user authentication endpoint"
- Another commit: "Update API documentation for auth endpoint"

**Bad:**

- One commit: "Add auth endpoint, fix typo in README, update CI config, and refactor utils"

**Benefits:**

- Easier code reviews
- Cleaner reverts
- Better debugging via `git bisect`
- Clearer history

#### Pull Request Best Practices

- Keep PRs small — under 400 lines changed is the target
- Single responsibility — one PR = one logical change
- Write descriptive PR titles — same conventions as commits
- Include context in description — why this change? what does it do? how to test?
- Reference issues — link related work
- Add screenshots/recordings for UI changes
- Self-review first — catch obvious issues before reviewers see them
- Use draft PRs for work-in-progress visibility
- Respond to feedback promptly — don't let PRs stagnate

**PR template example** (`.github/pull_request_template.md`):

```markdown
## Description
Brief explanation of what this PR does and why.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings introduced

Fixes #issue_number
```

#### Daily Git Workflow Tips

```bash
# Start your day
git checkout main
git pull origin main
git checkout -b feature/your-task

# Work and commit frequently
git add .
git commit -m "feat(scope): clear description"

# Stay synced with main
git fetch origin
git rebase origin/main

# Push regularly
git push origin feature/your-task

# Before merging, clean up history
git rebase -i HEAD~3  # Squash WIP commits

# After merge, clean up
git checkout main
git pull
git branch -d feature/your-task
```

#### Handling Mistakes

```bash
# Undo last commit (keep changes staged)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Amend last commit message
git commit --amend

# Add forgotten files to last commit
git add forgotten-file
git commit --amend --no-edit

# Revert a pushed commit (safe for shared branches)
git revert <commit-hash>

# Recover deleted commits
git reflog
git checkout <commit-hash>
```

---

## Part II: Git Worktrees Deep Dive

### What Are Git Worktrees?

A Git worktree is a linked working directory attached to your repository. While a normal Git repo has one working tree, you can attach multiple worktrees — each with a different branch checked out — all sharing the same `.git` history.

> **Key insight:** Worktrees give you multiple working directories without duplicating your entire repository.

### Why Worktrees Matter (Especially for AI Agents)

Traditional Git workflows force serial work:

- Switch branches = lose your current state
- Stash and restore = error-prone
- Multiple clones = wasted disk space, complex syncing

With worktrees, you get true parallel development. This becomes essential when running multiple AI coding agents simultaneously — each agent gets its own isolated working directory, preventing file conflicts.

### Core Commands

#### Creating Worktrees

```bash
# Create worktree with new branch
git worktree add ../feature-x

# Create worktree with new branch name
git worktree add -b feature-auth ../auth-work main

# Create worktree from existing branch
git worktree add ../bugfix bug-fix-123

# Create detached HEAD worktree (for testing)
git worktree add --detach ../test-v1 v1.0.0

# Create worktree without checkout (for sparse checkout)
git worktree add --no-checkout ../sparse
```

#### Managing Worktrees

```bash
# List all worktrees
git worktree list
git worktree list --verbose
git worktree list --porcelain  # Machine-readable

# Lock worktree (prevent cleanup)
git worktree lock --reason "long-running test" ../test

# Unlock worktree
git worktree unlock ../test

# Move worktree
git worktree move ../old-path ../new-path

# Remove worktree (clean way)
git worktree remove ../feature-x

# Force remove (if dirty)
git worktree remove -f ../feature-x

# Clean up missing worktrees
git worktree prune

# Repair broken connections
git worktree repair
```

### Recommended Directory Structure

```
~/projects/
├── myapp/                          # Main worktree (main branch)
├── myapp-feature-auth/             # Worktree on feature/auth
├── myapp-feature-payments/         # Worktree on feature/payments
├── myapp-bugfix-login/             # Worktree on bugfix/login
└── myapp-review-pr-123/            # Worktree for code review
```

Or organized in a parent directory:

```
~/projects/myapp-worktrees/
├── main/                           # Main branch
├── feature-auth/
├── feature-payments/
└── bugfix-login/
```

### Worktree Best Practices

- Use descriptive paths — match worktree directory to branch name
- Keep 2-5 active worktrees max — more creates context-switching overhead
- Always use `git worktree remove` — don't manually delete directories
- Run `git worktree prune` periodically — cleans up stale metadata
- Lock long-running worktrees — prevents accidental cleanup
- Don't checkout the same branch in multiple worktrees — Git will prevent this

Configure worktree-specific settings when needed:

```bash
git config extensions.worktreeConfig true
git config --worktree core.sparseCheckout true
```

### Common Worktree Workflows

#### Emergency Hotfix While Working on Feature

```bash
# Currently working on feature/big-refactor
# Critical bug needs immediate attention

# Create hotfix worktree from main
git worktree add -b hotfix/crash ../hotfix main

cd ../hotfix
# Fix the bug
git commit -am "fix: resolve null pointer in checkout"
git push origin hotfix/crash
# Merge via PR

# Return to original work, undisturbed
cd -

# Cleanup
git worktree remove ../hotfix
```

#### Code Review in Isolation

```bash
# Review PR #456 without disrupting current work
git worktree add -b review/pr-456 ../review origin/feature-branch

cd ../review
# Run tests, inspect code
npm test
npm run dev  # On a different port if needed

# Done with review
cd -
git worktree remove ../review
```

#### Parallel AI Agent Development

```bash
# Set up multiple worktrees for different AI agents
git worktree add -b agent/auth ../agent-auth main
git worktree add -b agent/api ../agent-api main
git worktree add -b agent/tests ../agent-tests main

# Launch Claude Code in each worktree
cd ../agent-auth && claude &
cd ../agent-api && claude &
cd ../agent-tests && claude &

# Each agent works in isolation, no file conflicts
```

---

## Part III: GitHub Actions

### What Are GitHub Actions?

GitHub Actions is GitHub's built-in CI/CD platform that lets you automate your software workflows directly from your repository. You can build, test, and deploy code based on events like pushes, pull requests, issues, or schedules.

### Core Concepts

| Concept | Description |
|---------|-------------|
| Workflow | An automated process defined in a YAML file in `.github/workflows/` |
| Event | An activity that triggers a workflow (push, PR, schedule, etc.) |
| Job | A set of steps that execute on the same runner |
| Step | An individual task within a job (action or shell command) |
| Action | A reusable unit of code that can be combined into workflows |
| Runner | A server (GitHub-hosted or self-hosted) that runs your workflows |

### Getting Started: Your First Workflow

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build
```

### Common Triggers

```yaml
on:
  # Push to specific branches
  push:
    branches: [main, develop]
    paths:
      - 'src/**'
      - 'package.json'

  # Pull requests
  pull_request:
    branches: [main]
    types: [opened, synchronize, reopened]

  # Scheduled (cron)
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC
    # New in 2026: timezone support
    timezone: "America/New_York"

  # Manual trigger
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        default: 'staging'
        type: choice
        options: [staging, production]

  # Other workflows trigger this one
  workflow_call:

  # External events
  repository_dispatch:
    types: [deploy-trigger]
```

### GitHub Actions Best Practices (2026)

#### 1. Security First

Pin actions to commit SHAs (not tags):

```yaml
# Risky - tags are mutable
uses: actions/checkout@v4

# Secure - immutable commit SHA
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11  # v4.1.1
```

Apply least privilege to permissions:

```yaml
# Set restrictive defaults at workflow level
permissions:
  contents: read

jobs:
  deploy:
    # Override per-job when needed
    permissions:
      contents: read
      packages: write
      id-token: write  # For OIDC
```

Use OIDC for cloud authentication (no long-lived secrets):

```yaml
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::123456789012:role/MyRole
    aws-region: us-east-1
    # No AWS keys needed!
```

#### 2. Performance Optimization

Use caching aggressively:

```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

Run jobs in parallel:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: [...]

  test:
    runs-on: ubuntu-latest
    steps: [...]

  build:
    runs-on: ubuntu-latest
    needs: [lint, test]  # Only after lint and test pass
    steps: [...]
```

Use matrix builds for multiple configurations:

```yaml
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node: [18, 20, 22]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

#### 3. Reliability

Always set timeouts:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 30  # Default is 6 hours - too long
```

Use concurrency to prevent race conditions:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ startsWith(github.ref, 'refs/pull/') }}
```

Handle failures gracefully:

```yaml
- name: Run tests
  id: tests
  run: npm test
  continue-on-error: false

- name: Notify on failure
  if: failure()
  run: ./scripts/notify-team.sh
```

#### 4. Maintainability

Use reusable workflows:

```yaml
# .github/workflows/reusable-deploy.yml
name: Reusable Deploy
on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      DEPLOY_TOKEN:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ./deploy.sh ${{ inputs.environment }}
        env:
          TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to Staging
on:
  push:
    branches: [main]

jobs:
  deploy:
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: staging
    secrets:
      DEPLOY_TOKEN: ${{ secrets.STAGING_TOKEN }}
```

Composite actions for repeated steps:

```yaml
# .github/actions/setup-app/action.yml
name: Setup Application
description: Common setup steps

runs:
  using: composite
  steps:
    - uses: actions/setup-node@v4
      with:
        node-version: '20'
        cache: 'npm'

    - run: npm ci
      shell: bash
```

#### 5. Secrets Management

```yaml
# Repository secrets
${{ secrets.API_KEY }}

# Environment-specific secrets
environment:
  name: production
${{ secrets.PROD_API_KEY }}

# Mask custom values in logs
- run: echo "::add-mask::$SECRET_VALUE"
```

**Best practices:**

- Never log secrets (use `::add-mask::` if needed)
- Audit secret usage regularly
- Rotate secrets periodically
- Use environments for production secrets with required reviewers

### Common Workflow Patterns

#### Continuous Integration

```yaml
name: CI
on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  ci:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v4
```

#### Auto-Deploy on Merge

```yaml
name: Deploy
on:
  push:
    branches: [main]

permissions:
  contents: read
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: us-east-1
      - run: ./deploy.sh
```

#### PR Auto-Labeling

```yaml
name: PR Labels
on:
  pull_request:
    types: [opened, edited]

permissions:
  pull-requests: write
  contents: read

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
```

---

## Part IV: GitHub Workflows

### Workflows vs. Actions: Clarifying Terminology

- **GitHub Actions** is the platform/feature
- A **workflow** is a specific YAML file defining an automated process
- An **action** is a reusable unit of code (like a function call within a workflow)

So when people say "GitHub Workflows," they typically mean the individual YAML files that orchestrate jobs and steps using GitHub Actions.

### Workflow File Structure

```yaml
# Workflow metadata
name: My Workflow
run-name: ${{ github.actor }} is running ${{ github.workflow }}

# Triggers
on:
  push:
    branches: [main]

# Workflow-level configuration
permissions:
  contents: read

defaults:
  run:
    shell: bash
    working-directory: ./app

env:
  GLOBAL_VAR: "value"

# Concurrency control
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

# Jobs
jobs:
  job-id:
    name: Display Name
    runs-on: ubuntu-latest
    timeout-minutes: 30

    permissions:
      packages: write

    env:
      JOB_VAR: "value"

    if: github.event_name == 'push'
    needs: [other-job]

    strategy:
      matrix:
        version: [18, 20]

    outputs:
      result: ${{ steps.step-id.outputs.value }}

    steps:
      - name: Step name
        id: step-id
        if: matrix.version == 20
        uses: actions/checkout@v4
        with:
          ref: main
        env:
          STEP_VAR: "value"
```

### Workflow Categories & Examples

#### 1. Build & Test Workflows

Multi-language test matrix:

```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python: ['3.10', '3.11', '3.12']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python }}
          cache: 'pip'
      - run: pip install -e ".[test]"
      - run: pytest
```

#### 2. Security Workflows

Dependency scanning:

```yaml
name: Security Scan
on:
  schedule:
    - cron: '0 0 * * 1'  # Weekly on Monday
  push:
    branches: [main]

permissions:
  contents: read
  security-events: write

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@b4ffde65f46336ab88eb53be808477a3936bae11
        with:
          scan-type: 'fs'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload to GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'
```

CodeQL analysis:

```yaml
name: CodeQL
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  security-events: write
  contents: read

jobs:
  analyze:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        language: ['javascript', 'python']
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}
      - uses: github/codeql-action/autobuild@v3
      - uses: github/codeql-action/analyze@v3
```

#### 3. Release Workflows

Automated semantic releases:

```yaml
name: Release
on:
  push:
    branches: [main]

permissions:
  contents: write
  packages: write
  pull-requests: write

jobs:
  release:
    runs-on: ubuntu-latest
    if: "!contains(github.event.head_commit.message, 'chore(release)')"
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - run: npm ci
      - run: npx semantic-release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

#### 4. Deployment Workflows

Multi-environment deployment with approvals:

```yaml
name: Deploy
on:
  push:
    branches: [main]

permissions:
  contents: read
  id-token: write
  deployments: write

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.build.outputs.tag }}
    steps:
      - uses: actions/checkout@v4
      - id: build
        run: |
          TAG="$(git rev-parse --short HEAD)"
          docker build -t myapp:$TAG .
          echo "tag=$TAG" >> $GITHUB_OUTPUT

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - run: ./deploy.sh staging ${{ needs.build.outputs.image-tag }}

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production  # Requires manual approval
      url: https://example.com
    steps:
      - run: ./deploy.sh production ${{ needs.build.outputs.image-tag }}
```

#### 5. AI-Augmented Workflows (2026)

AI code review on PRs:

```yaml
name: AI Review
on:
  pull_request:
    types: [opened, synchronize]

permissions:
  contents: read
  pull-requests: write

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run AI Review
        uses: anthropic/claude-review-action@v1
        with:
          api-key: ${{ secrets.ANTHROPIC_API_KEY }}
          focus: 'security,performance,readability'
```

Auto-fix linting with AI:

```yaml
name: AI Lint Fix
on:
  pull_request:

jobs:
  fix:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run lint --fix || true
      - uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "style: auto-fix linting issues"
```

### Workflow Optimization Checklist

- [ ] Triggers are appropriate (path filters, branch filters)
- [ ] `timeout-minutes` set to reasonable value (15-30 typically)
- [ ] `concurrency` configured for shared resources
- [ ] `permissions` set with least privilege
- [ ] Actions pinned to commit SHAs
- [ ] Caching configured for dependencies
- [ ] Jobs run in parallel where possible
- [ ] Matrix builds used for multi-config testing
- [ ] Secrets accessed via environments where appropriate
- [ ] Reusable workflows for common patterns
- [ ] OIDC used instead of long-lived cloud secrets
- [ ] Failed runs send notifications
- [ ] Logs don't leak sensitive data

---

## Part V: How They All Relate

Understanding how Git, Git Worktrees, GitHub Actions, and GitHub Workflows fit together is crucial for an effective workflow.

### The Conceptual Hierarchy

```
GitHub (Hosting Platform)
├── Repository (Your Code Storage)
│   ├── Git (Local Version Control)
│   │   ├── Branches (Lines of Development)
│   │   └── Worktrees (Multiple Working Directories)
│   │
│   └── GitHub Actions (Automation Platform)
│       ├── Workflows (.github/workflows/*.yml)
│       │   ├── Jobs (Parallel Units of Work)
│       │   │   └── Steps (Sequential Tasks)
│       │   │       └── Actions (Reusable Units)
│       │   └── Events (Triggers)
│       └── Runners (Execution Environment)
```

### The Information Flow

```
Developer Makes Changes
        ↓
Git (Local Commits)
        ↓
Push to GitHub Repository
        ↓
GitHub Actions Triggered (push, PR events)
        ↓
Workflows Execute (CI: lint, test, build)
        ↓
Pull Request Reviewed
        ↓
Workflow Passes → Merge to Main
        ↓
Deployment Workflow Triggers
        ↓
Production Deployment
```

### How Worktrees Fit In

Worktrees operate at the Git layer but interact with everything else:

```
Single Repository (.git)
        ↓
        ├── Main Worktree (main branch) → Push triggers CI workflow
        ├── Feature Worktree A → Push triggers CI workflow on feature branch
        ├── Feature Worktree B → Push triggers CI workflow on feature branch
        └── Review Worktree → Local testing of incoming PRs
```

Each worktree can independently push to GitHub, triggering its own workflow runs. This is what makes worktrees so powerful for parallel AI agent development — each agent's worktree triggers its own CI runs.

### Practical Integration Example

```bash
# Morning: Sync with team
cd ~/projects/myapp/main
git pull origin main

# Set up parallel work on three features
git worktree add -b feature/auth ../auth main
git worktree add -b feature/api ../api main
git worktree add -b feature/ui ../ui main

# Work on each feature (or assign to AI agents)
cd ../auth
git commit -am "feat(auth): add OAuth flow"
git push origin feature/auth
# → GitHub Actions runs CI workflow
# → Tests run, linting passes
# → PR auto-created (via GitHub CLI or workflow)

# Switch to API work (no context loss)
cd ../api
git commit -am "feat(api): add user endpoints"
git push origin feature/api
# → CI runs in parallel with the auth PR

# Code review another developer's PR
git worktree add -b review/pr-789 ../review origin/their-branch
cd ../review
npm test
# Approve or request changes via GitHub UI

# After PRs are merged, cleanup
cd ../auth && git worktree remove .
cd ../api && git worktree remove .
cd ../review && git worktree remove .
```

---

## Part VI: AI Coding Harnesses

AI coding harnesses transform how developers work with code. Each tool has different strengths, philosophies, and integration models.

### Common Concepts Across All Harnesses

| Concept | Description |
|---------|-------------|
| Agent Mode | AI autonomously plans and executes multi-step tasks |
| Context | Information the AI uses (codebase, docs, conversations) |
| Tool Use | AI's ability to read/write files, run commands, browse |
| MCP | Model Context Protocol — standard for connecting AI to tools |
| Memory/Rules | Persistent instructions that customize AI behavior |
| Multi-Agent | Multiple AI instances working in parallel |

---

### Claude Code

#### What It Is

Claude Code is Anthropic's terminal-native AI coding agent that lives in your shell. Built around Claude (currently Opus 4.7), it's designed for developers who want maximum control with minimal IDE lock-in.

#### Key Features

- **Terminal-first** — Runs in any shell on macOS, Linux, Windows
- **CLAUDE.md** — Project memory file that loads at every session
- **Skills system** — Reusable workflow templates
- **Subagents** — Spawn isolated agents for parallel work
- **MCP support** — Connect to external tools/services
- **Hooks** — Run custom scripts on events (pre-commit, etc.)
- **Native worktree support** — `claude -w feature-name`

#### Getting Started

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Authenticate
claude auth login

# Initialize a project
cd my-project
claude /init  # Creates CLAUDE.md based on codebase analysis

# Start a session
claude

# Or run autonomously
claude -p "Add input validation to the signup form"
```

#### CLAUDE.md Structure

```markdown
# Project: MyApp

## Overview
SaaS platform for project management built with Next.js 14 (App Router),
TypeScript, Tailwind CSS, PostgreSQL with Prisma, and tRPC.

## Architecture
- `/app` - Next.js App Router pages
- `/components` - Reusable React components
- `/lib` - Utility functions and shared logic
- `/server` - tRPC routers and database logic
- `/prisma` - Database schema and migrations

## Conventions
- Use TypeScript strict mode
- Prefer named exports over default exports
- Use Tailwind utility classes (no custom CSS unless necessary)
- API routes use tRPC, not REST
- Database access only through Prisma client in `/server/db.ts`

## Commands
- `npm run dev` - Start dev server
- `npm run test` - Run Vitest tests
- `npm run lint` - Run ESLint
- `npm run typecheck` - Type check without emitting
- `npm run db:migrate` - Run Prisma migrations

## Testing
- Unit tests: Vitest in `*.test.ts` files
- E2E tests: Playwright in `/e2e`
- Aim for 80%+ coverage on business logic
- Mock external services with MSW

## Code Review Standards
- All PRs must pass CI
- Two approvals required for production code
- No direct pushes to main
- Conventional commit messages required
```

#### Claude Code Best Practices

**1. Plan before implementing:**

```
> Plan a refactor of the auth system to use OAuth.
> Don't write code yet — just give me a step-by-step plan.
```

**2. Use subagents for parallel work:**

```
> Use a subagent to research how other Next.js apps handle OAuth,
> while you start drafting the implementation plan.
```

**3. Create slash commands for repeated workflows** (`.claude/commands/test-and-fix.md`):

```
Run the test suite. If any tests fail:
1. Identify the failure
2. Determine if it's a real bug or a test issue
3. Fix accordingly
4. Re-run tests until all pass
```

**4. Use git worktrees for parallel agents:**

```bash
# Terminal 1
claude -w feature-auth

# Terminal 2
claude -w feature-payments

# Terminal 3
claude -w bugfix-login
```

**5. Manage context aggressively:**

| Context % | Action |
|-----------|--------|
| 0-50% | Work freely |
| 50-70% | Be aware |
| 70-90% | Use `/compact` to summarize |
| 90%+ | Use `/clear` and restart |

#### Claude Code with GitHub Actions

```yaml
name: Claude AI Tasks
on:
  issue_comment:
    types: [created]

jobs:
  claude:
    if: contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          api-key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: ${{ github.event.comment.body }}
```

---

### GitHub Copilot

#### What It Is

GitHub Copilot is GitHub's AI coding assistant, deeply integrated with VS Code, JetBrains IDEs, and the GitHub platform itself. In 2026, it has evolved from autocomplete into a full agentic platform.

#### Tiers of Capability

| Mode | Description |
|------|-------------|
| Code Completion | Inline suggestions (Tab to accept) |
| Next Edit Suggestions | Predicts where your next edit will be |
| Copilot Chat | Q&A about your code |
| Edit Mode | Multi-file edits with natural language |
| Agent Mode | Autonomous multi-step task execution |
| Cloud Agent | Asynchronous PR creation from GitHub Issues |

#### Key Features (2026)

- **Multi-model support** — GPT, Claude, Gemini available
- **Custom agents** — Specialized agents with tools/skills
- **Agentic memory** — Persistent repository knowledge
- **Skills system** — Folders of instructions and resources
- **MCP integration** — External tools via Model Context Protocol
- **Coding agent** — Assigned to GitHub Issues, creates PRs automatically
- **Code review agent** — AI-powered PR reviews

#### Getting Started

```bash
# Install in VS Code
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat

# Or install GitHub CLI
gh extension install github/gh-copilot

# CLI usage
gh copilot suggest "create a docker compose for postgres and redis"
gh copilot explain "git rebase -i HEAD~3"
```

#### Activating Agent Mode

In VS Code:

1. Open Chat panel: `Ctrl+Alt+I` / `⌃⌘I`
2. Click mode dropdown at top of chat
3. Select **Agent**
4. Type instruction:

```
Add input validation to the signup form in src/components/SignupForm.tsx.
Validate email format, password strength (min 8 chars, one number, one
special char), and show inline error messages. Run the existing tests
after making changes.
```

#### Cloud Agent (Async PRs)

```bash
# Via GitHub CLI
gh issue edit 123 --add-assignee @copilot

# Or in GitHub UI: Open issue → Assignees → Copilot
```

Copilot will read the issue, analyze the codebase, create a branch, make the changes, run tests, create a PR, and notify you when ready.

#### Customization Files

`.github/copilot-instructions.md` — Workspace-wide instructions:

```markdown
# Repository Instructions

## Project Type
Full-stack web application

## Tech Stack
- Frontend: Next.js 14, TypeScript, Tailwind CSS
- Backend: Node.js, Express, PostgreSQL
- Testing: Jest, Playwright

## Coding Standards
- Use functional components with hooks (no class components)
- Prefer composition over inheritance
- Always handle errors explicitly
- Write JSDoc comments for public APIs

## Pull Request Conventions
- Title format: `type(scope): description`
- Reference issue numbers
- Include screenshots for UI changes
```

`.github/prompts/api-endpoint.md` — Reusable prompt:

```markdown
Create a new API endpoint following our REST conventions:
1. Add route handler in `/api/routes/`
2. Add validation schema with Zod
3. Add unit tests
4. Update OpenAPI docs
```

#### GitHub Copilot Best Practices

- Provide specific context — reference exact files and patterns
- Use repository instructions — set up `.github/copilot-instructions.md`
- Review the plan first — have agent show plan before executing
- Monitor premium request usage — agent mode burns through them quickly
- Combine with Copilot CLI — use `gh copilot` for terminal tasks
- Use Cloud Agent for backlogs — assign repetitive issues for async completion

---

### Google Antigravity

#### What It Is

Google Antigravity is Google's "agent-first" IDE launched November 2025 alongside Gemini 3. It's built on a heavily modified VS Code fork and distinguishes itself with the **Manager View** — a mission control for orchestrating multiple AI agents in parallel.

#### Key Features

- **Two views:**
  - Editor View — familiar IDE experience
  - Manager View — multi-agent orchestration dashboard
- **Multi-model support** — Gemini 3 Pro, Claude Sonnet/Opus 4.6, GPT-OSS
- **Browser-in-the-loop** — Agents can launch Chrome to test UIs
- **Artifacts** — Verifiable deliverables (plans, screenshots, walkthroughs)
- **Agent learning** — Improves understanding over time
- **Verification workflows** — Built-in quality checks

#### Getting Started

```
# Download from antigravity.google
# Available for macOS, Windows, Linux

# After install:
File → Open Folder → Select your project
```

#### Editor View vs. Manager View

**Editor View:**

- Tab autocomplete
- Natural language commands
- Embedded chat agent
- All VS Code extensions work

**Manager View:**

- Mission control dashboard
- Spawn multiple agents
- Each agent works in parallel
- View artifacts (plans, screenshots, results)
- Approve/reject changes

#### Permissions Model

Configure in Settings:

```yaml
Agent:
  Artifact Review Policy: "Asks for Review"
  Terminal Command Auto Execution: "Request Review"
  Enable Terminal Sandbox: true
  Non-Workspace File Access: false
```

Three permission lists:

- **Allow** — Auto-approved actions
- **Deny** — Blocked immediately
- **Ask** — Requires review

#### Multi-Agent Workflow

In Manager View, dispatch agents in parallel:

```
Agent 1: "Refactor authentication module to use OAuth"
Agent 2: "Add input validation to all forms in /src/components"
Agent 3: "Write E2E tests for the checkout flow"
Agent 4: "Update API documentation"
Agent 5: "Optimize database queries in /server/queries"
```

Each agent plans the task, executes across editor/terminal/browser, generates artifacts, and reports back for review.

#### Google Antigravity Best Practices

- Start with restrictive permissions — loosen as trust builds
- Review artifacts thoroughly — don't blindly approve
- Use browser subagents for UI verification — they take screenshots
- Leverage parallel execution — don't run agents sequentially
- Maintain a knowledge base — help agents learn your patterns

---

### Windsurf

#### What It Is

Windsurf (formerly Codeium, now owned by Cognition AI) is an AI-powered IDE built on VS Code. Its standout feature is **Cascade**, an agentic AI assistant that maintains deep context awareness of your entire workflow.

#### Key Features

- **Cascade** — Agentic AI with Write/Chat modes
- **Flow Awareness** — Tracks edits, terminal, clipboard, browser
- **Memories** — Persistent context across sessions
- **Rules** — User-defined behavior guidelines
- **Skills System** — Reusable instruction bundles
- **Workflows (Rulebooks)** — Reusable markdown-based workflows
- **MCP Integration** — Connect external services
- **Devin Integration** — Hand off to autonomous cloud agent
- **Browser Integration** — Live preview with click-to-edit
- **Multi-Cascade** — Run parallel sessions with worktrees

#### Cascade Modes

| Mode | Purpose |
|------|---------|
| Write Mode | Take action and make changes — edit files, run commands, generate docs, build tests |
| Chat Mode | Explore and retrieve information — code discovery, Q&A, pattern understanding, no changes made |

#### Getting Started

```bash
# Download from windsurf.com
# Or install JetBrains plugin

# Open Cascade
Cmd/Ctrl+L  # Or click Cascade icon
```

#### Configuration File

`.windsurfrules` in project root:

```markdown
# Windsurf Rules

## Project Overview
Next.js 14 application with App Router, TypeScript, Tailwind CSS.

## Code Style
- Use functional components
- Prefer named exports
- 2-space indentation
- Single quotes for strings (except JSX attributes)

## Architecture
- API routes in `/app/api`
- Components in `/components`
- Utilities in `/lib`
- Database access via Prisma client

## Testing
- Unit tests with Vitest
- E2E tests with Playwright
- Test files: `*.test.ts` colocated with source

## Behavior
- Always run `npm run lint` after changes
- Always run `npm test` before declaring task complete
- Ask before installing new dependencies
- Format with Prettier before committing
```

#### Workflows (Rulebooks)

Create reusable workflows in `.windsurf/workflows/`:

`.windsurf/workflows/new-component.md`:

```markdown
# Create New Component

When user requests a new component:

1. Determine component category (UI, layout, feature)
2. Create file in appropriate directory:
   - UI: `/components/ui/`
   - Layout: `/components/layout/`
   - Feature: `/components/features/`
3. Use this template:
   ```tsx
   import { FC } from 'react'

   interface Props {
     // ...
   }

   export const ComponentName: FC<Props> = ({ ... }) => {
     return (
       <div>
         {/* ... */}
       </div>
     )
   }
   ```
4. Add Storybook story
5. Add unit tests
6. Update component index exports

Invoke with: `/new-component`
```

#### Multi-Cascade with Worktrees

> **Note from Windsurf docs:** "If two Cascades edit the same file at the same time, the edits can race, and sometimes the second edit will fail. If you expect two Cascades to edit similar files, you should consider using worktrees to keep them isolated."

```bash
# Create worktrees for parallel work
git worktree add -b feature-a ../app-a main
git worktree add -b feature-b ../app-b main

# Open each in Windsurf
# Window 1: open ~/projects/app-a
# Window 2: open ~/projects/app-b

# Each Cascade operates independently
```

#### Windsurf Best Practices

- Set up `.windsurfrules` — project-specific guidance
- Build a workflow library — capture repeated patterns as rulebooks
- Use Memories deliberately — auto-generated and user-defined
- Review multi-file edits — Cascade can affect many files at once
- Use Click-to-Edit for UI — faster than describing changes
- Use worktrees for parallel Cascades — avoid file race conditions

---

### Comparing the Four Harnesses

| Feature | Claude Code | GitHub Copilot | Google Antigravity | Windsurf |
|---------|-------------|----------------|-------------------|----------|
| Primary Interface | Terminal | IDE (VS Code, JetBrains) | Custom IDE (VS Code fork) | Custom IDE (VS Code fork) |
| Model | Claude Opus 4.7 | Multi-model (GPT, Claude, Gemini) | Multi-model (Gemini, Claude, GPT-OSS) | Multi-model |
| Multi-Agent | Subagents + worktrees | Cloud Agent + custom agents | Manager View (native) | Multi-Cascade + worktrees |
| Browser Control | Via MCP (Chrome) | Limited | Native | Limited (preview/click-to-edit) |
| GitHub Integration | Via MCP/CLI | Native (deepest) | Via Git | Via Git |
| Persistent Context | CLAUDE.md + skills | copilot-instructions.md + memory | Knowledge base | .windsurfrules + memories |
| Best For | Terminal lovers, max control | GitHub-native teams | Multi-agent orchestration | Flow state, deep context |
| Pricing (2026) | Subscription-based | Free tier; $10-39/mo paid | Free preview | Free tier; paid plans |
| Worktree Support | Native (`-w` flag) | Manual | Manual | Recommended |

---

## Part VII: Trunk-Based Development with Coding Agent Swarms

### Why TBD + Agent Swarms = Powerful

Traditional human teams hit a bottleneck: developers can only do one thing at a time. AI agents don't have this limitation — they can execute at full speed in parallel. But agents need:

- **Isolation** — So they don't conflict with each other (Git worktrees)
- **Frequent integration** — So changes don't diverge (TBD)
- **Continuous validation** — So bad code is caught fast (GitHub Actions)
- **Clear conventions** — So they produce compatible output (`CLAUDE.md`, `.windsurfrules`, `copilot-instructions.md`)
- **Feature flags** — So incomplete work doesn't break production

TBD provides exactly this structure.

### Core Principles of TBD

- **Single trunk branch** — `main` is the source of truth
- **Always deployable** — Trunk is in releasable state at all times
- **Short-lived branches** — Hours to 1-2 days max (or direct commits)
- **Frequent integration** — Daily merges minimum
- **Feature flags** — Hide incomplete features in production
- **Comprehensive automation** — Tests, builds, deployments all automated
- **Branch by abstraction** — Refactor incrementally, not all at once

### Setting Up TBD with Agent Swarms

#### Step 1: Repository Configuration

Branch protection rules for `main`:

```yaml
# .github/settings.yml
branches:
  - name: main
    protection:
      required_pull_request_reviews:
        required_approving_review_count: 1
        dismiss_stale_reviews: true
        require_code_owner_reviews: true
      required_status_checks:
        strict: true
        contexts:
          - "ci/lint"
          - "ci/test"
          - "ci/build"
          - "ci/security-scan"
      enforce_admins: true
      restrictions: null
      allow_force_pushes: false
      allow_deletions: false
```

CODEOWNERS file:

```
# .github/CODEOWNERS
* @team-lead
/src/auth/ @security-team
/api/ @backend-team
/.github/workflows/ @devops-team
```

#### Step 2: Comprehensive CI Pipeline

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    name: ci/lint
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  test:
    name: ci/test
    runs-on: ubuntu-latest
    timeout-minutes: 15
    strategy:
      matrix:
        shard: [1, 2, 3, 4]  # Parallel test shards
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --shard=${{ matrix.shard }}/4

  build:
    name: ci/build
    runs-on: ubuntu-latest
    timeout-minutes: 15
    needs: [lint, test]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run build

  security-scan:
    name: ci/security-scan
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - uses: aquasecurity/trivy-action@b4ffde65f46336ab88eb53be808477a3936bae11
        with:
          scan-type: 'fs'
```

#### Step 3: Feature Flags Setup

Use a feature flag library (Unleash, LaunchDarkly, ConfigCat, OpenFeature):

```typescript
// lib/feature-flags.ts
import { Unleash } from 'unleash-client'

export const flags = new Unleash({
  url: process.env.UNLEASH_URL,
  appName: 'myapp',
  customHeaders: { Authorization: process.env.UNLEASH_TOKEN },
})

// Usage in code
if (flags.isEnabled('new-checkout-flow')) {
  return <NewCheckout />
}
return <OldCheckout />
```

#### Step 4: Agent Coordination Setup

Recommended project structure:

```
my-project/
├── .agents/
│   ├── coordinator.md          # Master coordination doc
│   ├── tasks/                  # Task definitions
│   │   ├── task-001.md
│   │   ├── task-002.md
│   └── completed/              # Archived completed tasks
├── .claude/
│   ├── CLAUDE.md
│   ├── commands/
│   ├── skills/
│   └── agents/
├── .github/
│   ├── workflows/
│   ├── copilot-instructions.md
│   └── prompts/
├── .windsurf/
│   ├── workflows/
│   └── memories/
└── src/
```

Coordinator file (`.agents/coordinator.md`):

```markdown
# Agent Coordination

## Active Tasks
- [ ] Task 001: Refactor auth module (assigned: agent-1, branch: refactor/auth)
- [ ] Task 002: Add user dashboard (assigned: agent-2, branch: feature/dashboard)
- [ ] Task 003: Optimize API queries (assigned: agent-3, branch: perf/api-queries)

## Coordination Rules
- Each task must be in its own worktree
- Each task must be behind a feature flag
- Each task must be merged within 24 hours
- Each task must include tests

## File Ownership
- /src/auth/* — agent-1 (until task 001 complete)
- /src/dashboard/* — agent-2 (until task 002 complete)
- /server/queries/* — agent-3 (until task 003 complete)

## Forbidden Cross-Task Modifications
- Agents must NOT modify files outside their assigned area
- Shared utilities must be updated via separate, coordinated PRs
- Database migrations require human approval
```

#### Step 5: Spinning Up an Agent Swarm

```bash
#!/bin/bash
# scripts/spawn-agents.sh

# Clean up any old worktrees
git worktree prune

# Pull latest main
git checkout main
git pull origin main

# Define tasks
declare -A TASKS=(
  ["agent-auth"]="refactor/auth-module"
  ["agent-dashboard"]="feature/user-dashboard"
  ["agent-api"]="perf/api-optimization"
  ["agent-tests"]="test/improve-coverage"
)

# Create worktrees for each task
for AGENT in "${!TASKS[@]}"; do
  BRANCH="${TASKS[$AGENT]}"
  WORKTREE="../$(basename $(pwd))-$AGENT"

  echo "Setting up worktree for $AGENT on branch $BRANCH"
  git worktree add -b "$BRANCH" "$WORKTREE" main
done

# Print status
echo ""
echo "All worktrees created:"
git worktree list

echo ""
echo "Now launch agents:"
echo "  Terminal 1: cd ../$(basename $(pwd))-agent-auth && claude"
echo "  Terminal 2: cd ../$(basename $(pwd))-agent-dashboard && claude"
echo "  Terminal 3: cd ../$(basename $(pwd))-agent-api && claude"
echo "  Terminal 4: cd ../$(basename $(pwd))-agent-tests && claude"
```

#### Step 6: Tooling for Agent Swarms

**Claude Squad** (open source, 6.8k+ stars):

- Go-based TUI
- Manages multiple agents with isolated worktrees
- Works with Claude Code, Codex, Aider, Gemini

```bash
# Install
go install github.com/smtg-ai/claude-squad@latest

# Launch
cs
```

**ccswarm:**

- Multi-agent orchestration framework
- Specialized agents (frontend, backend, testing)
- Template-based scaffolding

**Parallel Code:**

- Cross-tool agent management
- Works with Claude Code, Codex, Gemini CLI, Copilot CLI
- QR code mobile monitoring

#### Step 7: Daily TBD + Agent Workflow

```bash
# === MORNING (10 min) ===
git checkout main
git pull origin main
gh pr list --state open

# === SPAWN AGENT SWARM (5 min) ===
./scripts/spawn-agents.sh

# === ORCHESTRATION (throughout day) ===
git worktree list
gh pr list

# When merging an agent's work:
gh pr merge 123 --squash --delete-branch
git worktree remove ../myapp-agent-auth
git worktree prune

# === REBASE OTHER AGENTS (every few hours) ===
for WORKTREE in ../myapp-agent-*; do
  cd "$WORKTREE"
  git fetch origin
  git rebase origin/main
  cd -
done

# === END OF DAY ===
# All branches should be merged or cleaned up
# Trunk should be deployable
```

### Critical Rules for AI Agent TBD

1. Every agent works in its own worktree — no exceptions
2. Every change goes behind a feature flag — if not user-visible
3. Every PR must merge within 24 hours — or be split smaller
4. Every task has a clear scope — one agent, one purpose
5. No agent modifies shared utilities without coordination — prevent conflicts
6. All work goes through CI — including agent-generated code
7. Human review remains essential — treat agents as junior developers
8. Agents commit frequently — small, atomic commits
9. Tests are non-negotiable — generated code includes tests
10. Main is always green — failing CI blocks all merges

### Common Anti-Patterns to Avoid

| Anti-Pattern | Solution |
|-------------|----------|
| Agent free-for-all — letting agents modify any file | Scoped responsibilities — each agent owns specific paths/modules |
| Long-lived agent branches — agents working for days | Hourly progress — frequent commits, frequent merges |
| No human review — auto-merging agent PRs | Human-in-the-loop — review every agent change before merge |
| Agents modifying CI/CD — opens security holes | CI/CD changes require human authorship |
| No isolation — multiple agents in same directory | Worktree per agent — always |
| Ignoring feature flags — releasing incomplete features | Flag everything — behind flags by default |

---

## Part VIII: The Unified Workflow

### The Tech Stack

| Layer | Tool |
|-------|------|
| VCS | Git |
| Hosting | GitHub |
| CI/CD | GitHub Actions |
| Branching | Trunk-based development |
| Parallelization | Git worktrees |
| AI Agents | Mix of Claude Code, GitHub Copilot, Google Antigravity, Windsurf |
| Coordination | Custom `.agents/` directory + tools like Claude Squad |
| Feature Flags | OpenFeature-compatible service (Unleash, LaunchDarkly) |
| Testing | Comprehensive automated tests at all levels |

### A Day in the Life

**8:30 AM — Morning Sync**

```bash
cd ~/work/myapp
git checkout main
git pull origin main
gh pr list  # Check overnight async work from cloud agents
```

**8:45 AM — Plan Today's Work**

```bash
gh issue list --label ready
# Decide on 4-5 tasks for today
```

**9:00 AM — Spawn Agent Swarm**

```bash
# Use Claude Squad or custom script
cs

# Tasks dispatched:
# - agent-1: "Refactor session management" (Claude Code in worktree-1)
# - agent-2: "Add CSV export to dashboard" (Windsurf in worktree-2)
# - agent-3: "Write tests for payment module" (GitHub Copilot Agent in worktree-3)
# - cloud-agent: "Update API docs" (Copilot Cloud Agent on Issue #234)
```

**9:30 AM — Personal Coding**

```bash
cd ~/work/myapp/main
git checkout -b refactor/database-layer
# Use Copilot/Cascade for inline help
```

**11:00 AM — First Review Cycle**

```bash
gh pr view 456
git worktree add -b review/auth ../myapp-review origin/refactor/session-management
cd ../myapp-review
npm test
npm run dev

gh pr merge 456 --squash --delete-branch
cd - && git worktree remove ../myapp-review
git checkout main && git pull
```

**11:30 AM — Rebase Active Agents**

```bash
for WT in ../myapp-agent-*; do
  cd "$WT"
  git fetch origin
  git rebase origin/main
  cd -
done
```

**1:30 PM — Review Cycle 2**

```bash
gh pr review 457 --approve --body "Looks good, tests pass"
gh pr merge 457 --squash --delete-branch
```

**3:00 PM — Spawn Second Wave of Agents**

```bash
./scripts/spawn-agents.sh
# New tasks:
# - agent-4: "Optimize image loading" (Antigravity Manager View)
# - agent-5: "Migrate to new ORM version" (Claude Code)
# - agent-6: "Add accessibility audits" (Windsurf)
```

**5:00 PM — End-of-Day Cleanup**

```bash
gh pr list --state open
git worktree remove ../myapp-agent-1
git worktree remove ../myapp-agent-2
git checkout main && git pull
gh run list --branch main --limit 5
```

### Productivity Multipliers

| Multiplier | Source |
|-----------|--------|
| Parallelism | Worktrees + agent swarms = N tasks at once |
| Automation | GitHub Actions handles all rote validation |
| Speed | TBD's small batches = faster feedback loops |
| Safety | Feature flags + comprehensive testing = ship without fear |
| Quality | AI assists with code, humans focus on architecture |
| Async work | Cloud agents work while you sleep |
| Less context switching | Each worktree maintains its own state |

### Metrics That Matter

| Metric | Target |
|--------|--------|
| Lead time for changes (commit → production) | < 1 day |
| Deployment frequency | Multiple times per day |
| Change failure rate | < 15% |
| Mean time to recovery | < 1 hour |
| PR cycle time | < 4 hours |
| Average PR size | < 400 lines |
| Branch lifetime | < 2 days |

---

## Resources & References

### Official Documentation

**Git:**

- [Git Official Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book) — Free, comprehensive
- [git-worktree man page](https://git-scm.com/docs/git-worktree)

**GitHub Actions:**

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Actions Marketplace](https://github.com/marketplace?type=actions)
- [Awesome Actions](https://github.com/sdras/awesome-actions)
- [Security Hardening Guide](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

**Trunk-Based Development:**

- [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com) — Paul Hammant's authoritative site
- [Atlassian's TBD Guide](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)

**AI Coding Harnesses:**

- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [Google Antigravity](https://antigravity.google)
- [Windsurf Docs](https://docs.windsurf.com)

### Community Resources

**Best Practices Repositories:**

- [github/awesome-copilot](https://github.com/github/awesome-copilot)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

**Agent Swarm Tools:**

- [Claude Squad](https://github.com/smtg-ai/claude-squad) — Multi-agent TUI
- ccswarm — Orchestration framework
- Parallel Code — Cross-tool manager

**Feature Flag Services:**

- [Unleash](https://www.getunleash.io) — Open source
- [LaunchDarkly](https://launchdarkly.com) — Enterprise
- [ConfigCat](https://configcat.com) — Developer-friendly
- [OpenFeature](https://openfeature.dev) — Vendor-neutral standard

### Recommended Reading

- *Continuous Delivery* by Jez Humble & David Farley
- *Accelerate* by Nicole Forsgren, Jez Humble, Gene Kim
- *Software Engineering at Google* by Titus Winters et al.
- *The DevOps Handbook* by Gene Kim et al.
- [Trunk-Based Development and Branch by Abstraction](https://trunkbaseddevelopment.com) — Free online
- [Pro Git Book](https://git-scm.com/book) — Available free at git-scm.com/book

---

## Conclusion

The combination of Git, Git worktrees, GitHub Actions, GitHub Workflows, trunk-based development, and AI coding harnesses represents a fundamental shift in how software gets built.

The bottleneck has moved. It used to be typing speed. Then it was thinking speed. Now it's _coordination speed_ — how effectively can you orchestrate parallel work across multiple agents while maintaining quality?

The teams that win in 2026 aren't those with the most powerful AI. They're the ones whose workflows remove friction at every layer:

- **Git** provides the foundation for tracking parallel work
- **Worktrees** enable truly parallel execution without conflicts
- **GitHub Actions** automate all the validation
- **Trunk-based development** keeps everything continuously integrated
- **Feature flags** decouple deployment from release
- **AI harnesses** multiply human productivity

Start small. Pick one improvement. Master it. Then add another. The compound effect over months and years is transformative.

> The future of software development isn't humans vs. AI — it's humans directing AI swarms, with everything continuously integrated through robust automation.

---

*This guide is a living document. As tools evolve and best practices emerge, contribute updates and refinements to your team's version.*

**Last updated:** May 2026 | Based on Git 2.54.0, GitHub Actions 2026, Claude Code, GitHub Copilot, Google Antigravity, Windsurf as of April 2026
