# Agent Skills Directory

This directory is for your custom agent skills following the agentskills.io standard.

## During the Lab

You will create agent skills here as part of **Part 3, Exercise 3.2**.

## Skill Structure

Skills should follow this structure:
```
skills/
├── README.md (this file - Level 1: Always loaded)
├── your-skill.skill/
│   └── SKILL.md (Level 2: Loaded on demand)
└── advanced/
    └── advanced-skill.skill/
        └── SKILL.md (Level 3: Loaded when needed)
```

## Skill File Format

Each `SKILL.md` should have:
```markdown
---
name: skill-name
description: What the skill does
author: Your Name
version: 1.0.0
agentSkillsVersion: 0.1.0
---

# Skill Name

Detailed description...
```

## Skills You'll Create

- [ ] steel-calculations.skill/SKILL.md
- [ ] inventory-optimization.skill/SKILL.md
- [ ] advanced/metallurgy-analysis.skill/SKILL.md
- [ ] Additional skills as needed
