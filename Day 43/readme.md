# LeetCode Problem Summaries

## 1. 230. Kth Smallest Element in a BST

### 🧠 Problem Statement:
Given the root of a Binary Search Tree (BST) and an integer `k`, return the `k`th smallest value (1-indexed) among all the nodes in the BST.

### ✅ Approach:
Use **inorder traversal** because the in-order traversal of a BST yields nodes in **sorted (ascending) order**.

### 💡 Logic:
- Perform a recursive in-order traversal.
- Maintain a counter to track how many nodes have been visited.
- When the count reaches `k`, capture the node’s value as the result.
- Early termination is possible once the `k`th node is found.

### 📌 Time Complexity:
- **O(H + k)**, where H is the height of the tree. In the worst case (skewed tree), H = N. For balanced trees, H = log N.

---

## 2. 6. Zigzag Conversion

### 🧠 Problem Statement:
Convert a given string `s` into a zigzag pattern on a given number of rows, and then read line by line.

### ✅ Approach:
Simulate the zigzag traversal by building each row of the pattern one character at a time.

### 💡 Logic:
- Use an array of strings (or list of strings) for each row.
- Traverse the input string while maintaining the current row and direction (down or up).
- Change direction when the top or bottom row is reached.
- Finally, concatenate all rows to get the final result.

### 📌 Time Complexity:
- **O(n)** where `n` is the length of the string.
