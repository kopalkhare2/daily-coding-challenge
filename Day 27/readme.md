# Day 24 - Dr. G. Viswanathan Challenge

**Problems Solved:**  
1. Maximum Subarray (LeetCode #53 - Medium)  
2. Path Sum (LeetCode #112 - Easy)

## ✅ Problem Summary

### 🔹 1. Maximum Subarray
- **Category:** Array, Dynamic Programming
- **Concepts Used:** Kadane’s Algorithm
- **Problem Link:** [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

### 🔹 2. Path Sum
- **Category:** Tree, DFS, Recursion
- **Concepts Used:** Depth-First Search (Recursive)
- **Problem Link:** [Path Sum](https://leetcode.com/problems/path-sum/)

---

## 🧠 Approach & Method

### 🔹 Maximum Subarray
**Approach:**  
Kadane's Algorithm is used to track the current subarray sum. At each step, we decide whether to continue the existing subarray or start a new one from the current element. The maximum sum found during this process is the answer.

**Method Summary:**  
- Initialize `currentSum` and `maxSum` with the first element.
- Traverse the array:
  - At each step, choose the maximum between the current element and `currentSum + element`.
  - Update `maxSum` if `currentSum` exceeds it.

---

### 🔹 Path Sum
**Approach:**  
We use DFS recursion to check each root-to-leaf path in the binary tree. At each node, we subtract its value from the `targetSum` and recursively check its left and right children.

**Method Summary:**  
- If a node is a leaf and its value equals the remaining target, return true.
- Recursively call for left and right subtrees with updated `targetSum`.
- Return true if either subtree has a valid path.
