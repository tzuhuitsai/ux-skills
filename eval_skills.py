#!/usr/bin/env python3
"""
Skill quality evaluator for ux-skills repository.
Evaluates each SKILL.md against 5 dimensions, total 100 pts.
Pass threshold: >= 90 pts.
"""

import re
import sys

# ──────────────────────────────────────────
# Rubric (total = 100 pts)
# ──────────────────────────────────────────
# 1. Frontmatter completeness     20 pts
# 2. Trigger precision            20 pts
# 3. Skill-boundary clarity       15 pts
# 4. Output-format definition     25 pts
# 5. Content depth & specificity  20 pts
# ──────────────────────────────────────────

PASS_THRESHOLD = 90


def score_frontmatter(content: str) -> tuple[int, list[str]]:
    """20 pts — YAML frontmatter has name, description, triggers, boundaries."""
    pts = 0
    notes = []
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        notes.append("✗ 缺少 YAML frontmatter")
        return 0, notes

    fm = fm_match.group(1)

    # name field (5 pts)
    if re.search(r"^name:", fm, re.MULTILINE):
        pts += 5
    else:
        notes.append("✗ frontmatter 缺少 name")

    # description field (5 pts)
    if re.search(r"^description:", fm, re.MULTILINE):
        pts += 5
    else:
        notes.append("✗ frontmatter 缺少 description")

    # trigger section inside description (5 pts)
    if "使用此 skill 的時機" in fm:
        pts += 5
    else:
        notes.append("✗ description 缺少「使用此 skill 的時機」")

    # boundary section inside description (5 pts)
    if "與其他 skills 的邊界" in fm:
        pts += 5
    else:
        notes.append("✗ description 缺少「與其他 skills 的邊界」")

    if pts == 20:
        notes.append("✓ frontmatter 完整")
    return pts, notes


def score_triggers(content: str) -> tuple[int, list[str]]:
    """20 pts — trigger conditions are specific and numerous."""
    pts = 0
    notes = []

    # Explicit trigger section (5 pts)
    if "使用此 skill 的時機" in content:
        pts += 5
    else:
        notes.append("✗ 缺少「使用此 skill 的時機」段落")

    # 積極觸發 keyword (5 pts)
    if "積極觸發" in content:
        pts += 5
    else:
        notes.append("✗ 缺少「積極觸發」標記")

    # Number of user-scenario bullets (≥ 4 = 5 pts, ≥ 3 = 3 pts)
    user_bullets = len(re.findall(r"- 使用者", content))
    if user_bullets >= 4:
        pts += 5
        notes.append(f"✓ {user_bullets} 個使用者觸發情境")
    elif user_bullets >= 3:
        pts += 3
        notes.append(f"~ {user_bullets} 個使用者觸發情境（建議 ≥ 4）")
    else:
        notes.append(f"✗ 只有 {user_bullets} 個使用者觸發情境")

    # Keyword list present (5 pts)
    if "關鍵詞" in content or "關鍵字" in content:
        pts += 5
        notes.append("✓ 有關鍵詞清單")
    else:
        notes.append("✗ 缺少關鍵詞清單")

    return pts, notes


def score_boundary(content: str) -> tuple[int, list[str]]:
    """15 pts — clearly distinguishes from sibling skills."""
    pts = 0
    notes = []

    # Has boundary section (5 pts)
    if "與其他 skills 的邊界" in content:
        pts += 5
    else:
        notes.append("✗ 缺少「與其他 skills 的邊界」")

    # Has negative-trigger (不觸發條件) (5 pts)
    if "不觸發條件" in content:
        pts += 5
        notes.append("✓ 有「不觸發條件」說明")
    else:
        notes.append("✗ 缺少「不觸發條件」")

    # Uses → arrows to show routing (≥ 2 = 5 pts)
    arrows = len(re.findall(r"→", content))
    if arrows >= 4:
        pts += 5
        notes.append(f"✓ {arrows} 個 → 路由說明")
    elif arrows >= 2:
        pts += 3
        notes.append(f"~ {arrows} 個 → 路由說明（建議 ≥ 4）")
    else:
        notes.append(f"✗ 路由說明不足（{arrows} 個 →）")

    return pts, notes


def score_output_format(content: str) -> tuple[int, list[str]]:
    """25 pts — output template is complete and structured."""
    pts = 0
    notes = []

    # Has 輸出格式 section (10 pts)
    if "## 輸出格式" in content:
        pts += 10
        notes.append("✓ 有「輸出格式」章節")
    else:
        notes.append("✗ 缺少「## 輸出格式」章節")

    # Has code-fenced template (5 pts)
    code_blocks = len(re.findall(r"```", content))
    if code_blocks >= 4:
        pts += 5
        notes.append(f"✓ {code_blocks // 2} 個 code block（輸出範本 + 程式碼範例）")
    elif code_blocks >= 2:
        pts += 3
        notes.append(f"~ {code_blocks // 2} 個 code block")
    else:
        notes.append("✗ 缺少 code block 輸出範本")

    # Uses traffic-light emoji (🔴🟡🟢) (5 pts)
    if "🔴" in content and "🟡" in content and "🟢" in content:
        pts += 5
        notes.append("✓ 使用三色燈號（🔴🟡🟢）")
    else:
        notes.append("✗ 缺少三色燈號（🔴🟡🟢）")

    # Has markdown table(s) (5 pts)
    tables = len(re.findall(r"\|[-:]+\|", content))
    if tables >= 2:
        pts += 5
        notes.append(f"✓ {tables} 個 Markdown 表格")
    elif tables == 1:
        pts += 3
        notes.append("~ 只有 1 個 Markdown 表格")
    else:
        notes.append("✗ 缺少 Markdown 表格")

    return pts, notes


