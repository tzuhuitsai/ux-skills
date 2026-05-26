# ux-skills

Claude Code skills for UX design work.

## Structure

Skills are organised into two categories. Skills that don't belong to either category can live at the top level (`skill-name/SKILL.md`).

```
ux-skills/
├── ui/                          # UI design & implementation
│   ├── product-ui-advisor/
│   └── ...
├── ux/                          # UX research & analysis
│   ├── product-ux-advisor/
│   └── ...
└── standalone-skill/            # no category (flat)
```

## Install

```bash
./install.sh
```

Copies all skills to `~/.claude/skills/`, supporting both categorised and flat layouts.

---

## Skills

### ui/ — UI Design & Implementation

| Skill | What it does |
|-------|-------------|
| [product-ui-advisor](./ui/product-ui-advisor/) | UI 層面一站式入口——調度八個 UI/DS skill，提供：Full UI Review、UI Phase Guide（Explore→Handoff）、UI Handoff Checklist（12 項）、Prototype-First Workflow Guide（含 Token Contract 模板）|
| [visual-hierarchy-checker](./ui/visual-hierarchy-checker/) | 診斷設計稿的視覺層級：CTA 突出度、字型層級系統、色彩使用、空間分組、元素視覺重量，輸出三色燈號優先修正清單 |
| [interaction-pattern-advisor](./ui/interaction-pattern-advisor/) | 推薦最合適的 UI 互動模式（Switch vs Checkbox、Modal vs Drawer、Toast vs Banner 等），並說明選擇理由與放棄其他選項的原因 |
| [component-state-specifier](./ui/component-state-specifier/) | 輸入一個原子元件（Button、Input、Toggle 等），輸出所有必備視覺狀態的完整規格（Default/Hover/Focus/Active/Disabled/Loading）含 Token 對應、CSS transition 與 ARIA |
| [responsive-layout-stress-tester](./ui/responsive-layout-stress-tester/) | 模擬設計稿在 1920/1440/1280/1024/768px 下的版面行為，找出 Auto Layout 失效點、表格水平溢出、側邊欄收合策略 |
| [data-density-optimizer](./ui/data-density-optimizer/) | 評估 B2B SaaS 後台資訊密度，診斷白空間浪費或資訊過載，給出截斷 vs 折行決策、行高規格（Compact/Default/Comfortable/Dense）與極限資料情境測試 |
| [design-system-manager](./ui/design-system-manager/) | 四合一設計系統工具：① audit ② document ③ extend ④ validate Token Contract |
| [visual-consistency-checker](./ui/visual-consistency-checker/) | 多張截圖輸入，不需要 Figma，找出跨頁面視覺語言不一致：字型層級、色彩語意、元件外觀、間距節奏、互動模式 |
| [design-handoff](./ui/design-handoff/) | 整合所有前置 skill 產出，編譯成工程師可直接實作的交付文件（佈局規格、Token 清單、元件 Props、Edge Cases、響應式行為、動畫、無障礙） |

### ux/ — UX Research & Analysis

| Skill | What it does |
|-------|-------------|
| [product-ux-advisor](./ux/product-ux-advisor/) | UX 層面一站式入口——調度六個 UX skill，提供：Full UX Review、Phase Guide（Discovery→Launch）、Handoff Checklist（14 項）、競品 UX 比較框架（七維度） |
| [heuristic-audit](./ux/heuristic-audit/) | 根據 Nielsen 十大啟發式原則 + 格式塔心理學 + Shneiderman 八大法則審查設計稿，輸出 P = S + F + B 嚴重性評分報告與優先修復清單 |
| [cognitive-load-audit](./ux/cognitive-load-audit/) | 根據 Miller's Law（7±2）、Fitts's Law 與工作記憶理論評估單一畫面資訊複雜度，量化組塊數並分析視覺掃描路徑 |
| [flow-friction-analyzer](./ux/flow-friction-analyzer/) | 分析跨畫面任務路徑，依 EAS 框架（Eliminate / Automate / Simplify）找出點擊成本、工作記憶負擔、Hick's Law 決策點與錯誤恢復死路 |
| [edge-case-state-mapper](./ux/edge-case-state-mapper/) | 輸入 Happy Path 描述，自動推導遺漏的 UI 狀態（Empty / Loading / Error / Validation / Partial Data / Business Rule），並輸出帶優先級與文案建議的結構化清單 |
| [a11y-consultant](./ux/a11y-consultant/) | 依 WCAG 2.2 AA/AAA 分兩階段審查：① 設計稿（對比度、色盲模擬、觸控目標 44px）② 程式碼（語意化 HTML、aria、Tab 順序、焦點管理） |
| [ux-writing](./ux/ux-writing/) | Write and review UI microcopy — buttons, errors, labels, dialogs, notifications — following a strict rule set (sentence case, no "Please", Permanently delete, etc.) |

---

## Adding a new skill

**Categorised skill** (belongs to `ui/` or `ux/`):
```bash
mkdir ui/<skill-name>   # or ux/<skill-name>
# add SKILL.md inside
```

**Standalone skill** (no category):
```bash
mkdir <skill-name>
# add SKILL.md inside
```

Then run `./install.sh` to sync to `~/.claude/skills/`.

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
| visual-consistency-checker | 100/100 | — | eval v1 |
| product-ui-advisor | 100/100 | — | eval v1 |
