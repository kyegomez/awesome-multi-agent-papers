# Contributing to Awesome Multi-Agent Papers

Thank you for helping grow this collection! This guide will help you submit papers that match the list's format and land in the right section.

## What Qualifies

This list is for **multi-agent** research—papers where multiple AI/LLM agents collaborate, debate, compete, orchestrate, or communicate. This includes:

- Multi-agent LLM collaboration and communication
- Multi-agent reinforcement learning
- Agent societies and social simulations
- Swarm intelligence
- Multi-agent frameworks and benchmarks
- Orchestration of multiple agents

**Single-agent papers do not qualify.** If a paper focuses on a single agent (even a capable one), it belongs elsewhere.

## Entry Format

Each entry follows this format:

```
- **[Paper Title](https://arxiv.org/abs/XXXX.XXXXX)**
```

**Example:**

```
- **[AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)**
```

### Link Preferences

1. **Prefer the arXiv abstract page** (`https://arxiv.org/abs/<id>`) over the PDF link (`https://arxiv.org/pdf/<id>.pdf`)
2. If no arXiv version exists, use the most stable link available (conference proceedings, official project page, Semantic Scholar, etc.)
3. Avoid URL shorteners or temporary links

### Optional Additions

You may append a GitHub link or brief note after the entry if relevant:

```
- **[Paper Title](https://arxiv.org/abs/XXXX.XXXXX)** [GitHub](https://github.com/org/repo)
```

## Choosing a Section

Place your paper in the most fitting **existing** section. Current sections:

- **Multi-Agent Collaboration & System Design** — Core multi-agent architectures, coordination, communication
- **Multi-Agent Frameworks & Benchmarks** — Platforms, evaluation benchmarks, toolkits
- **Application-Specific Multi-Agent Systems**
  - Software Engineering
  - Healthcare & Medical
  - Data & ML
  - Security
  - Multimodal
  - Other Domains
- **Evaluation & Model Improvement** — Judging, routing, ensemble methods
- **Social Simulation & Agent Societies** — Simulated worlds, emergent behavior
- **Workflow, Architecture & Agent Design** — Agentic workflows, system design patterns
- **Science** — Scientific discovery, research automation
- **Alignment** — Safety and alignment in multi-agent contexts
- **Reinforcement Learning** — Multi-agent RL specifically
- **Surveys** — Survey papers covering multi-agent topics
- **Finance** — Financial applications
- **Agents for Research** — Research automation
- **Training** — Training methods for multi-agent systems
- **Others** — Papers that don't fit elsewhere

If you believe a new section is needed, propose it in your PR description—don't create a new section in the README directly.

## Check for Duplicates

Before submitting, verify the paper isn't already listed or proposed:

1. **Search the README** for:
   - The arXiv ID (e.g., `2308.08155`)
   - Keywords from the paper title
2. **Check open PRs** for the same paper

## Keep PRs Focused

- Add one or a few related papers per PR
- Don't include unrelated README changes
- Don't reformat existing entries

## BibTeX Citations

The `src/arxiv_bibtex.bib` file contains BibTeX citations for papers in this list. You don't need to update it manually—a script (`src/arxiv-bibtex.py`) automatically extracts arXiv IDs from the README and generates BibTeX entries. Just add your paper to the README with an arXiv link, and the citation will be picked up on the next run.

## Questions?

Open an issue or join the [Discord](https://discord.gg/EamjgSaEQf) if you're unsure about anything. Thank you for contributing!
