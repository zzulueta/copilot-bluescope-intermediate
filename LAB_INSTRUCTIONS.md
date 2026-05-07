# GitHub Copilot Advanced Features Lab
## Steel Inventory Management API

**Duration:** 2 hours  
**Level:** Intermediate to Advanced  
**Organization:** BlueScope

---

## Pre-Lab Setup (15 minutes before lab)

### 1. Prerequisites
- GitHub Copilot license activated
- VS Code with GitHub Copilot extensions installed
- Python 3.9+ installed
- Git configured

### 2. Clone and Setup
```bash
cd bluescope/steel-inventory-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Verify Setup
```bash
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs - you should see the API documentation.

### 4. Initial Commit
```bash
git init
git add .
git commit -m "Initial project scaffold"
git branch -M main
```

---

## Lab Overview

You'll enhance a partially implemented Steel Inventory Management API using GitHub Copilot's advanced features. The starter code has intentional bugs, missing features, and incomplete tests.

### Learning Objectives Checklist
- [ ] Apply decomposition prompting
- [ ] Use test-first development
- [ ] Apply refactor-first patterns
- [ ] Generate PR summaries
- [ ] Generate semantic commit messages
- [ ] Perform Copilot code reviews (multiple modes)
- [ ] Create custom agents (.agent.md)
- [ ] Create agent skills (SKILL.md)
- [ ] Use Copilot Memory
- [ ] Verify with Diagnostics view

---

## Part 1: Advanced Prompting Patterns (30 minutes)

### Exercise 1.1: Fix Bugs Using Decomposition (10 min)

**Current Issues:**
1. `database.py` - duplicate product codes not prevented
2. `database.py` - `last_updated` not set on updates
3. `routers/inventory.py` - negative quantities allowed
4. `steel_utils.py` - `calculate_area_m2()` crashes on None width

**Task:** Use Copilot with decomposition prompting

1. Open Copilot Chat and use this pattern:
```
I need to fix the duplicate product code bug in database.py. Let's break this down:
1. First, show me where product codes are validated
2. Then, suggest validation logic to check for duplicates
3. Finally, show where to add this validation in the create method
```

2. For each bug, use decomposition:
   - Identify the problem location
   - Understand the root cause
   - Propose a solution
   - Implement with Copilot's help

**Expected Outcome:** All 4 bugs fixed with clear, maintainable code.

**Commit:** 
```bash
git add .
# Use Copilot to generate commit message: Ctrl+I in commit message box
# Expected: "fix: prevent duplicate product codes and handle None values in calculations"
```

---

### Exercise 1.2: Test-First Development (10 min)

**Task:** Add comprehensive tests BEFORE implementing new features

1. Open `tests/test_inventory.py`
2. In Copilot Chat, use test-first prompting:
```
Using TDD, I want to add a feature to search products by grade. 
First, write comprehensive tests for this feature including:
- Searching for existing grade
- Searching for non-existent grade
- Case-insensitive search
- Empty results handling

Don't implement the feature yet, just the tests.
```

3. Run the tests (they should fail):
```bash
pytest tests/test_inventory.py -v
```

4. Now ask Copilot to implement the feature to make tests pass:
```
Now implement the search_by_grade endpoint in routers/inventory.py to make these tests pass
```

**Expected Outcome:** 
- Tests written first (failing)
- Feature implemented (tests passing)
- `GET /inventory/search?grade=A36` endpoint working

**Commit:**
```bash
git add tests/
git commit -m "test: add comprehensive tests for grade search feature"
git add app/routers/inventory.py
# Use Copilot for commit message
```

---

### Exercise 1.3: Refactor-First Pattern (10 min)

**Task:** Refactor the steel_utils.py before adding new features

1. Open `app/utils/steel_utils.py`
2. Use refactor-first prompting:
```
I want to add weight calculations for coil, bar, and tube shapes.
Before adding new features, let's refactor the existing code:
1. Extract shape-specific calculations into separate functions
2. Add proper type hints
3. Add comprehensive docstrings
4. Add input validation

Show me the refactored structure first.
```

