# LeetCode Practice Notes

---

## 🚩 Problem 48: Rotate Image (Medium)

### 🔸 Description:
Given an `n x n` 2D matrix representing an image, rotate the image **90 degrees clockwise**.  
You must perform the rotation **in-place**, i.e., modify the input 2D matrix directly without allocating another matrix.

### 📊 Constraints:
- Do **not** use extra space.
- Matrix must be rotated in-place.

### 💡 Logic:

To rotate a matrix 90° clockwise **in-place**, follow two main steps:

1. **Transpose the matrix**: convert all `matrix[i][j]` into `matrix[j][i]`
2. **Reverse each row** of the matrix

These steps mimic the rotation effect without using extra space.

---

## ✅ Problem 101: Symmetric Tree (Easy)

### 🔸 Description:
Given the `root` of a binary tree, check whether it is a **mirror of itself** (i.e., symmetric around its center).

### 💡 Logic:

A tree is symmetric if:
- Its left and right subtrees are mirrors of each other.

To verify symmetry, define a helper function that:
- Recursively compares the left subtree of the left node with the right subtree of the right node (and vice versa)
- Returns `true` if all mirrored pairs match in value and structure

### 🔄 Recursive Conditions:
- If both nodes are `null` → return `true`
- If only one is `null` → return `false`
- If values differ → return `false`
- Else → recursively check:
  - `left->left` vs `right->right`
  - `left->right` vs `right->left`

---
