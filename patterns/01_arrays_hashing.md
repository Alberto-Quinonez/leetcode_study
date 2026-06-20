# Pattern: Arrays & Hashing

## Core Idea

Trade space for time. Use a hash map to turn O(n²) lookup problems into O(n) by storing values (or counts, or indices) as you scan.

## When to Reach for This

- "Find two elements that satisfy a condition" → store complement while scanning
- "Count frequency of elements" → `map[T]int`
- "Detect duplicates" → `map[T]struct{}`
- "Group elements by some property" → `map[key][]T`

## Canonical Templates

**Complement lookup (Two Sum style)**
```go
seen := make(map[int]int) // value → index
for i, n := range nums {
    if j, ok := seen[target-n]; ok {
        return []int{j, i}
    }
    seen[n] = i
}
```

**Frequency count**
```go
freq := make(map[byte]int)
for _, c := range s {
    freq[c]++
}
```

**Grouping**
```go
groups := make(map[string][]string)
for _, word := range words {
    key := sortString(word) // or some canonical form
    groups[key] = append(groups[key], word)
}
```

## Complexity Profile

- Time: O(n) for a single pass with O(1) map ops
- Space: O(n) for the map

## Watch Out For

- Map lookup returns zero-value if key is missing — use the two-value form `v, ok := m[k]`
- When the problem asks for indices, store index as the value, not the element
- Sorted arrays let you skip the map entirely (use two pointers instead)

## Problems in This Group

| # | Problem | Key Trick |
|---|---------|-----------|
| 001 | Two Sum | complement map |
| 002 | Contains Duplicate | existence set |
| 003 | Valid Anagram | frequency diff |
| 004 | Group Anagrams | sorted key as group identifier |
| 005 | Top K Frequent Elements | freq map + bucket sort or heap |
| 006 | Encode and Decode Strings | length-prefix encoding |
| 007 | Product of Array Except Self | prefix + suffix products, no division |
| 008 | Valid Sudoku | row/col/box sets |
| 009 | Longest Consecutive Sequence | set membership + only start from sequence heads |
