# LeetCode Problem Summaries

This document outlines the approach and logic used to solve two LeetCode problems:

1. **450. Delete Node in a BST (Medium)**
2. **14. Longest Common Prefix (Easy)**

---

## 1. Delete Node in a BST

**Problem Summary**:  
Given the root of a Binary Search Tree (BST) and a key, delete the node with the specified key and return the updated root.

### 🔍 Core Logic:
A BST has the property that for any node:
- All values in the left subtree are smaller.
- All values in the right subtree are larger.

Deletion in a BST can be broken down into two major stages:
1. **Search**: Traverse the tree to find the node to delete.
2. **Delete**:
   - **Case 1**: Node has no children → Simply remove the node.
   - **Case 2**: Node has one child → Replace the node with its child.
   - **Case 3**: Node has two children → 
     - Find the **in-order successor** (minimum in the right subtree).
     - Copy the successor's value to the node.
     - Recursively delete the successor node.

### 💡 Approach:
- Traverse left if the key is smaller than the node’s value.
- Traverse right if the key is greater than the node’s value.
- When found, handle one of the three deletion cases accordingly.
- Ensure to return the modified subtree back up the recursive call stack to maintain tree structure.

---

## 2. Longest Common Prefix

**Problem Summary**:  
Find the longest common prefix string among an array of strings. Return an empty string if no common prefix exists.

### 🔍 Core Logic:
- The common prefix of a list of strings is the **shared starting substring** of all the strings.

### 💡 Approach:
- Start by assuming the first string is the prefix.
- Iteratively compare this prefix with each string in the list.
- Trim the prefix from the end until the current string starts with it.
- If at any point the prefix becomes empty, return an empty string immediately.
- Continue until all strings have been checked.

---