3. Review the refactoring suggestions
4. Apply the refactoring
5. NOW add the new calculations:
```
Now implement weight calculations for:
- coil (use rectangular approximation)
- bar (circular cross-section: π * r² * length * density)
- tube (hollow circular: π * (r_outer² - r_inner²) * length * density)
```

**Expected Outcome:**
- Clean, well-structured code
- All shape types supported
- Proper documentation

**Commit with Copilot-generated message**

---

## Part 2: GitHub Workflow Integration (25 minutes)

### Exercise 2.1: Create Feature Branch with PR (10 min)

1. Create a new feature branch:
```bash
git checkout -b feature/low-stock-alerts
```

2. Implement low stock alert feature. Ask Copilot:
```
Add a low stock alert feature:
1. Add a `min_stock_level` field to SteelProduct model
2. Create an endpoint GET /inventory/low-stock that returns products below their minimum
3. Add a field to track whether an alert has been sent
```

3. Stage your changes:
```bash
git add .
```

4. Use Copilot to generate a semantic commit message:
   - In VS Code, open Source Control view
   - Click in the commit message box
   - Press `Ctrl+I` (Inline Copilot)
   - Type: `generate commit message`

5. Commit and push:
```bash
git commit
# Your Copilot-generated message will be used
git push origin feature/low-stock-alerts
```

---

### Exercise 2.2: Generate PR Summary (5 min)

1. Create a PR on GitHub (or simulate locally)
2. Use Copilot to generate a comprehensive PR description:

In Copilot Chat:
```
Generate a pull request description for the low-stock-alerts feature.
Include:
- Summary of changes
- Technical details
- Testing done
- Breaking changes (if any)
Use professional PR template format
```

3. Copy the generated description to your PR

**Expected Output:**
```markdown
## Summary
Implements low stock alerting system for inventory management...

## Changes
- Added `min_stock_level` field to SteelProduct model
- Created `/inventory/low-stock` endpoint
...

## Testing
- Added unit tests for low stock detection
...
```

---

### Exercise 2.3: Copilot Code Review - All Modes (10 min)

**Task:** Experience different code review modes

#### A. Manual Code Review with Copilot
1. Open any file (e.g., `routers/inventory.py`)
2. Select a function
3. Ask Copilot:
```
Review this function for:
- Performance issues
- Security vulnerabilities
- Best practices
- Error handling
```

#### B. Automatic Code Review (if available)
1. In Copilot Chat, type:
```
@workspace /review
```
2. Review suggestions from Copilot

#### C. Full-Project Context Review
1. Ask Copilot:
```
@workspace Perform a comprehensive code review of the entire API.
Focus on:
- Architecture patterns
- Consistency across modules
- Error handling strategy
- Test coverage gaps
```

#### D. Addressing Review Comments
1. For any issues found, ask:
```
How should I fix [specific issue]? Show me the corrected code.
```

**Expected Outcome:** List of improvements applied based on code review

---

## Part 3: Custom Agents and Skills (40 minutes)

### Exercise 3.1: Create Custom Agent (20 min)

**Task:** Create specialized agents for steel calculations from scratch

1. **Create steel-expert.agent.md** in `.github/copilot/agents/`

Ask Copilot to help you structure it:
```
I want to create a custom GitHub Copilot agent for steel manufacturing expertise.
Create an agent file called steel-expert.agent.md that:
- Specializes in steel grades, calculations, and specifications
- Has access to read_file and semantic_search tools
- Knows about ASTM and EN standards
- Can perform weight and dimension calculations
- Uses gpt-4 model
```

2. **Test your steel-expert agent:**
   - Open Copilot Chat
   - Type: `@steel-expert what's the weight of a 304 stainless steel sheet 2400x1200x6mm?`

3. **Create inventory-manager.agent.md** with handoffs:

