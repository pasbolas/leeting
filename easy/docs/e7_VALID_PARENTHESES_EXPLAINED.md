# Valid Parentheses / Closing Matching Brackets - Concept Explanation

## Problem Overview
The goal is to determine if a string of brackets is **valid**, meaning:
1. Every opening bracket has a matching closing bracket of the same type
2. Brackets are closed in the correct order (no crossing like `([)]`)
3. All brackets are properly matched

### Valid Examples:
- `"()"` ✓
- `"(){}"` ✓
- `"([{}])"` ✓

### Invalid Examples:
- `"("` ✗ (unclosed)
- `"([)]"` ✗ (wrong order)
- `"{]"` ✗ (mismatched types)

---

## Solution 1: The Counter Approach (Ugly Solution)

### How It Works
1. **Count each bracket type** - Track how many opening vs closing brackets of each type
2. **Check adjacent pairs** - Validate that closing brackets follow the correct opening bracket
3. **Verify balance** - Ensure each type has equal opening and closing brackets

### Code Breakdown

```python
keydict = {
    "(": 0, ")": 0,
    "{": 0, "}": 0,
    "[": 0, "]": 0
}
```
Dictionary to count each bracket type.

```python
match previous_word:
    case "(":
        if word == "]" or word == "}":
            return False
```
**Check order**: If the previous bracket was `(`, the next must be `)`. Other closing brackets are invalid.

```python
if (keydict["("] - keydict[")"]) != 0:
    return False
```
**Check balance**: Difference between opening and closing must be zero.

### Why This Approach Has Issues
- ❌ Only checks **adjacent pairs** - misses problems like `"([)]"`
- ❌ Inefficient - uses extra memory for counting
- ❌ Doesn't handle nesting complexity well
- ❌ Code is repetitive (lots of match cases)

---

## Solution 2: The Stack Approach (Beautiful Solution)

### How It Works
A **stack** is a Last-In-First-Out (LIFO) data structure. Imagine a stack of plates - you add to the top and remove from the top.

**Key Idea**: Use a stack to track opening brackets and match them with closing brackets in the correct order.

### Algorithm

1. **For each character in the string:**
   - If it's an **opening bracket** `(`, `{`, `[` → **Push** it onto the stack
   - If it's a **closing bracket** `)`, `}`, `]` → Check if it matches the **top of the stack**
     - If no match → return `False` (invalid)
     - If match → **Pop** from the stack
   
2. **After processing all characters:**
   - If the stack is empty → `True` (all brackets matched)
   - If the stack has leftovers → `False` (unclosed brackets)

### Code Breakdown

```python
stack = []
pairs = {"(":")", "{":"}", "[":"]"}
```
- `stack`: Holds unmatched opening brackets
- `pairs`: Maps each opening bracket to its matching closing bracket

```python
if character in pairs:
    stack.append(character)
```
**Opening bracket?** Add it to the stack.

```python
elif character in pairs.values():
    if not stack or character != pairs[stack[-1]]:
        return False
    stack.pop()
```
**Closing bracket?** 
- Check if stack is empty (`not stack`) - if yes, invalid
- Check if the closing bracket matches the most recent opening bracket (`pairs[stack[-1]]`)
- If it matches, remove the opening bracket from stack (`pop()`)

```python
if len(stack) != 0:
    return False
```
**Final check**: If anything is left on the stack, there were unclosed brackets.

### Why This Approach is Better
- ✅ Handles **nesting** perfectly: `([{}])`
- ✅ Detects **crossing** patterns: `([)]` is caught as invalid
- ✅ Efficient - O(n) time, O(n) space
- ✅ Clean, readable code
- ✅ Works with any number of bracket types

---

## Visualization Example

**Input:** `"([)]"`

| Step | Char | Stack | Action | Valid? |
|------|------|-------|--------|--------|
| 1 | `(` | `['(']` | Push opening bracket | - |
| 2 | `[` | `['(', '[']` | Push opening bracket | - |
| 3 | `)` | `['(', '[']` | Closing `)` but top is `[` | ❌ INVALID |

**Result:** `False` (brackets are crossing/mismatched)

---

## Key Concepts to Remember

### Stack (LIFO)
- Last element added is first to be removed
- Like a stack of books - you take from the top

### Matching Pairs
- Each closing bracket must match the **most recent unmatched** opening bracket
- This is exactly what a stack handles

### Time/Space Complexity
- **Time:** O(n) - visit each character once
- **Space:** O(n) - worst case, all opening brackets on stack

---

## Practice Exercise

Try tracing through these inputs with the stack approach:
1. `"({})"` → Should be `True`
2. `"([)]"` → Should be `False`
3. `"{[]}"` → Should be `True`
4. `"("` → Should be `False`
5. `"())"` → Should be `False`

Can you draw the stack at each step?
