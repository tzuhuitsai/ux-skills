---
name: ux-writing
description: >
  Write, generate, or review UI microcopy for digital product interfaces -- buttons, labels,
  error messages, placeholders, tooltips, success toasts, destructive action dialogs, empty
  states, notifications, and any other text that appears inside a UI. Use this skill whenever
  the user asks what a button/label/error should say, wants copy written for a UI component,
  wants existing UI text reviewed or audited, or describes a product scenario and needs the
  right words. Trigger even if they just say "write this error message", "what should the
  delete confirmation say", "help me word this", or share a UI screenshot and ask for copy
  suggestions. The skill encodes a full rule set so output is always spec-compliant -- don't
  skip it and improvise from general knowledge.
---

# UX Writing

Your job is to produce UI copy that is clear, direct, and consistent with the following
spec. When the user gives you a scenario, component type, or draft copy to review, apply
the rules below and return finished, production-ready text.

---

## DI Brand Voice

> 以下為 DI 品牌層約束，執行所有 copy 任務前先套用。

- **語氣**：中性、清晰、專業（Professional）。不過度親暱，不過度技術化。
- **人稱**：第二人稱 + 主動語態（you/your）+ 行動導向。說明使用者應做什麼 / 事件將發生什麼。
- **避免**：術語縮寫、驚嘆號、責備語氣、指代不明的 "this" / "that"。
- **DIP 產品術語**（保留原文，不翻譯）：Pipeline、Tag、Rule、Entity、Data Bridge、OmniTag、Query Service。

| ✅ 建議 | ❌ 避免 |
|--------|--------|
| Enter your password | Your password is incorrect |
| No results found. Try a different keyword | No results found |
| Select a date to continue | Please select a date |
| Email format is incorrect | Invalid input |

---

## Three rules that matter most

These three patterns account for the most common mistakes. Check them first on every
piece of copy before applying anything else.

1. **No "Please" in errors or instructions.** Use `[Field name] is required` not
   `Please enter your field name.` State the fact; don't ask politely.

2. **Irreversible destructive actions use `Permanently delete` on the primary button.**
   The dialog title names the resource (`Delete topic user-events`); the button signals
   permanence (`Permanently delete`). Never just `Delete` or `Yes` for an irreversible action.

3. **Single-line elements get no period.** Buttons, labels, placeholders, tooltips,
   checkboxes, single-sentence body text -- no period. Two or more sentences -- add
   periods to all of them.

---

## Core principles

**Say what happens, not what to beware of.** Users read UI in an F-pattern -- they skim.
Lead with the outcome or action, not a caution. "Deleting this topic removes all messages"
is better than "Warning: This action is irreversible."

**Use second person (you/your) throughout.** Never mix "my/I" with "your/you" on the same
screen. Exception: legal/agreement text where "I agree to..." emphasises user ownership.

**Sentence case everywhere.** First word capitalised, everything else lowercase -- for
titles, labels, nav items, buttons, headings. Proper nouns and technical acronyms
(API, IAM, CSV, TTL, Schema) keep their own capitalisation. Never Title Case, never
ALL CAPS.

---

## Component rules

### Buttons
- 1-2 words, start with a verb: `Save`, `Export records`, `Confirm`
- Describe the action, not the answer: `Delete topic` not `Yes` / `OK`
- Destructive irreversible actions: `Permanently delete` not just `Delete`
- No period, no question mark

### Labels & placeholders
- Sentence case: `Created date`, `Search by ID or name`
- Placeholder = specific action hint, no period: `Search by ID or name`
- Helper text for character limits: `Enter up to 300 characters` (preferred over
  "Max 300" or "300 character limit")
- Counter format: `0 / 300`

### Error messages
- **Surface only what the user can act on.** Technical details (error codes, stack
  traces, system states, internal IDs) belong in logs, not in UI copy. The UI message
  answers exactly two questions: "What can't I do right now?" and "What do I do next?"
  If neither has a clear answer yet, use the minimal fallback:
  `Something went wrong. Try again, or contact support if the issue persists.`
- State the fact + the fix. Format: `[What went wrong]. [How to resolve].`
  - Good: `No long type fields found in this topic. Select another topic to continue.`
  - Bad: `Error! Please select a valid topic.`
- Required fields: `[Field name] is required` (specific) or `This field is required`
  (general). Never `Please enter this field.`
- Use `Unable to...` not `Failed to...` -- more neutral, less accusatory
- Two sentences get periods; a single instruction does not

### Success & status messages (toasts/snackbars)
- State what completed, don't say "successfully": `Topic registered`, `File uploaded`
- The green colour already signals success -- the word "successfully" is redundant
- Use `complete` when you need a word: `Upload complete`
- Dynamic data labels: `Updated 2 minutes ago` not `Freshness: 2 mins ago`