def score_depth(content: str) -> tuple[int, list[str]]:
    """20 pts — actionable content with concrete numbers."""
    pts = 0
    notes = []

    # Number of H2/H3 sections (≥ 6 = 5 pts, ≥ 4 = 3 pts)
    sections = len(re.findall(r"^##+ .+", content, re.MULTILINE))
    if sections >= 6:
        pts += 5
        notes.append(f"✓ {sections} 個章節")
    elif sections >= 4:
        pts += 3
        notes.append(f"~ {sections} 個章節（建議 ≥ 6）")
    else:
        notes.append(f"✗ 只有 {sections} 個章節")

    # Uses concrete numbers / px / ms (5 pts)
    if re.search(r"\d+px|\d+ms|\d+%", content):
        pts += 5
        notes.append("✓ 有具體數字（px / ms / %）")
    else:
        notes.append("✗ 缺少具體數字規格")

    # Has 建議 with 具體 or 修正 (5 pts)
    if re.search(r"建議.{0,20}(具體|修正|改為|改用)", content) or \
       re.search(r"(具體|修正|改為|改用).{0,20}建議", content):
        pts += 5
        notes.append("✓ 有具體修正建議")
    else:
        notes.append("✗ 修正建議不夠具體")

    # Has 重要提醒 section (5 pts)
    if "## 重要提醒" in content:
        pts += 5
        notes.append("✓ 有「重要提醒」章節")
    else:
        notes.append("✗ 缺少「## 重要提醒」章節")

    return pts, notes


def evaluate_skill(skill_dir: str, skill_name: str) -> dict:
    path = f"/home/user/ux-skills/{skill_dir}/SKILL.md"
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return {"skill": skill_name, "error": f"找不到 {path}"}

    fm_pts, fm_notes   = score_frontmatter(content)
    tr_pts, tr_notes   = score_triggers(content)
    bnd_pts, bnd_notes = score_boundary(content)
    out_pts, out_notes = score_output_format(content)
    dep_pts, dep_notes = score_depth(content)

    total = fm_pts + tr_pts + bnd_pts + out_pts + dep_pts
    passed = total >= PASS_THRESHOLD

    return {
        "skill": skill_name,
        "total": total,
        "passed": passed,
        "breakdown": {
            "frontmatter (20)":      (fm_pts,  fm_notes),
            "triggers (20)":         (tr_pts,  tr_notes),
            "boundary (15)":         (bnd_pts, bnd_notes),
            "output_format (25)":    (out_pts, out_notes),
            "depth (20)":            (dep_pts, dep_notes),
        },
    }


SKILLS = [
    ("responsive-layout-stress-tester", "responsive-layout-stress-tester"),
    ("interaction-pattern-advisor",      "interaction-pattern-advisor"),
    ("design-handoff",                   "design-handoff"),
    ("component-state-specifier",        "component-state-specifier"),
    ("visual-hierarchy-checker",         "visual-hierarchy-checker"),
    ("data-density-optimizer",           "data-density-optimizer"),
    ("design-system-manager",            "design-system-manager"),
]


def main():
    print("=" * 60)
    print("  UX Skills Quality Evaluation")
    print(f"  Pass threshold: {PASS_THRESHOLD}/100")
    print("=" * 60)

    all_passed = True
    results = []

    for skill_dir, skill_name in SKILLS:
        result = evaluate_skill(skill_dir, skill_name)
        results.append(result)

        status = "✅ PASS" if result.get("passed") else "❌ FAIL"
        print(f"\n{'─'*60}")
        print(f"  {status}  {result['skill']}  [{result.get('total', 0)}/100]")
        print(f"{'─'*60}")

        for dim, (pts, notes) in result.get("breakdown", {}).items():
            max_pts = int(re.search(r"\((\d+)\)", dim).group(1))
            bar = "█" * pts + "░" * (max_pts - pts)
            print(f"  {dim:<22} {bar}  {pts}/{max_pts}")
            for note in notes:
                print(f"    {note}")

        if not result.get("passed"):
            all_passed = False

    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    for r in results:
        status = "✅" if r.get("passed") else "❌"
        print(f"  {status} {r['skill']:<40} {r.get('total', 0):>3}/100")

    print(f"\n  Overall result: {'ALL PASSED ✅' if all_passed else 'SOME FAILED ❌'}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
