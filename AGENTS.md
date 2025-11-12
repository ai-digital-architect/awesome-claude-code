# AGENTS.md - Claude Code Agent Catalog

## Overview
This document catalogs all available agents in the Claude Code ecosystem. Agents are specialized AI assistants with specific roles, capabilities, and expertise areas. They can be invoked using the Task tool with the appropriate `subagent_type` parameter.

## Built-in Agents

### 1. General-Purpose Agent
**Subagent Type**: `general-purpose`

**Description**: Multi-faceted agent for complex, multi-step tasks requiring broad capabilities.

**Capabilities**:
- Research complex questions across multiple files
- Search for code patterns and implementations
- Execute multi-step workflows autonomously
- Access to all available tools

**When to Use**:
- Investigating unfamiliar codebases
- Multi-step refactoring tasks
- Complex feature implementation requiring research
- Tasks requiring iteration and discovery

**Example Invocations**:
```
Use the Task tool to launch a general-purpose agent to:
- "Find all API endpoints and document their authentication requirements"
- "Research how error handling works across the codebase and suggest improvements"
- "Implement user authentication with OAuth2, researching existing patterns first"
```

**Best Practices**:
- Provide clear, detailed task descriptions
- Specify what information to return in the final report
- Use when you need autonomous multi-step execution
- Launch in parallel when possible for independent tasks

---

### 2. Explore Agent
**Subagent Type**: `Explore`

**Description**: Fast, specialized agent for codebase exploration and discovery.

**Capabilities**:
- Quick file pattern matching (e.g., "src/components/**/*.tsx")
- Keyword searches across the codebase
- Understanding code organization and structure
- Finding specific implementations or patterns
- Access to all tools with focus on search and analysis

**Thoroughness Levels**:
- `quick`: Basic searches, single-pass exploration (fastest)
- `medium`: Moderate exploration, checks multiple locations
- `very thorough`: Comprehensive analysis across all relevant areas

**When to Use**:
- Understanding codebase structure
- Finding specific code patterns or implementations
- Locating where features are implemented
- Quick discovery without modification needs
- Answering "where" and "how" questions about code

**Example Invocations**:
```
Use the Task tool with subagent_type=Explore:
- "Find all React components that use the useAuth hook (quick)"
- "Locate error handling patterns in the API layer (medium)"
- "Comprehensively map all database query patterns (very thorough)"
```

**Best Practices**:
- Specify thoroughness level based on task needs
- Use "quick" for simple lookups
- Use "medium" for moderate complexity
- Use "very thorough" for comprehensive audits
- Prefer Explore over direct Grep/Glob for open-ended searches

---

### 3. Plan Agent
**Subagent Type**: `Plan`

**Description**: Specialized agent for planning and architectural design.

**Capabilities**:
- Analyze codebase to understand architecture
- Design implementation plans
- Identify files and components to modify
- Assess impact and risks
- Create detailed roadmaps
- Access to all tools with focus on analysis

**Thoroughness Levels**:
- `quick`: High-level planning, basic approach
- `medium`: Detailed planning with impact analysis
- `very thorough`: Comprehensive planning with all considerations

**When to Use**:
- Planning new features before implementation
- Designing refactoring approaches
- Architecture decisions requiring analysis
- Creating implementation roadmaps
- Risk assessment for changes

**Example Invocations**:
```
Use the Task tool with subagent_type=Plan:
- "Plan the implementation of a real-time notification system (medium)"
- "Design a migration strategy from REST to GraphQL (very thorough)"
- "Create a quick plan for adding dark mode support (quick)"
```

**Best Practices**:
- Use before starting complex implementations
- Request specific deliverables (files to modify, steps, risks)
- Specify thoroughness based on change complexity
- Review plan output before proceeding with implementation

---

### 4. Statusline Setup Agent
**Subagent Type**: `statusline-setup`

**Description**: Specialized agent for configuring Claude Code's status line settings.

**Capabilities**:
- Read current status line configuration
- Edit status line settings
- Configure display options
- Troubleshoot status line issues

**Tools Available**:
- Read
- Edit

**When to Use**:
- Configuring status line appearance
- Customizing information displayed
- Troubleshooting status line problems
- Setting up status line for first time

**Example Invocations**:
```
Use the Task tool with subagent_type=statusline-setup:
- "Configure the status line to show git branch and token usage"
- "Fix status line not displaying properly"
- "Customize status line colors and format"
```

**Best Practices**:
- Provide specific requirements for status line display
- Test changes after configuration
- Keep status line configuration minimal for performance

