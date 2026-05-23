# ux-skills

Claude Code skills for UX design work.

Each skill lives in its own subdirectory with a `SKILL.md`.
Install any skill via the Claude Code skill installer.

---

## Skills

### 🗂️ 入口 / 調度

| Skill | What it does |
|-------|-------------|
| [product-ux-advisor](./product-ux-advisor/) | 產品開發全流程的 UIUX 一站式入口——智慧調度下方六個專業 skill，並提供：Full Review（完整設計審查）、Phase Guide（Discovery→Launch 各階段交付物）、Handoff Checklist（14 項交付前檢核）、競品 UX 比較框架（七維度） |

### 🔬 專業審查

| Skill | What it does |
|-------|-------------|
| [heuristic-audit](./heuristic-audit/) | 根據 Nielsen 十大啟發式原則 + 格式塔心理學 + Shneiderman 八大法則審查設計稿，輸出 P = S + F + B 嚴重性評分報告與優先修復清單 |
| [cognitive-load-audit](./cognitive-load-audit/) | 根據 Miller's Law（7±2）、Fitts's Law 與工作記憶理論評估單一畫面資訊複雜度，量化組塊數並分析視覺掃描路徑 |
| [flow-friction-analyzer](./flow-friction-analyzer/) | 分析跨畫面任務路徑，依 EAS 框架（Eliminate / Automate / Simplify）找出點擊成本、工作記憶負擔、Hick's Law 決策點與錯誤恢復死路 |
| [edge-case-state-mapper](./edge-case-state-mapper/) | 輸入 Happy Path 描述，自動推導遺漏的 UI 狀態（Empty / Loading / Error / Validation / Partial Data / Business Rule），並輸出帶優先級與文案建議的結構化清單 |
| [a11y-consultant](./a11y-consultant/) | 依 WCAG 2.2 AA/AAA 分兩階段審查：① 設計稿（對比度、色盲模擬、觸控目標 44px）② 程式碼（語意化 HTML、aria、Tab 順序、焦點管理） |
| [ux-writing](./ux-writing/) | Write and review UI microcopy — buttons, errors, labels, dialogs, notifications — following a strict rule set (sentence case, no "Please", Permanently delete, etc.) |

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
