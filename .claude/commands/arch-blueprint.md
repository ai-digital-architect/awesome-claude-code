# Architecture Blueprint Generator

Analyze the codebase to create detailed architectural documentation that captures the system's structure, patterns, and design decisions.

## Task
Generate comprehensive architectural documentation by analyzing:

1. **System Overview**
   - High-level architecture diagram (as text/mermaid)
   - Core components and their responsibilities
   - Technology stack analysis

2. **Architectural Patterns**
   - Design patterns in use (MVC, Repository, Factory, etc.)
   - Architectural style (Microservices, Monolith, Serverless, etc.)
   - Data flow patterns

3. **Component Analysis**
   - Frontend architecture
   - Backend architecture
   - Database design
   - External integrations

4. **Directory Structure**
   - Logical organization
   - Module boundaries
   - Dependency relationships

5. **Key Design Decisions**
   - Why certain patterns were chosen
   - Trade-offs made
   - Alternative approaches considered

6. **Data Architecture**
   - Data models and schemas
   - Data flow diagrams
   - Storage strategies

7. **Integration Points**
   - APIs and endpoints
   - Third-party services
   - Event-driven components

8. **Quality Attributes**
   - Scalability approach
   - Security measures
   - Performance optimizations
   - Reliability patterns

## Output Format
Create `docs/architecture/ARCHITECTURE.md` with:
- Mermaid diagrams where applicable
- Clear section headers
- Code examples for patterns
- References to key files

## Analysis Approach
1. Start with entry points (main.ts, app.ts, index.ts)
2. Map module dependencies
3. Identify core abstractions
4. Document data flows
5. Capture design patterns
6. Note architectural decisions

## Usage
Run this command when:
- Onboarding new team members
- Planning major refactoring
- Documenting legacy systems
- Preparing for architecture reviews
