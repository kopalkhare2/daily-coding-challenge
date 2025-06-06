# ✅ LeetCode Practice Notes

## 🟢 700. Search in a Binary Search Tree

### Problem Summary
You are given the root of a binary search tree (BST) and an integer value. You need to find and return the subtree rooted at the node with the given value. If no such node exists, return `null`.

### 🔍 Approach & Logic
A **Binary Search Tree** (BST) has a key property:  
- Values in the left subtree are **less than** the current node’s value.  
- Values in the right subtree are **greater than** the current node’s value.

Using this property:
- If the current node is `null` or its value matches the target, return it.
- If the target value is **less**, search recursively in the **left** subtree.
- If the target value is **greater**, search recursively in the **right** subtree.

This ensures a time-efficient search with average complexity **O(log n)** for a balanced BST.

---

## 🟢 125. Valid Palindrome

### Problem Summary
Determine whether a given string is a **palindrome** after converting all uppercase letters to lowercase and removing all non-alphanumeric characters. A string is a palindrome if it reads the same forward and backward.

### 🔍 Approach & Logic
- **Sanitize the string**:
  - Convert all characters to **lowercase**.
  - Filter out all **non-alphanumeric** characters.

- After preprocessing:
  - Compare the cleaned string with its **reverse**.
  - If both are equal, the string is a palindrome.

This method ensures only valid characters are considered and case is ignored, making the check clean and robust.

---
