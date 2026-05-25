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
| [visual-hierarchy-checker](./visual-hierarchy-checker/) | 診斷設計稿的視覺層級：CTA 突出度、字型層級系統、色彩使用、空間分組、元素視覺重量，輸出三色燈號優先修正清單 |

### 📊 資料 & 設計系統

| Skill | What it does |
|-------|-------------|
| [data-density-optimizer](./data-density-optimizer/) | 評估 B2B SaaS 後台資訊密度，診斷白空間浪費或資訊過載，給出截斷 vs 折行決策、行高規格（Compact/Default/Comfortable/Dense）與極限資料情境測試 |
| [design-system-manager](./design-system-manager/) | 三合一設計系統工具：① audit — 掃描 hardcoded 值並給出 Token 替換建議 ② document — 輸出元件完整規格文件（Props、States、Token 映射、Do & Don't）③ extend — 規劃新元件加入設計系統 |

### 🎨 設計決策 & 元件

| Skill | What it does |
|-------|-------------|
| [interaction-pattern-advisor](./interaction-pattern-advisor/) | 推薦最合適的 UI 互動模式（Switch vs Checkbox、Modal vs Drawer、Toast vs Banner 等），並說明選擇理由與放棄其他選項的原因 |
| [component-state-specifier](./component-state-specifier/) | 輸入一個原子元件（Button、Input、Toggle 等），輸出所有必備視覺狀態的完整規格（Default/Hover/Focus/Active/Disabled/Loading）含 Token 對應、CSS transition 與 ARIA |

### 📦 交付

| Skill | What it does |
|-------|-------------|
| [responsive-layout-stress-tester](./responsive-layout-stress-tester/) | 模擬設計稿在 1920/1440/1280/1024/768px 下的版面行為，找出 Auto Layout 失效點、表格水平溢出、側邊欄收合策略 |
| [design-handoff](./design-handoff/) | 整合所有前置 skill 產出，編譯成工程師可直接實作的交付文件（佈局規格、Token 清單、元件 Props、Edge Cases、響應式行為、動畫、無障礙） |

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
| responsive-layout-stress-tester | 95/100 | — | eval v1 |
| interaction-pattern-advisor | 100/100 | — | eval v1 |
| design-handoff | 100/100 | — | eval v1 |
| component-state-specifier | 90/100 | — | eval v1 |
| visual-hierarchy-checker | 98/100 | — | eval v1 |
| data-density-optimizer | 90/100 | — | eval v1 |
| design-system-manager | 100/100 | — | eval v1 |