---

## Custom Agent Development

### Creating Custom Agents

You can define custom agents in `.claude/agents/` to specialize Claude's behavior for your project needs.

**Agent Definition Template**:
```markdown
# Agent Name

## Role
[Define the agent's primary role]

## Expertise Areas
- [Area 1]
- [Area 2]
- [Area 3]

## Activation Triggers
- [When this agent should be used]
- [Specific keywords or contexts]

## Capabilities
- [What the agent can do]
- [Specific tools or knowledge]

## Example Usage
[Provide example scenarios and invocations]

## Limitations
[What the agent should not do]
```

**Example Custom Agents**:

### Code Review Agent
```markdown
# Code Review Agent

## Role
Perform comprehensive code reviews with focus on quality, security, and best practices.

## Expertise Areas
- Security vulnerability detection
- Performance optimization
- Code maintainability
- Test coverage analysis

## Activation Triggers
- Use when: code review requested
- Keywords: "review", "audit", "check quality"

## Capabilities
- Static code analysis
- Security scanning
- Performance profiling suggestions
- Test coverage assessment

## Example Usage
"Review the authentication module for security vulnerabilities and performance issues"

## Limitations
Does not execute code or run tests, focuses on static analysis only.
```

### Documentation Agent
```markdown
# Documentation Agent

## Role
Create and maintain comprehensive project documentation.

## Expertise Areas
- API documentation
- README files
- Architecture diagrams
- Onboarding guides

## Activation Triggers
- Use when: documentation needed
- Keywords: "document", "explain", "write guide"

## Capabilities
- Generate API documentation from code
- Create architecture documentation
- Write user guides
- Update README files

## Example Usage
"Document all API endpoints in the user service with examples"

## Limitations
Relies on existing code; cannot infer undocumented business logic.
```

---

## Agent Selection Guide

### Decision Tree

```
Is this a multi-step research task?
├─ Yes → Use general-purpose agent
└─ No
    ├─ Need to explore/find code?
    │   └─ Use Explore agent (specify thoroughness)
    ├─ Need to plan implementation?
    │   └─ Use Plan agent (specify thoroughness)
    ├─ Configuring status line?
    │   └─ Use statusline-setup agent
    └─ Other specialized task?
        └─ Check custom agents or use appropriate tool directly
```

### Quick Reference Table

| Task Type | Agent | Thoroughness | Typical Duration |
|-----------|-------|--------------|------------------|
| Find specific code | Explore | quick | < 30 sec |
| Understand architecture | Explore | medium | 1-2 min |
| Full codebase audit | Explore | very thorough | 3-5 min |
| Quick feature plan | Plan | quick | 1-2 min |
| Detailed planning | Plan | medium | 2-4 min |
| Complex architecture | Plan | very thorough | 5-10 min |
| Multi-step research | general-purpose | N/A | Variable |
| Status line config | statusline-setup | N/A | < 1 min |

---

## Best Practices

### 1. Agent Invocation
- **Be specific**: Provide clear, detailed task descriptions
- **Set expectations**: Specify what information you want returned
- **Use thoroughness wisely**: Balance speed vs completeness
- **Parallel execution**: Launch multiple agents in parallel when tasks are independent

### 2. Agent Selection
- **Explore vs General-Purpose**: Use Explore for searches; general-purpose for complex workflows
- **Plan before Execute**: Use Plan agent before complex implementations
- **Right tool for job**: Don't use agents when direct tools are more appropriate

### 3. Performance Optimization
- **Minimize agent use**: Direct tools are faster for simple tasks
- **Parallel agents**: Send single message with multiple Task calls
- **Appropriate thoroughness**: Don't use "very thorough" when "quick" suffices
- **Cache awareness**: Agents don't share context between invocations

### 4. Effective Communication
- **Detailed prompts**: Include all necessary context in initial prompt
- **Specify deliverables**: Tell agent exactly what to return
- **Stateless design**: Each invocation is independent; include all info needed
- **Trust output**: Agent outputs are generally reliable

---

## Common Patterns

### Pattern 1: Comprehensive Feature Implementation
```
1. Launch Plan agent (medium thoroughness)
   - Research existing patterns
   - Design implementation approach
   - Identify files to modify

2. Review plan output

3. Launch general-purpose agent with implementation task
   - Reference the plan
   - Specify quality requirements
   - Include testing requirements

4. Review implementation
```

### Pattern 2: Codebase Discovery
```
1. Launch Explore agent (quick)
   - Find initial patterns
   - Understand structure

2. If needed, launch Explore agent (medium)
   - Deeper investigation
   - Multiple locations

3. If comprehensive needed, launch Explore (very thorough)
   - Complete mapping
   - All variations
```

