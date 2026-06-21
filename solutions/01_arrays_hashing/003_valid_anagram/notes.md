# 003 · Valid Anagram

**Pattern:** Arrays & Hashing  
**Difficulty:** Easy  
**Date attempted:** 2026-06-21  
**Time to solve:**  
**Solved without help:** yes

---

## Approach

Early exit on length mismatch. Build frequency maps for both strings manually with `dict.get(k, 0)`, then compare counts for every key in s's map against t's map.

## Complexity

- **Time:** O(n)
- **Space:** O(1) — at most 26 keys (lowercase letters), so the maps are bounded

## Key Insight

Two strings are anagrams if and only if their character frequency maps are identical. Length check upfront avoids the edge case where t has extra characters not in s.

## Gotchas

- `tCountMap.get(k, 0)` handles characters in s that don't appear in t — no KeyError
- Don't need a separate `tVal == 0` check; `v != tCountMap.get(k, 0)` covers it since v >= 1

## Revisit?

no
