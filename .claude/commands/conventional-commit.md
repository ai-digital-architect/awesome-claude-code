# Conventional Commit Message Generator

Generate standardized commit messages following the Conventional Commits specification.

## Purpose
Create clear, consistent commit messages that:
- Follow semantic versioning principles
- Enable automated changelog generation
- Improve git history readability
- Support automated CI/CD workflows

## Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Commit Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning (white-space, formatting, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes affecting build system or external dependencies
- **ci**: Changes to CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

## Examples

### Simple Feature
```
feat: add user authentication

Implement JWT-based authentication with login/logout endpoints
and token validation middleware.
```

### Bug Fix with Scope
```
fix(api): correct user validation logic

The email validation regex was too restrictive and rejected
valid email addresses with special characters.

Fixes #123
```

### Breaking Change
```
feat(api)!: redesign user authentication API

BREAKING CHANGE: The /auth/login endpoint now returns a different
response format. Clients must update to use the new structure:

Before:
{ "token": "..." }

After:
{ "access_token": "...", "refresh_token": "...", "expires_in": 3600 }
```

### Multiple Changes
```
feat: add search and pagination to user list

- Implement full-text search across user fields
- Add pagination with configurable page size
- Include sorting by multiple columns
- Add filters for user status and role

Related to #456
```

## Task Execution

When generating commit messages:

1. **Analyze Changes**
   - Review git diff
   - Identify primary purpose
   - Check for breaking changes
   - Note related issues

2. **Determine Type**
   - What is the main purpose of this change?
   - Use the most specific applicable type

3. **Add Scope (if applicable)**
   - api, ui, database, auth, etc.
   - Keep scopes consistent across project
   - Only include if it adds clarity

4. **Write Description**
   - Start with lowercase verb
   - Use imperative mood ("add" not "added")
   - Keep under 72 characters
   - Be specific but concise

5. **Add Body (if needed)**
   - Explain WHAT and WHY, not HOW
   - Wrap at 72 characters
   - Include motivation and context
   - Reference issues/PRs

6. **Add Footer (if applicable)**
   - Breaking changes: `BREAKING CHANGE: description`
   - Issue references: `Fixes #123` or `Related to #456`
   - Co-authors: `Co-authored-by: Name <email>`

## Best Practices

**Do:**
- Use present tense ("add feature" not "added feature")
- Use imperative mood ("move cursor to" not "moves cursor to")
- Be specific about what changed
- Reference issues when applicable
- Explain WHY for complex changes
- Mark breaking changes clearly

**Don't:**
- Mix multiple unrelated changes
- Use vague descriptions ("update code", "fix bug")
- Exceed 72 characters in subject line
- Include implementation details in subject
- Forget to mention breaking changes

## Validation Checklist

Before committing, verify:
- [ ] Type is correct and specific
- [ ] Description is clear and under 72 chars
- [ ] Breaking changes are marked with `!` and `BREAKING CHANGE:`
- [ ] Related issues are referenced
- [ ] Body explains WHY if needed
- [ ] Changes are atomic and focused

## Integration with Git

```bash
# Commit with the generated message
git commit -m "feat(auth): add JWT token refresh

Implement automatic token refresh when tokens are close to expiration.
This improves user experience by reducing forced logouts.

Fixes #789"
```

## Output
Present the commit message to the user for review before executing the commit.
