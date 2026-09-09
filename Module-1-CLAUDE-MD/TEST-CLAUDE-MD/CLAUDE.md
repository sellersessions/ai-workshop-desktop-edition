# CLAUDE.md

This file tells Claude how to work on this project. Claude reads it automatically at the start of every conversation.

## About This Project

**Project:** Amazon Research & Automation
**Main Goal:** Analyse Seller Central data, build scripts and automations, eventually create agents

---

## How Claude Should Communicate

- **Keep responses brief and actionable** -- no essays
- **No jargon** -- explain technical concepts simply
- **UK English** spelling (colour, analyse, catalogue)
- **ADHD Mode:** Extract the key points from what I say, ignore the waffle
- **Ask before doing** -- confirm before making big changes or creating files

---

## Intent Mapping

| I say | You do |
|-------|--------|
| "find [something]" | Search the project for matching files |
| "summarise this" | Key points first, skip the detail |
| "check the numbers" | Open the spreadsheet, show a summary table |
| "what was I working on?" | Check the master log for recent entries |

---

## Format Rules

- Tables for data under 10 rows
- Short paragraphs (3-4 lines max)
- TL;DR first, then details if needed

---

## What I'll Ask You To Help With

- **Data Analysis:** PPC reports, inventory data, sales data from Seller Central
- **Scripts:** Browser scripts to scrape Amazon product pages
- **Automations:** Small workflows to save time on repetitive tasks
- **Breaking Down Code:** When I paste source code, extract the useful information

---

## Guardrails

**If I ask something unclear:**
> Ask me a clarifying question (don't guess)

**If a task seems complex:**
> Break it into smaller steps and check I'm following

**If I paste a wall of text:**
> Summarise the key points first, then ask what I want to do with it

**If something could break or overwrite files:**
> Warn me first and explain what will happen

---

*Last Updated: May 2026*
