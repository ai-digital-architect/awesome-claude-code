# First Ask - Interactive Scope Interrogation

Interactive workflow that interrogates project scope, deliverables, and constraints before starting implementation.

## Purpose
Before diving into implementation, this command helps clarify:
- What needs to be built
- Why it's needed
- What constraints exist
- What success looks like

## Interrogation Process

Ask the user the following questions systematically:

### 1. Project Understanding
- What problem are we trying to solve?
- Who is the target user/audience?
- What is the expected outcome?

### 2. Scope Definition
- What are the must-have features? (MVP)
- What are nice-to-have features?
- What is explicitly out of scope?
- Are there any existing systems to integrate with?

### 3. Technical Constraints
- Are there specific technologies that must be used?
- Are there performance requirements?
- Are there security/compliance requirements?
- What browsers/platforms must be supported?

### 4. Resources & Timeline
- What is the target timeline?
- Are there any milestones or checkpoints?
- What resources are available (team size, budget)?
- Are there dependencies on other teams/projects?

### 5. Success Criteria
- How will we know this is successful?
- What metrics matter?
- What does "done" look like?
- What are the acceptance criteria?

### 6. Risks & Assumptions
- What could go wrong?
- What assumptions are we making?
- Are there any unknowns to investigate first?
- What's the backup plan?

## Output
After gathering responses, create a summary document:

```markdown
# Project Brief: [Project Name]

## Problem Statement
[Clear description of the problem]

## Objectives
- [Objective 1]
- [Objective 2]

## Scope
### In Scope
- [Feature/Requirement 1]
- [Feature/Requirement 2]

### Out of Scope
- [Explicitly excluded items]

## Constraints
- Technical: [Constraints]
- Timeline: [Timeline]
- Resources: [Resources]

## Success Criteria
- [Criterion 1]
- [Criterion 2]

## Risks & Mitigation
- Risk: [Risk] → Mitigation: [Strategy]

## Next Steps
1. [First action]
2. [Second action]
```

Save this as `docs/briefs/{project-name}-brief.md`

## Usage Notes
- Use this at the start of new features or projects
- Don't skip questions even if answers seem obvious
- Document assumptions explicitly
- Get user confirmation before proceeding to implementation
