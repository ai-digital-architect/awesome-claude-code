# Create Implementation Plan

Generate a detailed, phased implementation plan for features, refactoring, or system upgrades.

## Task
Analyze the current codebase and create a step-by-step implementation plan that breaks down the work into manageable phases.

## Plan Structure

### Phase Analysis
For each phase, include:

1. **Phase Overview**
   - Phase number and name
   - Primary objectives
   - Estimated complexity (Small/Medium/Large)

2. **Prerequisites**
   - Required knowledge or setup
   - Dependencies on previous phases
   - Team readiness

3. **Implementation Steps**
   - Specific tasks in order
   - Files to modify or create
   - Code patterns to follow

4. **Testing Requirements**
   - Unit tests to write
   - Integration test scenarios
   - Manual testing checklist

5. **Success Criteria**
   - How to verify completion
   - Performance benchmarks
   - Quality metrics

6. **Rollback Plan**
   - How to revert if needed
   - Data migration considerations

### Risk Assessment
- Potential blockers
- Technical challenges
- Mitigation strategies

### Timeline Estimates
- Development time per phase
- Testing time
- Review and deployment time

## Output Format
Save as `docs/plans/IMPLEMENTATION_PLAN.md` or in the relevant feature directory.

## Best Practices
- Break large features into small, shippable increments
- Prioritize high-value, low-risk phases first
- Include migration strategies for breaking changes
- Plan for backward compatibility where needed
- Consider feature flags for gradual rollout