Ask Copilot:
```
Create an inventory-manager.agent.md that:
- Manages inventory operations
- Delegates calculations to @steel-expert using handoffs
- Has access to read_file, semantic_search, and grep_search
```

4. **Test handoff between agents:**
```
@inventory-manager I need to add a new product: A36 plate, 3000x1500x10mm, qty 50. 
What's its weight?
```

5. **Create quality-inspector.agent.md** for quality control:

```markdown
---
name: quality-inspector
description: Inspects steel products for defects and compliance
tools:
  - read_file
  - semantic_search
model: gpt-4
---

You are a quality control specialist for steel manufacturing.

Your responsibilities:
- Inspect products for dimensional accuracy
- Verify material properties
- Check compliance with specifications
- Recommend corrective actions

Use precise measurements and cite quality standards (ASTM, ISO).
```

5. Test your new agent:
```
@quality-inspector Check if a steel sheet with thickness 5.8mm meets the specification of 6mm ±0.3mm
```

**Expected Outcome:**
- Custom agents responding appropriately
- Handoff working between agents
- Specialized responses based on agent context

---

### Exercise 3.2: Create Agent Skills (20 min)

**Task:** Create portable skills following the agentskills.io standard from scratch

1. **Create steel-calculations.skill** in `skills/steel-calculations.skill/SKILL.md`

Ask Copilot:
```
I want to create an agent skill following the agentskills.io standard.
Create a SKILL.md file for steel-calculations that:
- Has proper YAML frontmatter (name, description, author, version, agentSkillsVersion: 0.1.0)
- Performs weight, volume, and area calculations
- Supports different steel shapes (sheet, coil, bar, tube)
- Includes usage examples
- References the functions in app/utils/steel_utils.py
```

2. **Test the steel-calculations skill:**
```
@workspace Use the steel-calculations skill to calculate weight of a sheet:
2400mm x 1200mm x 6mm, A36 steel
```

3. **Create inventory-optimization.skill** in `skills/inventory-optimization.skill/SKILL.md`:

```markdown
---
name: inventory-optimization
description: Optimize inventory levels and reorder points
author: BlueScope Training Team
version: 1.0.0
agentSkillsVersion: 0.1.0
---

# Inventory Optimization Skill

Provides recommendations for optimal inventory management.

## Capabilities

- Calculate reorder points
- Suggest optimal stock levels
- Identify slow-moving inventory
- Forecast demand

## Usage

Invoke when:
- Planning inventory levels
- Analyzing stock turnover
- Optimizing warehouse space

## Examples

```
Calculate reorder point for:
- Product: STL-001
- Lead time: 7 days
- Daily usage: 5 units
- Safety stock: 20 units
```

## Formula

Reorder Point = (Lead Time × Daily Usage) + Safety Stock
```

4. **Create advanced skill** in `skills/advanced/metallurgy-analysis.skill/SKILL.md`

This demonstrates three-level progressive loading:
```
Create an advanced metallurgy-analysis skill that:
- Analyzes material properties
- Provides heat treatment recommendations
- Lives in the advanced/ subdirectory for on-demand loading
```

5. **Update skills/README.md** to document all skills:
```markdown
# Available Skills

## Core Skills (Always Available)
- steel-calculations: Weight and dimension calculations
- inventory-optimization: Inventory level optimization

## Advanced Skills (Load on demand)
- metallurgy-analysis: Material property analysis
```

6. **Test the new skill:**
```
@workspace Use the inventory-optimization skill to calculate reorder point:
lead time 7 days, daily usage 10 units, safety stock 50 units
```

**Expected Outcome:**
- Skill properly structured
- Progressive loading working
- Portable across VS Code, CLI, Cloud

---

## Part 4: Copilot Memory and Diagnostics (25 minutes)

### Exercise 4.1: Use Copilot Memory (10 min)

**Task:** Store and retrieve BlueScope-specific standards

