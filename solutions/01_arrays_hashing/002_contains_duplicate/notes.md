# 002 · Contains Duplicate

**Pattern:** Arrays & Hashing  
**Difficulty:** Easy  
**Date attempted:** 2026-06-21  
**Time to solve:**  
**Solved without help:** yes

---

## Approach

Use a set to track seen numbers in a single pass. Before adding each number, check if it already exists in the set — if so, a duplicate exists and we return early.

## Complexity

- **Time:** O(n) — single pass, early exit on first duplicate
- **Space:** O(n) — set grows up to n elements

## Key Insight

A set gives O(1) membership checks. Checking before inserting catches the duplicate the moment it appears, avoiding a full scan.

## Gotchas

- `len(nums) != len(set(nums))` is a valid one-liner but has no early exit — always worse in the average case. Prefer the explicit loop.

## Revisit?

no
