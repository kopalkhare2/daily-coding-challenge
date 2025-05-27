# LeetCode Solutions – Logic and Approach

This README documents the logic and approach for the following solved LeetCode problems:

1. [2470. Number of Subarrays With LCM Equal to K (Medium)](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/)
2. [111. Minimum Depth of Binary Tree (Easy)](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

---

## ✅ 1. Number of Subarrays With LCM Equal to K

### Problem:
Given an integer array `nums` and an integer `k`, return the number of subarrays of `nums` where the **least common multiple (LCM)** of the subarray's elements is `k`.

### Approach:
- Iterate through all subarrays starting from every index.
- For each starting index, calculate the LCM progressively by including one element at a time.
- Stop early if the current LCM becomes greater than `k` or if `k` is not divisible by the current LCM (optimization).
- Increment the count whenever the current LCM matches `k`.

---

## ✅ 2. Minimum Depth of Binary Tree

### Problem:
Given a binary tree, find its **minimum depth**, which is the number of nodes along the shortest path from the root to the nearest leaf node.

### Approach:
- Use recursion to traverse the tree.
- If the current node is null, return 0.
- If one child is null, recursively calculate depth through the non-null child and add 1.
- If both children exist, take the minimum of the depths of both subtrees and add 1.

---

### 👨‍💻 Status:
- Both problems accepted with optimal runtime.
- Solutions implemented in Python and C++ respectively.

---