1. Open Copilot Chat and teach it BlueScope standards:
```
Remember: BlueScope uses the following standard locations:
- Warehouse-A: Hot-rolled products
- Warehouse-B: Cold-rolled and coated products
- Warehouse-C: Long products (bars, tubes)

Remember: Minimum stock levels by shape:
- Sheets: 100 units
- Coils: 50 units
- Plates: 75 units
- Bars: 200 units
- Tubes: 150 units

Remember: Our quality grades:
- Premium: aerospace, automotive
- Standard: construction, general manufacturing
- Economy: non-critical applications
```

2. Test memory recall:
```
What's the standard minimum stock level for sheets?
```

```
Where should I store hot-rolled coils?
```

3. Use memory in code generation:
```
Update the SteelProduct model to include quality_grade and set appropriate defaults based on what you remember
```

**Expected Outcome:**
- Copilot recalls BlueScope-specific information
- Suggestions align with stored preferences
- Memory persists across chat sessions

---

### Exercise 4.2: Use /create-agent and /create-skill (5 min)

1. Create an agent using the quick command:
```
/create-agent name=shipping-coordinator description="Coordinates shipping and logistics for steel products" tools=read_file,grep_search
```

2. Create a skill using the quick command:
```
/create-skill name=weight-distribution description="Calculates optimal weight distribution for shipping" author="BlueScope Logistics"
```

3. Review and customize the generated files

**Expected Outcome:**
- Agent and skill files created with proper structure
- Ready to customize further

---

### Exercise 4.3: Verify with Diagnostics View (10 min)

**Task:** Ensure all customizations are properly configured

1. Open Command Palette (`Ctrl+Shift+P`)
2. Search: "GitHub Copilot: Show Diagnostics"
3. Review:
   - Are all agents recognized?
   - Are skills loading properly?
   - Any configuration warnings?

4. Open Chat Customizations Editor:
   - Command Palette → "GitHub Copilot: Edit Chat Customizations"
   - Review agent configurations
   - Test agent invocation

5. Check progressive loading:
```
@workspace Show me all available skills and their loading status
```

6. Debug any issues:
   - Check YAML frontmatter syntax
   - Verify file paths
   - Ensure proper indentation

**Expected Outcome:**
- All agents showing as active
- Skills properly loaded
- No warnings or errors in diagnostics

---

## Final Challenge: Integrate Everything (15 minutes)

### Comprehensive Task

Implement a batch processing feature using ALL techniques learned:

1. **Test-First:** Write tests for batch operations
2. **Decomposition:** Break down the implementation into steps
3. **Custom Agent:** Use @steel-expert for validations
4. **Skill:** Use steel-calculations skill
5. **Memory:** Leverage stored minimum stock levels
6. **PR Workflow:** Create branch, commit with Copilot messages, generate PR summary
7. **Code Review:** Run full workspace review

**Feature Requirements:**
- Endpoint: `POST /inventory/batch`
- Accept array of product updates
- Validate each product using @steel-expert
- Calculate total weight using skill
- Check against stored minimum levels
- Return summary report

**Steps:**

1. Create feature branch:
```bash
git checkout -b feature/batch-processing
```

2. Ask Copilot to write tests first:
```
Using TDD, write comprehensive tests for a batch processing endpoint that:
- Accepts an array of product updates (quantity and location changes)
- Validates all products exist
- Returns success/failure for each operation
- Calculates total weight of all updated products
```

3. Implement the feature with Copilot's help, using decomposition:
```
Let's implement the batch processing endpoint step by step:
1. First, create the request/response models
2. Then, implement the batch update logic in database.py
3. Finally, create the /inventory/batch endpoint in routers/inventory.py
```

4. Use @steel-expert to add validation:
```
@steel-expert Review the batch processing logic and add validation for:
- Product dimensions
- Steel grades
- Quantity limits
```

5. Generate commit and PR:
```bash
git add .
# Use Copilot for commit message
git commit
```

**Time to Complete:** 15 minutes

---

## Lab Completion Checklist

