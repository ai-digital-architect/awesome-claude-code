# Create GitHub Issues from Specification

Generate GitHub issues from a specification document, breaking down requirements into trackable work items.

## Purpose
Convert specification documents into actionable GitHub issues that:
- Break down large features into manageable tasks
- Provide clear acceptance criteria
- Enable parallel development
- Track progress effectively

## Process

### 1. Analyze Specification
Review the spec document to identify:
- Major features/components
- Individual requirements
- Technical tasks
- Testing requirements
- Documentation needs

### 2. Group Related Work
Organize work into logical groups:
- Frontend tasks
- Backend tasks
- Database changes
- Infrastructure updates
- Documentation
- Testing

### 3. Create Issue Structure

For each issue, include:

```markdown
## Title
[Component]: Brief description

## Description
Detailed explanation of what needs to be done

## Context
Why this is needed and how it fits into the larger feature

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Technical Notes
- Approach suggestions
- Files to modify
- Dependencies

## Related Issues
- Depends on: #123
- Blocks: #456
- Related to: #789

## Labels
- `feature` / `bug` / `enhancement`
- `frontend` / `backend` / `infrastructure`
- `priority:high` / `priority:medium` / `priority:low`

## Estimated Effort
Story points or time estimate
```

## Example Issues

### Feature Issue
```markdown
# [Auth] Implement JWT token validation middleware

## Description
Create Express middleware to validate JWT tokens on protected routes.

## Context
Part of the authentication system. This middleware will be used
to protect admin and user-specific endpoints.

## Acceptance Criteria
- [ ] Middleware validates JWT signature
- [ ] Expired tokens are rejected with 401
- [ ] Invalid tokens are rejected with 401
- [ ] Valid tokens attach user data to request
- [ ] Error responses follow API error format
- [ ] Unit tests cover all scenarios

## Technical Notes
- Use `jsonwebtoken` library
- Create in `src/middleware/auth.ts`
- Extract secret from environment config
- Follow existing middleware patterns

## Dependencies
- Requires: #123 (JWT token generation)
- Blocks: #456 (Protected admin routes)

## Labels
`feature`, `backend`, `auth`, `priority:high`

## Effort
3 story points (1-2 days)
```

### Bug Issue
```markdown
# [API] Fix email validation rejecting valid addresses

## Description
Email validation regex rejects valid email addresses containing
plus signs (e.g., user+tag@example.com)

## Steps to Reproduce
1. POST to /api/users/register
2. Use email: test+tag@example.com
3. Receive 400 error: "Invalid email"

## Expected Behavior
Email addresses with plus signs should be accepted per RFC 5322

## Acceptance Criteria
- [ ] Validation accepts emails with plus signs
- [ ] Validation accepts other valid special chars
- [ ] Invalid emails still rejected
- [ ] Tests cover edge cases
- [ ] No breaking changes to API

## Technical Notes
- Update regex in `src/validators/user.validator.ts`
- Reference: RFC 5322 email specification
- Consider using a validation library

## Labels
`bug`, `backend`, `validation`, `priority:medium`

## Effort
1 story point (2-4 hours)
```

## Issue Creation Workflow

1. **Review Specification**
   - Read spec document thoroughly
   - Identify all requirements
   - Note dependencies

2. **Create Epic/Milestone** (if large feature)
   - Create parent issue or milestone
   - Link all related issues

3. **Draft Issues**
   - One issue per focused task
   - Clear, actionable descriptions
   - Complete acceptance criteria
   - Appropriate labels

4. **Set Priority and Dependencies**
   - Mark critical path items
   - Note what blocks what
   - Assign to milestones

5. **Review and Create**
   - Verify issues are clear
   - Check for duplicates
   - Create in GitHub

## GitHub CLI Commands

```bash
# Create a feature issue
gh issue create \
  --title "[Auth] Implement JWT validation middleware" \
  --body-file .github/issue-templates/feature-issue.md \
  --label "feature,backend,auth" \
  --assignee "@me" \
  --milestone "v2.0"

# Create multiple issues from a list
while IFS= read -r title; do
  gh issue create --title "$title" --label "feature"
done < issues-list.txt

# Link related issues
gh issue comment 123 --body "Depends on #122"
```

## Output Format

Present issues in two formats:

1. **Summary Table**
```markdown
| # | Title | Type | Priority | Estimate |
|---|-------|------|----------|----------|
| 1 | [Auth] JWT validation | Feature | High | 3 pts |
| 2 | [Auth] Login endpoint | Feature | High | 5 pts |
| 3 | [DB] User schema update | Task | Medium | 2 pts |
```

2. **Individual Issue Markdown**
Save each issue as `issues/{number}-{slug}.md` for review before creation

## Best Practices

**Do:**
- Keep issues focused and atomic
- Write clear acceptance criteria
- Include technical context
- Link related issues
- Use consistent labeling
- Add effort estimates

**Don't:**
- Create issues that are too large
- Mix multiple unrelated changes
- Write vague descriptions
- Forget dependencies
- Skip acceptance criteria
- Leave issues unassigned to milestones

## Usage
```bash
# Use this command with a spec file
/github-issues-from-spec docs/specs/authentication-feature.md
```
