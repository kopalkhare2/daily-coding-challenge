# LeetCode Problem Explanations

## 🧩 2697. Lexicographically Smallest Palindrome

### 📝 Problem Statement
Given a string `s` of lowercase English letters, the task is to make `s` a **palindrome** with the **minimum number of operations**. In one operation, you can replace any character in the string with another lowercase letter.

If multiple palindromes are possible with the same number of operations, return the **lexicographically smallest** one.

---

### 💡 Intuition & Logic
- To form a palindrome, we compare characters from both ends moving toward the center (i.e., character at `i` with character at `j` where `i + j = n - 1`).
- If characters are **equal**, no change is needed.
- If characters are **different**, one of them must be changed:
  - To minimize the number of operations, we only change **one** character.
  - To get the **lexicographically smallest** result, we choose the **smaller** character (i.e., earlier in the alphabet).

---

### 🧠 Approach
1. Use two pointers: `i = 0` and `j = s.size() - 1`.
2. While `i < j`, do:
   - If `s[i] != s[j]`, replace the larger character with the smaller one.
3. Return the modified string which is now the required palindrome.

---

### ✅ Example
**Input:** `"egcfe"`  
**Output:** `"efcfe"`  
**Explanation:** Change `'g'` to `'f'` to make it a palindrome. It's also the lexicographically smallest possible palindrome after one change.

---

## 🌳 199. Binary Tree Right Side View

### 📝 Problem Statement
Given the `root` of a binary tree, return the **values of the nodes visible from the right side**, in order from top to bottom.

---

### 💡 Intuition & Logic
- Imagine looking at the tree from the **right side**.
- At each level of the tree, the **rightmost node** is the only one visible.

---

### 🧠 Approach
1. Perform a **Level Order Traversal** (BFS) using a queue.
2. For each level:
   - Traverse all nodes.
   - Track the **last node** in that level and add it to the result list.
3. Continue until all levels are processed.

---

### ✅ Example
**Input:** `[1,2,3,null,5,null,4]`  
**Output:** `[1,3,4]`  
**Explanation:** Rightmost nodes from each level are:  
- Level 0 → `1`  
- Level 1 → `3`  
- Level 2 → `4`

