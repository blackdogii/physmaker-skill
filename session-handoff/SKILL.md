---
name: session-handoff
description: Write a short handoff note so the next work session on this project can pick up immediately without re-explaining context. Use when the user says they're wrapping up, stopping for now, done for today, or asks "how do I hand this off / pick this back up next time" — for any project, not tied to any particular knowledge base. Also use mid-session when the user says to jot down / note down / remember a specific finding so it survives to next time.
---

# Session Handoff

A lightweight, project-local version of "distill and hand off" — no shared knowledge base, no classification taxonomy, no cross-project index. Everything lives in one file inside the project itself, so anyone who opens the project (including a different person, or the same person a week later) can read one file and know exactly where things stand.

## Where it writes

1. **Check the project first.** If it already has an obvious continuity file (e.g. `docs/HANDOFF.md`, `docs/PROGRESS.md`, `docs/upgrades/` from `game-upgrade`, or something a README points at), use that instead of inventing a new one — don't create a second, competing place to look.
2. **Otherwise, default to `docs/HANDOFF.md`** in the project root. Create `docs/` if it doesn't exist.
3. **If the user has told you to use a different path** (a specific file, a different knowledge base, a shared vault), remember that for the rest of this project and use it every time — don't ask again once it's been said.

## Full handoff (wrapping up / done for now / 收工)

Add a new entry at the **top** of the file (newest first, so opening the file always shows current state without scrolling). Each entry:

```markdown
## YYYY-MM-DD HH:mm

### 今天完成
...

### 尚未完成
...

### 下一步
...

### 注意事項
...
```

- Write the actual local date/time, not a placeholder.
- Every section is required even when empty — write **無** rather than omitting it. A missing section reads as "forgot to check," not "nothing there."
- **今天完成**: what was actually finished and verified this session — not a blow-by-blow of every action taken, just the outcomes and any decisions made along the way.
- **尚未完成**: what's still in progress, waiting on something, or was deliberately left for later.
- **下一步**: the single most useful thing to do first next time; if there's more than one candidate, order them.
- **注意事項**: anything that would cause wasted time if forgotten — a gotcha hit, a constraint, a "don't do X" lesson, required setup, where a specific file/tool lives.
- If the project already has a `docs/upgrades/upgrade-NNN.md` from `game-upgrade` covering the same session, don't duplicate its full content — write a short entry here and link to it (`see docs/upgrades/upgrade-003.md`) instead of copying details across two files.

## Quick note (mid-session, not wrapping up yet)

When the user just says "note this down" / "remember this" without a full wrap-up, don't create a whole new dated entry — append a bullet to the **注意事項** section of the current open entry (the most recent one, if it's from this same session) instead of forcing the full four-section ritual for one line.

## What this deliberately doesn't do

- No classification into topics/categories, no dedup search across old entries, no separate index file. If that level of knowledge management is actually needed, that's a different, heavier job (a personal knowledge-base skill), not this one.
- No assumption of a specific tool (Claude Code vs. Codex vs. anything else) or a specific shared vault — this works for a single person's single project with zero setup.
