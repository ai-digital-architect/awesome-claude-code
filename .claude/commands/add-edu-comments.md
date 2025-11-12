# Add Educational Comments

Annotate code with instructional comments and explanations to help others (or your future self) understand the implementation.

## Purpose
Transform working code into educational material by adding:
- Clear explanations of what the code does
- Why certain approaches were chosen
- How components interact
- Common pitfalls and gotchas
- Links to relevant documentation

## Comment Types

### 1. Overview Comments
Explain the overall purpose and structure:
```typescript
/**
 * UserAuthenticationService
 *
 * Handles all user authentication logic including:
 * - Login/logout flows
 * - JWT token generation and validation
 * - Password hashing and verification
 * - Session management
 *
 * This service integrates with the UserRepository for data access
 * and uses bcrypt for secure password handling.
 */
```

### 2. Function/Method Comments
Describe purpose, parameters, return values, and usage:
```typescript
/**
 * Validates a JWT token and returns the decoded payload.
 *
 * @param token - The JWT string to validate
 * @returns Decoded token payload containing user information
 * @throws TokenExpiredError if token has expired
 * @throws JsonWebTokenError if token is invalid
 *
 * Example:
 *   const payload = await validateToken(req.headers.authorization);
 *   console.log(payload.userId); // "user-123"
 */
```

### 3. Inline Explanations
Explain complex logic or non-obvious code:
```typescript
// Sort users by last activity, with null dates appearing last
// This ensures active users appear first in the list
users.sort((a, b) => {
  if (!a.lastActive) return 1;
  if (!b.lastActive) return -1;
  return b.lastActive.getTime() - a.lastActive.getTime();
});
```

### 4. Gotcha Comments
Warn about common mistakes or edge cases:
```typescript
// IMPORTANT: This must run BEFORE the authentication middleware
// or the session won't be available to auth checks
app.use(sessionMiddleware);
app.use(authMiddleware);
```

### 5. Pattern Explanations
Explain design patterns or architectural decisions:
```typescript
// Using the Repository Pattern to abstract database operations
// This allows us to swap data sources without changing business logic
class UserRepository {
  // All database access happens through this class
}
```

### 6. Learning References
Link to documentation and resources:
```typescript
// Using debounce to limit API calls during user input
// Learn more: https://lodash.com/docs/#debounce
// Pattern: https://davidwalsh.name/javascript-debounce-function
const debouncedSearch = debounce(searchAPI, 300);
```

## Guidelines

**Do:**
- Explain WHY, not just WHAT
- Focus on non-obvious code
- Include examples where helpful
- Reference documentation
- Explain trade-offs and alternatives
- Use clear, beginner-friendly language

**Don't:**
- State the obvious (`i++; // increment i`)
- Repeat information from function names
- Leave outdated comments
- Over-comment simple code
- Use comments to disable code (remove it instead)

## Task Execution

When adding educational comments:

1. **Identify Key Areas**
   - Complex algorithms
   - Design patterns
   - Non-obvious logic
   - Important gotchas
   - Integration points

2. **Add Structured Comments**
   - File/class overview
   - Function documentation
   - Inline explanations
   - Usage examples

3. **Verify Accuracy**
   - Ensure comments match code
   - Test all examples
   - Verify links work

4. **Consider Audience**
   - What would a junior developer need to know?
   - What confused you when writing this?
   - What questions might reviewers ask?

## Output
Update the relevant files with educational comments that make the codebase more accessible and maintainable.
