# LeetCode Problem Solutions

## 🌀 796. Rotate String

**Difficulty:** Easy  
**Topic:** String Manipulation  
**Company Tags:** Frequently asked in interviews  

### 📄 Problem Statement:
Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of **shifts** on `s`.  
A shift operation involves moving the **leftmost** character of `s` to the **rightmost** position.

### 💡 Logic and Approach:
1. The key insight is that all rotations of string `s` will be substrings of `s + s`.
2. So, if `goal` is a rotation of `s`, it should appear in `s + s`.
3. First, check if the lengths of `s` and `goal` are equal. If not, return `false`.
4. Then check if `goal` is a substring of `s + s`.
5. This solution has time complexity **O(n)**, where `n` is the length of the string.

---

## 🌳 235. Lowest Common Ancestor of a Binary Search Tree

**Difficulty:** Medium  
**Topic:** Binary Search Tree, Recursion  
**Company Tags:** Common in coding interviews  

### 📄 Problem Statement:
Given a **Binary Search Tree (BST)**, find the **Lowest Common Ancestor (LCA)** of two given nodes `p` and `q`.  
The **LCA** is defined as the **lowest** node in the BST that has both `p` and `q` as **descendants** (we allow a node to be a descendant of itself).

### 💡 Logic and Approach:
1. Use the properties of BST:
   - All values in the left subtree of a node are smaller than the node’s value.
   - All values in the right subtree are greater.
2. Traverse the tree from the root:
   - If both `p` and `q` are less than the current node, move to the **left**.
   - If both are greater, move to the **right**.
   - If one is on the left and the other is on the right (or matches the root), then the current node is the **LCA**.
3. The approach uses **binary search traversal**, ensuring efficient performance:  
   **Time Complexity:** O(h), where `h` is the height of the tree.

---
