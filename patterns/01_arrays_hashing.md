# Pattern: Arrays & Hashing

## Core Idea

Trade space for time. Use a hash map to turn O(n²) lookup problems into O(n) by storing values (or counts, or indices) as you scan.

## When to Reach for This

- "Find two elements that satisfy a condition" → store complement while scanning
- "Count frequency of elements" → `Counter` or `defaultdict(int)`
- "Detect duplicates" → `set`
- "Group elements by some property" → `defaultdict(list)`

## Canonical Templates

**Complement lookup (Two Sum style)**
```python
seen = {}
for i, n in enumerate(nums):
    if target - n in seen:
        return [seen[target - n], i]
    seen[n] = i
```

**Frequency count**
```python
from collections import Counter
freq = Counter(s)  # or Counter(nums)
```

**Grouping**
```python
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    key = tuple(sorted(word))  # or some canonical form
    groups[key].append(word)
```

## Complexity Profile

- Time: O(n) for a single pass with O(1) hash ops
- Space: O(n) for the map

## Useful Python Built-ins

- `collections.Counter` — frequency map in one line
- `collections.defaultdict` — map with a default value, avoids key existence checks
- `set` — O(1) membership test, use for duplicate detection

## Watch Out For

- `dict.get(key, default)` to avoid KeyError when key may be missing
- When the problem asks for indices, store the index as the value, not the element
- Sorted arrays let you skip the map entirely (use two pointers instead)

## Problems in This Group

| # | Problem | Key Trick |
|---|---------|-----------|
| 001 | Two Sum | complement map |
| 002 | Contains Duplicate | set membership |
| 003 | Valid Anagram | Counter comparison |
| 004 | Group Anagrams | sorted tuple as group key |
| 005 | Top K Frequent Elements | Counter + heapq or bucket sort |
| 006 | Encode and Decode Strings | length-prefix encoding |
| 007 | Product of Array Except Self | prefix + suffix products, no division |
| 008 | Valid Sudoku | row/col/box sets |
| 009 | Longest Consecutive Sequence | set membership + only start from sequence heads |
