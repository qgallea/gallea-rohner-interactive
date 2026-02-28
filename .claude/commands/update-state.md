# /update-state

Update the project progress tracker after completing a task.

## Usage
```
/update-state
```

## Process
1. Read `.planning/state.md`
2. Assess what has changed since last update:
   - Check `data/` for new JSON files
   - Check `site/components/` for new components
   - Check `code_build/` for new notebooks
3. Update the status tables (🔴 → 🟡 → 🟢)
4. Log any decisions made in the "Decisions Made" section
5. Update "Last updated" timestamp
6. Note any blocking issues

## Status Legend
- 🔴 Not started
- 🟡 In progress
- 🟢 Complete
- 🔵 Needs revision