### Destructive action dialogs
Distinguish reversible from irreversible -- they use different copy and visual treatment:

| Type | Dialog title | Primary button | Visual |
|------|-------------|----------------|--------|
| Reversible (disable) | `Disable [name]` | `Disable` | Warning / neutral (orange, grey) |
| Irreversible (delete) | `Delete [resource-type] [name]` | `Permanently delete` | Destructive red |

The title names exactly what is being deleted so the user can't mistake it. The primary
button says `Permanently delete` (not just `Delete`) to signal that the action cannot be
undone -- even though the title already contains the word "Delete".

Example for deleting a topic named "user-events":
- Title: `Delete topic user-events`
- Body: `Deleting this topic permanently removes all messages and cannot be undone.`
- Primary button: `Permanently delete`
- Cancel: `Cancel`

For **irreversible** actions, add double friction:
1. Checkbox (no period): `I acknowledge this action cannot be undone`
2. Name confirmation input label (no period): `Type the topic name to confirm`

No question mark on the title. No colon. No Title Case.

### Notifications
- Never use "today", "tomorrow", "tonight" -- use the specific day: `Monday`, `Jun 3`
- Character budgets (English): title < 29 chars, collapsed body < 40 chars,
  expanded body < 80 chars, buttons 1-2 words each
- If the resource name makes the title exceed 29 chars, shorten the title (e.g. `Segment ready`)
  and put the full name in the body instead
- Don't repeat the app name -- the OS already shows it

### Tooltips / helper text
- Explain the "why" or add context the label can't: `Required for deduplication across sources`
- No period on a single line; period required if two or more sentences
- End with a call to action if relevant: `Contact your administrator for access`

### Empty states
- Two parts: reason + path forward
  - `No schema defined` + `Upload a schema to start validating messages`
- Don't just say "No data" -- tell the user why and what to do next

### Alt text (images, charts, icons)
- Max 140 characters
- Do not start with "Image of" -- screen readers announce "image" automatically
- Decorative images: use `alt=""` (empty string, not omitted)
- Charts: `[Summary of what the data shows] + [why this matters or where to look]`

---

## Forbidden patterns

When you catch any of these in a review, replace them.

| Avoid | Use instead |
|-------|------------|
| Please / Sorry / Thank you | State the fact or instruction directly |
| Are you sure? | State consequences; provide a confirming action |
| Please note: | Just say it |
| Successfully / Success! | Omit, or use "complete" |
| Failed to... | Unable to... |
| Warning: / Danger: (in body text) | State the consequence; use colour/icons for severity |
| i.e. / e.g. / etc. | for example / and more |
| I want to... (checkbox) | Direct action phrase: "Delete all data" |
| ALL CAPS | Sentence case |
| Title Case For All The Words | Sentence case |

---

## Tone calibration (do this first)

Before generating copy, determine the audience from context:
1. Check for explicit signals: product name, feature name, user type mentioned
   (e.g. "data engineer", "marketing user", "admin console", "pipeline")
2. If the copy type makes the audience obvious, proceed without asking
   (destructive dialogs → always enterprise-neutral; onboarding → default SaaS)
3. If audience is genuinely ambiguous after step 1–2, ask exactly ONE question
   before generating: "Is this for a technical user (engineer, admin) or a
   business user (analyst, marketer)?" — then generate immediately after the answer.

Default when unknown: plain language + tooltip for jargon.

## Tone by audience

When the user specifies the persona or platform layer, adjust:

- **PaaS / technical users** (data engineers, devs): precision first, keep technical terms
  (Schema, Nullable, Partition, TTL, Principal). Example: `Compaction policy`
- **SaaS / business users** (marketing, analysts, admins): action outcomes first, plain
  alternatives. Example: `Empty` instead of `Null`; `Members` instead of `Records`

When the audience is mixed or unknown, default to plain language and add a tooltip for
jargon.

---

## Output format

When generating copy, present it like this -- clean and ready to paste:

```
Dialog title:      Delete topic user-events
Body:              Deleting this topic permanently removes all messages and cannot be undone.
Checkbox:          I acknowledge this action cannot be undone
Confirm input:     Type the topic name to confirm
Primary button:    Permanently delete
Cancel button:     Cancel
```

When **reviewing** existing copy, show a before/after table with a one-line note on
which rule was applied. Don't over-explain -- keep the reasoning tight.

| Element | Before | After | Rule |
|---------|--------|-------|------|
| Button | Delete Topic | Delete topic | Sentence case |
| Error | Please enter a name. | Name is required | No "please"; drop period |

---

## Globalisation note

If copy will be translated, keep sentences short -- other languages expand ~1.5x from
English. Avoid idioms, metaphors, and region-specific references. Don't start a sentence
with "This" or "That" unless the noun immediately follows.
