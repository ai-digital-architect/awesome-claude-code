# Architectural Decision Record (ADR)

Document significant technical and architectural decisions using the ADR format.

## Task
Create an Architectural Decision Record that captures:

1. **Title**
   - ADR number and descriptive title
   - Format: "ADR-XXX: [Decision Title]"

2. **Status**
   - Proposed, Accepted, Deprecated, or Superseded
   - Date of status change

3. **Context**
   - What is the issue we're facing?
   - What factors are driving this decision?
   - What constraints exist?
   - What requirements must be met?

4. **Decision**
   - What decision have we made?
   - Clear statement of the chosen approach

5. **Alternatives Considered**
   - What other options were evaluated?
   - Why were they not chosen?
   - Trade-offs of each option

6. **Consequences**
   - What becomes easier?
   - What becomes harder?
   - Positive impacts
   - Negative impacts
   - Risks and mitigation strategies

7. **Implementation Notes**
   - Key steps to implement
   - Timeline considerations
   - Migration path (if applicable)

## Output Format
Save as `docs/adr/ADR-{number}-{kebab-case-title}.md`

## Example Structure

```markdown
# ADR-001: Use PostgreSQL for Primary Database

**Status:** Accepted
**Date:** 2025-01-15
**Deciders:** Engineering Team

## Context
We need to choose a database for our multi-tenant SaaS application...

## Decision
We will use PostgreSQL as our primary database...

## Alternatives Considered
1. MongoDB - NoSQL flexibility but...
2. MySQL - Mature but lacks...
3. DynamoDB - Serverless benefits but...

## Consequences
### Positive
- ACID compliance
- Rich query capabilities
- Strong ecosystem

### Negative
- Scaling complexity
- Operational overhead

## Implementation
- Week 1: Setup RDS instance
- Week 2: Schema migration
- Week 3: Integration testing
```

## Best Practices
- Write ADRs for significant decisions only
- Keep them concise and factual
- Update status as decisions evolve
- Link to related ADRs
- Include date and decision makers
