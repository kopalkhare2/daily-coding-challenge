🚀 Day 31 - Dr. G. Viswanathan Challenge

## ✅ Problem 1: Length of Last Word

### 📝 Problem Statement
Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A word is defined as a maximal substring consisting of non-space characters only.

### 💡 Approach
- Traverse the string from the end to skip trailing spaces.
- Then, continue traversing in reverse while counting characters until a space is encountered.
- Return the final count.

### 🔍 Key Concepts
- Reverse traversal of string
- Edge case handling (e.g., trailing spaces)
- Basic string manipulation


---

## ✅ Problem 2: Flatten Binary Tree to Linked List

### 📝 Problem Statement
Given the `root` of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same `TreeNode` class where the right child pointer points to the next node in the list and the left child pointer is always `null`.
- The flattened list must follow the same order as a **pre-order traversal** of the binary tree.

### 💡 Approach
- Perform a reverse post-order traversal: right → left → root.
- Use a pointer to keep track of the previous node (`prev`).
- At each node, set:
  - `node->right = prev`
  - `node->left = nullptr`
  - `prev = node`

### 🔍 Key Concepts
- Tree traversal (pre-order and post-order)
- In-place tree modification
- Recursion
- Binary tree transformation to a linear structure