### Pattern 3: Parallel Investigation
```
Launch multiple Explore agents in parallel:
- Agent 1: "Find all API endpoints (quick)"
- Agent 2: "Find all database queries (quick)"
- Agent 3: "Find all authentication code (quick)"

Process results concurrently for fast overview.
```

### Pattern 4: Iterative Refinement
```
1. Explore agent (quick): Get initial understanding
2. Review results
3. Plan agent (medium): Design based on findings
4. Review plan
5. general-purpose agent: Implement with iterations
```

---

## Troubleshooting

### Agent Not Finding Code
- **Issue**: Explore agent returns no results
- **Solutions**:
  - Increase thoroughness level
  - Broaden search terms
  - Check if code exists in expected locations
  - Use general-purpose for more flexible search

### Agent Taking Too Long
- **Issue**: Agent exceeds expected duration
- **Solutions**:
  - Reduce thoroughness level
  - Narrow the scope of the task
  - Break into smaller, parallel sub-tasks
  - Use more specific search criteria

### Agent Missing Context
- **Issue**: Agent doesn't have necessary information
- **Solutions**:
  - Include all context in the prompt (agents are stateless)
  - Reference specific files or locations
  - Provide examples of expected output
  - Break task into smaller steps with explicit context

### Unclear Agent Output
- **Issue**: Agent returns vague or incomplete results
- **Solutions**:
  - Specify exactly what information to return
  - Request specific format (list, table, code, etc.)
  - Ask for examples in output
  - Increase thoroughness level

---

## Integration with Claude Code

### Using Agents in Workflows

**Quality Checkpoint Workflow** (with `/qplan`, `/qcode`, `/qcheck`):
```
1. /qplan → Uses Plan agent to analyze approach
2. /qcode → May use general-purpose for implementation
3. /qcheck → Manual review or custom review agent
```

**TDD Workflow** (with `/tdd`):
```
1. Plan agent: Design test strategy
2. general-purpose agent: Implement tests and code
3. Explore agent: Verify coverage
```

**Feature Planning** (with `/plan-feature`):
```
1. Explore agent: Understand current implementation
2. Plan agent: Design new feature
3. Review and approval
4. general-purpose agent: Implementation
```

### Agent Hooks Integration

Agents respect all configured hooks:
- **Security hooks**: Sensitive file protection applies
- **Auto-format hooks**: Code modifications are formatted
- **Logging hooks**: Agent actions are logged
- **Session hooks**: Included in session summaries

---

## Advanced Topics

### Agent Performance Tuning

**For Speed**:
- Use "quick" thoroughness
- Narrow scope with specific paths
- Use Explore for searches (not general-purpose)
- Direct tools when possible

**For Completeness**:
- Use "very thorough" thoroughness
- Broad scope with multiple patterns
- Use general-purpose for complex tasks
- Allow more time for execution

### Multi-Agent Orchestration

**Serial Execution** (when dependent):
```
1. Wait for Agent 1 to complete
2. Use Agent 1 output in Agent 2 prompt
3. Use Agent 2 output in Agent 3 prompt
```

**Parallel Execution** (when independent):
```
Send single message with multiple Task calls:
- All agents launch simultaneously
- Process results concurrently
- Combine outputs
```

### Custom Agent Development

**Steps**:
1. Create `.claude/agents/agent-name.md`
2. Define role, capabilities, activation triggers
3. Document usage examples
4. Test with various scenarios
5. Add to this catalog

**Considerations**:
- Keep scope focused and specific
- Clear activation criteria
- Document limitations
- Provide usage examples

---

## Resources

### Documentation
- Claude Code Docs: https://docs.claude.com/claude-code
- Task Tool Documentation: See system prompts
- Agent Development: `.claude/agents/README.md`

### Examples
- See `.claude/agents/` for custom agent definitions
- Check `docs/onboarding/` for workflow examples
- Review `CLAUDE.md` for project-specific patterns

### Community
- Share custom agents in team documentation
- Document lessons learned
- Contribute patterns back to this catalog

---

## Changelog

### Version 1.0 (Initial)
- Documented all built-in agents
- Added custom agent development guide
- Included best practices and patterns
- Created troubleshooting section

---

**This catalog is maintained as part of the Claude Code enhanced setup.**
**Last Updated**: Auto-generated during setup
**Maintainer**: Project Team

For questions or additions, update this file and share with the team.
