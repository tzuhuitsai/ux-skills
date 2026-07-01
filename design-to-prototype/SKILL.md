---
name: design-to-prototype
description: 設計稿轉 Prototype 製作簡報。輸入設計截圖，自動從 design.md 提取 token 規格，可選填 Figma URL 補充元件細節，輸出結構化製作 spec 與 AI 製作 prompt，確保 AI 照設計製作而非自由發揮。使用時機：把設計稿交給 AI 製作 prototype 之前；關鍵詞：「幫我把這個畫面做成 prototype」「轉成 HTML」「AI 製作畫面」「生成 prototype」「製作這個設計」。
---

# 設計稿轉 Prototype 製作簡報

你的工作是在 AI 開始製作 prototype 之前，先把設計截圖轉換成一份結構化的「製作 spec」，讓 AI 有足夠的規格依據，而不是靠猜測或通用預設值製作。

---

## 參考來源優先級

```
1. design.md（若存在）→ token 層：色彩、間距、字型、圓角、陰影
2. Figma（若提供 URL）→ 元件層：padding、variants、佈局細節、狀態規格
3. 截圖目測推斷     → 兩者皆無時，標記為「⚠️ 推斷值，需確認」
```

**design.md 載入方式**：在常見路徑搜尋 `design.md`（`./design.md`、`./docs/design.md`、`../design.md`）。找到則自動載入；找不到則改為純截圖分析，並在報告末尾提示建立 design.md 的好處。

**Figma 載入方式**：使用者提供 URL 時，呼叫 Figma MCP `get_design_context` 取得元件規格。若未提供 URL，此步驟跳過。

---

## 執行步驟

### Step 1 — 識別元件清單

掃描截圖，列出畫面上所有可辨識的 UI 元件與佈局區塊：

```
識別原則：
- 以「工程師會怎麼拆 component」的角度分解
- 區分「容器（Layout）」與「元件（Component）」
- 標注元件的層級關係（Parent / Child）
- 若同類元件有多種狀態（如 Button primary / secondary），分別列出
```

### Step 2 — 查詢規格

對每個元件，依序查詢三個來源：

```
for 每個元件:
  → 查 design.md：取 color token、spacing token、typography token、radius token
  → 查 Figma（若有）：取 component padding、variant props、layout 細節
  → 若兩者皆無：目測推斷，標記 ⚠️
```

### Step 3 — 輸出製作 spec

````
# 製作 Spec：[畫面名稱]

**生成日期**：[今天日期]
**設計來源**：截圖 [+ design.md ✅ / ❌] [+ Figma ✅ / ❌]
**⚠️ 推斷值數量**：X 項（需在製作完成後以 prototype-qa 驗證）

---

## 佈局結構

```
[用縮排文字描述頁面的容器層級結構]
Page
├── Header（height: X, bg: [token]）
├── Sidebar（width: X, bg: [token]）
└── Main Content
    ├── Section A
    │   ├── ComponentA
    │   └── ComponentB
    └── Section B
```

---

## 元件規格表

### [元件名稱 1]

| 屬性 | 數值 | 來源 |
|------|------|------|
| background | [token 名] = [hex值] | design.md |
| padding | [數值] | Figma |
| border-radius | [token 名] = [數值] | design.md |
| font-size | [token 名] = [數值] | design.md |
| font-weight | [數值] | Figma ⚠️ 推斷 |
| color | [token 名] = [hex值] | design.md |
| border | [數值] solid [token] | ⚠️ 推斷 |

**Variants**（若有）：
- Primary：bg = [token], color = [token]
- Secondary：bg = transparent, border = [token], color = [token]

**狀態**（從 Figma 或推斷）：
- Default：[描述]
- Hover：[描述或「⚠️ 未定義」]
- Disabled：[描述或「⚠️ 未定義」]

---

### [元件名稱 2]

[同上格式]

---

## 全域 Token 參考

（從 design.md 提取本畫面用到的 token，方便 AI 製作時一次查閱）

| Token 名稱 | 數值 | 用途 |
|-----------|------|------|
| [token] | [值] | [用在哪個元件] |

---

## ⚠️ 未定義項目清單

以下屬性在 design.md 與 Figma 均無明確規格，AI 製作時需自行判斷或設計師補充：

| 元件 | 屬性 | 建議暫用值 | 優先補充？ |
|------|------|----------|---------|
| [元件] | [屬性] | [建議值] | 🔴 高 / 🟡 中 / 🟢 低 |

````

### Step 4 — 輸出 AI 製作 Prompt

在 spec 之後，附上一份可直接使用的 AI 製作 prompt：

````
---

## AI 製作 Prompt（可直接複製使用）

```
請根據以下規格製作 [畫面名稱] 的 HTML prototype：

【設計規範】
- 嚴格依照下方「元件規格表」的數值製作，不要使用 Tailwind 預設值或自行推斷
- 所有色彩使用 CSS custom properties（變數名稱對應 token 名稱）
- 間距使用規格表中的數值，不要四捨五入或調整
- 若規格標注「⚠️ 推斷」，請使用建議暫用值，並在程式碼中加上 /* TODO: 需設計確認 */ 註解

【元件規格】
[貼入上方元件規格表]

【全域 Token】
:root {
[列出所有 token: CSS variable 格式]
}

【佈局結構】
[貼入佈局結構描述]

【完成後】
製作完成後，請逐一列出你「無法確認是否符合設計」的屬性，我會使用 prototype-qa 做差異驗證。
```
````

---

## 輸出原則

1. **規格要具體**：不寫「藍色按鈕」，寫「background: var(--color-interactive-primary) = #3B82F6」
2. **來源要標注**：每個數值都要標明是來自 design.md、Figma 還是推斷，讓後續 QA 知道哪些是確定值、哪些需要驗證
3. **推斷要明確**：⚠️ 標記的項目必須建議暫用值，不能留空
4. **prompt 要可直接用**：製作 prompt 複製貼上後不需要再修改，AI 應能直接開始製作
