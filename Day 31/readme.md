# LeetCode Problems Summary

## Problem 1: Maximum Depth of Binary Tree

### Problem ID
104

### Difficulty
Easy

### Description
Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

### Approach and Logic
- Use **recursion** to traverse the tree.
- For each node, recursively find the maximum depth of its left and right subtrees.
- The depth at the current node is `1 + max(left_depth, right_depth)`.
- Base case: if the node is `null`, return `0`.

This is a classic example of **post-order traversal** in a binary tree, where computation is done after visiting both left and right children.

---

## Problem 2: Flipping an Image

### Problem ID
832

### Difficulty
Easy

### Description
Given an `n x n` binary matrix representing an image, the task is to:
1. **Flip the image horizontally** – i.e., reverse each row.
2. **Invert the image** – replace all `0`s with `1`s and all `1`s with `0`s.

Return the resulting transformed image after both operations are performed.

### Approach and Logic
- Traverse each row of the image matrix.
- First, **reverse** the row to perform the horizontal flip.
- Then, **invert** each element by replacing `0` with `1` and `1` with `0`.
- You can perform both operations in a single pass using list comprehensions or nested loops.

This problem leverages basic list manipulation and bit inversion.

---
