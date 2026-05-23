# ux-skills

Claude Code skills for UX design work.

Each skill lives in its own subdirectory with a `SKILL.md`.
Install any skill via the Claude Code skill installer.

---

## Skills

| Skill | What it does |
|-------|-------------|
| [ux-writing](./ux-writing/) | Write and review UI microcopy — buttons, errors, labels, dialogs, notifications — following a strict rule set (sentence case, no "Please", Permanently delete, etc.) |
| [edge-case-state-mapper](./edge-case-state-mapper/) | 輸入 Happy Path 描述，自動推導遺漏的 UI 狀態（Empty / Loading / Error / Validation / Partial Data / Business Rule），並輸出帶優先級與文案建議的結構化清單 |
| [a11y-consultant](./a11y-consultant/) | 依 WCAG 2.2 AA/AAA 分兩階段審查：① 設計稿（對比度、色盲模擬、觸控目標 44px）② 程式碼（語意化 HTML、aria、Tab 順序、焦點管理） |

---

## Adding a new skill

1. Create a new subdirectory: `mkdir <skill-name>`
2. Add a `SKILL.md` following the [Claude skill format](https://docs.anthropic.com/en/docs/claude-code/skills)
3. Package with `python -m scripts.package_skill ./<skill-name>`
4. Commit and push

---

## Eval results

| Skill | With skill | Baseline | Gap |
|-------|-----------|---------|-----|
| ux-writing | 93.8% | 59.4% | +34pp |
