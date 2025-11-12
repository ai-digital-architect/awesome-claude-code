# Boost Prompt - Refine Your Request

Improve the quality and clarity of user prompts through structured interrogation and refinement.

## Purpose
When a user's request is vague or could benefit from more specificity, use this workflow to:
- Clarify unclear requirements
- Surface hidden assumptions
- Identify missing context
- Refine the prompt for better results

## Refinement Process

### 1. Analyze Current Prompt
- What is the user asking for?
- What is clear vs. unclear?
- What context is missing?
- What assumptions might be wrong?

### 2. Ask Clarifying Questions

**Scope Questions:**
- What is the specific goal you want to achieve?
- What files/components should be affected?
- Should this apply project-wide or to specific areas?

**Context Questions:**
- What problem led to this request?
- Have you tried anything already?
- Are there existing patterns in the codebase to follow?

**Constraint Questions:**
- Are there specific technologies/approaches to use or avoid?
- Are there performance/security requirements?
- Are there backward compatibility needs?

**Success Questions:**
- How will you know this is working correctly?
- What should the end result look like?
- Are there specific test cases to verify?

### 3. Synthesize Improved Prompt

After gathering answers, create a refined prompt:

```markdown
## Original Request
[User's original prompt]

## Refined Request
[Improved, specific prompt incorporating clarifications]

### Context
[Relevant background and constraints]

### Objectives
1. [Specific objective]
2. [Specific objective]

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Technical Approach
[Suggested approach based on context]

### Files/Components Affected
- [File/component 1]
- [File/component 2]
```

## Example

**Original:** "Add authentication to the app"

**After Boost Prompt:**
```markdown
## Refined Request
Implement JWT-based authentication for the Express API with:
- Login endpoint (/api/auth/login)
- Token validation middleware
- User session management
- Password hashing with bcrypt

### Context
- Using Express.js backend
- PostgreSQL database with existing users table
- Need to protect /api/admin/* routes
- Frontend is React using fetch API

### Acceptance Criteria
- [ ] Users can login with email/password
- [ ] JWT tokens expire after 24 hours
- [ ] Protected routes reject invalid tokens
- [ ] Passwords are securely hashed
- [ ] Integration tests cover auth flows
```

## When to Use
- User requests are high-level or vague
- Multiple valid interpretations exist
- Significant implementation decisions needed
- Risk of misunderstanding requirements
- Complex or ambiguous requirements

## Output
Present the refined prompt to the user for confirmation before proceeding with implementation.
