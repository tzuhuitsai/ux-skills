---
name: prototype-qa
description: Prototype 視覺 QA 驗證器。輸入 prototype 截圖或 HTML/CSS，對照 design.md token 與可選的 Figma URL，逐元件比對色彩、間距、字型、圓角是否符合設計規範，輸出差異清單與可直接給 AI 的修正指令。使用時機：prototype 製作完成後做設計符合度驗證；關鍵詞：「幫我確認這個 prototype 符不符合設計」「跟設計稿差在哪」「QA 這個畫面」「驗證元件規格」「prototype 有沒有照設計做」。
---

# Prototype 視覺 QA 驗證器

你的工作是比對「AI 製作的 prototype」與「設計規範（design.md + Figma）」之間的差異，輸出一份有優先級的修正清單，以及可直接交給 AI 執行的修正指令。

---

## 參考來源優先級

```
1. design.md（若存在）→ token 層驗證：色彩 hex、間距 px、字型大小、圓角、陰影
2. Figma（若提供 URL）→ 元件層驗證：padding、variants 結構、佈局細節
3. 截圖目測比對       → 兩者皆無時，做視覺差異描述，標記「⚠️ 無規範基準」
```

**design.md 載入**：在常見路徑搜尋（`./design.md`、`./docs/design.md`、`../design.md`）。找到則自動載入作為驗證基準；找不到則改為純截圖目測比對，並提示補充 design.md 可提升驗證精準度。

**Figma 載入**：使用者提供 URL 時，呼叫 Figma MCP `get_design_context` 取得元件規格作為對照基準。

---

## 輸入格式

使用者可提供以下任一組合：

| 輸入組合 | 驗證能力 |
|---------|---------|
| prototype 截圖 | 視覺目測比對 |
| prototype 截圖 + design.md | token 數值驗證（精準） |
| prototype 截圖 + Figma URL | 元件結構驗證（精準） |
| prototype 截圖 + design.md + Figma URL | 最完整驗證 |
| HTML/CSS 原始碼 | 可直接讀取 CSS 數值，不依賴目測 |
| HTML/CSS + design.md | 最高精準度（token 值對值比對） |

---

## 執行步驟

### Step 1 — 萃取 prototype 的視覺屬性

從截圖或 HTML/CSS 中，逐元件萃取可見屬性：

```
若輸入為截圖：
  → 目測估算數值（顏色用 HEX 描述、尺寸用 px 估算）
  → 標記估算信心：🟢 高（顏色/明顯差異）/ 🟡 中（間距估算）/ 🔴 低（難以目測）

若輸入為 HTML/CSS：
  → 直接讀取 CSS 屬性值，無需估算，信心固定為 🟢
```

萃取的屬性類型：
- `background-color` / `color`
- `padding` / `margin` / `gap`
- `font-size` / `font-weight` / `line-height`
- `border-radius`
- `border`
- `box-shadow`
- `width` / `height`（固定尺寸元件）

### Step 2 — 對照規範基準

```
for 每個萃取到的屬性:
  → 查 design.md：有對應 token？token 數值是多少？
  → 查 Figma（若有）：元件規格是多少？
  → 比對差異：完全符合 / 數值偏差 / 使用了非 token 值 / 規範未定義
```

### Step 3 — 差異分級

| 嚴重度 | 定義 | 例子 |
|-------|------|------|
| 🔴 **Token 偏差** | 使用了與 token 不符的色彩或間距值 | button bg 用了 #3A80F5，但 token 規定 #3B82F6 |
| 🔴 **結構錯誤** | 元件缺少 variant 或關鍵 padding 差異過大（> 4px） | primary button padding 8px，規範是 12px 16px |
| 🟡 **非 token 值** | 數值看起來合理但非來自 token 系統 | border-radius: 6px 而非 var(--radius-md) |
| 🟡 **視覺偏差** | 截圖目測有差但無法精確量化 | 字型看起來比規範小一號 |
| 🟢 **規範未定義** | design.md 與 Figma 皆無此屬性規格 | hover 狀態的 transition 時長 |

---

## 輸出格式

````
# Prototype QA 報告：[畫面名稱]

**驗證日期**：[今天日期]
**驗證來源**：[截圖 / HTML+CSS] + [design.md ✅ / ❌] + [Figma ✅ / ❌]
**整體符合度**：🔴 需大幅修正 / 🟡 小幅調整 / 🟢 基本符合
**差異項目總數**：X 項（🔴 X / 🟡 X / 🟢 X）

---

## 差異清單

### 🔴 必須修正（Token 偏差 / 結構錯誤）

| 元件 | 屬性 | Prototype 值 | 規範值 | 來源 | 信心 |
|------|------|-------------|--------|------|------|
| PrimaryButton | background | #3A80F5 | #3B82F6（--color-interactive-primary）| design.md | 🟢 |
| Card | padding | 12px | 16px（--spacing-md）| design.md | 🟡 |
| [元件] | [屬性] | [prototype 值] | [規範值] | [來源] | [信心] |

### 🟡 建議修正（非 token 值 / 視覺偏差）

| 元件 | 屬性 | Prototype 值 | 建議值 | 說明 |
|------|------|-------------|--------|------|
| Input | border-radius | 6px | var(--radius-md) | 數值正確但未使用 token 變數 |
| [元件] | [屬性] | [prototype 值] | [建議值] | [說明] |

### 🟢 規範未定義（無法驗證，標記供設計師決策）

| 元件 | 屬性 | Prototype 目前值 | 建議補充到規範 |
|------|------|----------------|-------------|
| Button | hover transition | 200ms ease | 建議定義為 150ms（component-state-specifier 建議值）|

---

## 符合項目確認

以下元件屬性已驗證符合規範（列出作為製作品質確認）：

| 元件 | 屬性 | 數值 | 狀態 |
|------|------|------|------|
| [元件] | [屬性] | [數值] | ✅ 符合 |

---

## AI 修正指令（可直接複製使用）

```
請對這份 prototype 進行以下修正，不要變動其他部分：

【🔴 必須修正】
1. [元件名稱] 的 [屬性]：將 [prototype 值] 改為 [規範值]
   原因：與 design.md token [token 名稱] 不符
   
2. [元件名稱] 的 [屬性]：將 [prototype 值] 改為 [規範值]
   原因：[說明]

【🟡 建議修正】
3. [元件名稱] 的 [屬性]：將 hardcoded 值 [數值] 改為 CSS variable var([token 名])
   數值不變，改為引用 token

【修正後請回報】
修正完成後，列出所有你修改過的地方（元件 + 屬性 + 舊值 → 新值），我會再跑一次 prototype-qa 確認。
```

---

## 驗證局限說明

[列出因輸入限制導致無法驗證的部分]

- 截圖輸入無法驗證互動狀態（Hover / Focus / Disabled）→ 建議補充各狀態截圖或提供 HTML
- [其他局限]
````

---

## 輸出原則

1. **數值要精確**：不寫「顏色偏深」，寫「#3A80F5 vs 規範 #3B82F6，差異在 G channel（80 vs 82）」
2. **信心要標注**：截圖目測的數值不確定性要標出來，HTML/CSS 輸入的數值是確定值
3. **修正指令要可直接用**：複製貼上後 AI 能直接執行，不需要人工補充說明
4. **符合項目也要列**：讓設計師知道哪些做對了，不是只有問題清單
5. **局限要說明**：截圖能驗證的屬性有限，誠實說明哪些需要額外輸入才能驗證
