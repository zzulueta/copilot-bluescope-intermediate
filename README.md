# GitHub Copilot Intermediate Course

A comprehensive 2-hour hands-on lab for learning intermediate GitHub Copilot features using a Steel Inventory Management API.

## 📚 Course Overview

This course teaches intermediate GitHub Copilot capabilities through practical exercises:

### Learning Objectives
- ✅ Advanced prompting patterns (decomposition, test-first, refactor-first)
- ✅ GitHub workflow integration (PR summaries, commit messages, code reviews)
- ✅ Custom agent authoring (.agent.md)
- ✅ Agent skills (SKILL.md) following agentskills.io standard
- ✅ Copilot Memory for persistent context

## 🎯 What's Included

### `/steel-inventory-api/`
FastAPI-based Steel Inventory Management system with:
- **Intentional bugs** for debugging exercises
- **Incomplete features** for TDD practice
- **Basic test suite** to expand
- **Utility functions** to refactor
- **REST API** for CRUD operations

### `/LAB_INSTRUCTIONS.md`
Complete 2-hour lab guide with:
- **Part 1:** Advanced Prompting
- **Part 2:** GitHub Workflow
- **Part 3:** Custom Agents & Skills
- **Part 4:** Memory
- **Final Challenge:** Integration exercise

## 🚀 Quick Start

Follow the complete instructions in `LAB_INSTRUCTIONS.md`

## 📋 Prerequisites

- GitHub Copilot license
- VS Code with GitHub Copilot extensions
- Python 3.9+
- Git
- Basic FastAPI/Python knowledge

## 🏗️ Project Structure

```
bluescope/
├── LAB_INSTRUCTIONS.md          # Complete lab guide
├── steel-inventory-api/         # Starter project
│   ├── app/
│   │   ├── main.py             # FastAPI app
│   │   ├── models.py           # Pydantic models
│   │   ├── database.py         # In-memory DB (with bugs)
│   │   ├── routers/
│   │   │   ├── inventory.py   # CRUD endpoints
│   │   │   └── calculations.py
│   │   └── utils/
│   │       └── steel_utils.py  # Utility functions
│   ├── tests/
│   │   └── test_inventory.py  # Basic tests
│   ├── requirements.txt
│   └── README.md
```

## 🐛 Known Issues (By Design)

The starter code contains intentional issues for learning:
1. Duplicate product code validation missing
2. `last_updated` timestamp not updating on changes
3. Negative quantities accepted in updates
4. `calculate_area_m2()` crashes on None width
5. Weight calculations incomplete for coil/bar/tube shapes
6. Missing test coverage

Participants will fix these using Copilot's features!

## 🎓 Key Topics Covered

### Advanced Prompting
- Decomposition for complex problems
- Test-driven development (TDD)
- Refactor-first approach
- Multi-turn refinement

### GitHub Integration
- PR summary generation
- Semantic commit messages
- Code review modes (manual, automatic, agentic)

### Customization
- Custom agents with tool restrictions
- Declarative agent handoffs
- Agent skills (agentskills.io)
- Progressive skill loading

### Memory
- Persistent memory across sessions

## 📖 Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [AgentSkills.io Standard](https://agentskills.io)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 📝 License

This course material is for training purposes.

## 🤝 Contributing

This is a training repository. For improvements or suggestions, please open an issue.

## ⏱️ Lab Duration

**Total:** 2 hours
- Setup: 15 minutes (pre-lab)
- Exercises: 120 minutes
- Q&A: 15 minutes (post-lab)

## 🎯 Expected Outcomes

By the end of this lab, participants will:
- Fix bugs using decomposition
- Implement features using TDD
- Create custom agents
- Author agent skills
- Configure Copilot Memory
- Complete a full-stack integration challenge

---