### Skills Demonstrated
- [x] Decomposition prompting
- [x] Test-first development
- [x] Refactor-first patterns
- [x] Multi-turn refinement
- [x] PR summary generation
- [x] Semantic commit messages
- [x] Multiple code review  (4 bugs)
2. ✅ Added grade search feature using TDD
3. ✅ Completed weight calculations for all shapes
4. ✅ Implemented low stock alerts feature
5. ✅ Created steel-expert.agent.md
6. ✅ Created inventory-manager.agent.md with handoffs
7. ✅ Created quality-inspector.agent.md
8. ✅ Created steel-calculations.skill
9. ✅ Created inventory-optimization.skill
10. ✅ Created advanced metallurgy-analysis skill
11. ✅ Configured Copilot Memory with BlueScope standards
12
### Deliverables
1. ✅ Fixed all starter bugs
2. ✅ Added grade search feature (TDD)
3. ✅ Completed weight calculations for all shapes
4. ✅ Implemented low stock alerts
5. ✅ Tested steel-expert and inventory-manager agents
6. ✅ Created custom quality-inspector agent
7. ✅ Created inventory-optimization skill
8. ✅ Configured Copilot Memory with standards
9. ✅ Batch processing feature (final challenge)

---

## Troubleshooting Guide

### Copilot Not Responding
- Check license activation
- Restart VS Code
- Clear Copilot cache: Command Palette → "Reload Window"

### Agents Not Working
- Verify file path: `.github/copilot/agents/`
- Check YAML frontmatter syntax (must start with `---`)
- Review Diagnostics view
- Ensure proper agent naming (lowercase, hyphens)

### Skills Not Loading
- Confirm SKILL.md naming (must be exactly `SKILL.md`)
- Check agentSkills.io version compatibility
- Verify progressive loading structure
- Ensure YAML frontmatter is valid

### Memory Not Persisting
- Memory feature requires Copilot subscription
- Check if preview feature is enabled in VS Code settings
- Try explicit "Remember:" prefix
- Memory may take a few seconds to persist

### Python Environment Issues
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### API Not Starting
```bash
# Check for port conflicts
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Try different port
uvicorn app.main:app --reload --port 8001
```

---

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [AgentSkills.io Standard](https://agentskills.io)
- [Copilot Best Practices](https://github.blog/copilot-tips)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)

---

## Post-Lab Survey

After completing the lab, please provide feedback on:

1. **Clarity of Instructions** (1-5): _____
2. **Appropriate Difficulty Level** (1-5): _____
3. **Time Allocation** (Too short / Just right / Too long)
4. **Most Valuable Exercise:** _________________
5. **Areas Needing Improvement:** _________________
6. **Would you recommend this lab?** (Yes / No / Maybe)

### Open Feedback
```
[Your feedback here]
```

---

## Appendix: Quick Reference

### Copilot Chat Commands
- `@workspace` - Query entire workspace
- `@steel-expert` - Invoke custom agent
- `/create-agent` - Quick agent creation
- `/create-skill` - Quick skill creation
- `/review` - Code review mode

### Git Commands
```bash
git checkout -b feature/name    # Create branch
git add .                       # Stage changes
git commit                      # Commit (use Copilot for message)
git push origin feature/name    # Push branch
```

### Pytest Commands
```bash
pytest                          # Run all tests
pytest tests/test_inventory.py  # Run specific file
pytest -v                       # Verbose output
pytest -k "test_name"          # Run specific test
```

### API Testing
```bash
# Health check
curl http://localhost:8000/health

# Get all products
curl http://localhost:8000/inventory/

# Create product
curl -X POST http://localhost:8000/inventory/ \
  -H "Content-Type: application/json" \
  -d '{"product_code":"TEST-001","grade":"A36","shape":"sheet","length_mm":2400,"width_mm":1200,"thickness_mm":6.0,"quantity":100,"location":"Warehouse-A"}'
```

---

**Lab Version:** 1.0  
**Last Updated:** May 2026  
**Instructor Contact:** [Your contact information]

---

## License

This lab material is proprietary to BlueScope and is for training purposes only.
