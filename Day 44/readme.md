# LeetCode Problem Solving Summary

## ✅ Problem 1: Convert Sorted List to Binary Search Tree

- **Problem Link**: [LeetCode 109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)
- **Difficulty**: Medium
- **Tags**: Linked List, Depth-First Search, Binary Search Tree, Divide and Conquer

### 🔍 Logic and Approach

The task is to convert a sorted singly linked list into a height-balanced Binary Search Tree (BST). A height-balanced BST ensures the depth of two subtrees of every node never differs by more than 1.

To achieve this:
- Use the slow and fast pointer technique to find the middle node of the list, which becomes the root of the BST.
- Recursively apply the same strategy to the left half (before mid) and right half (after mid) of the list to form left and right subtrees.
- Ensure list connections are broken appropriately during recursive splitting to maintain tree structure.

This divide-and-conquer approach ensures balance and adheres to BST rules.

---

## ✅ Problem 2: Maximum Number of Vowels in a Substring of Given Length

- **Problem Link**: [LeetCode 1456](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
- **Difficulty**: Medium
- **Tags**: String, Sliding Window

### 🔍 Logic and Approach

The goal is to find the maximum number of vowels present in any substring of length `k` in a given string `s`.

To do this efficiently:
- Use a **sliding window** approach of size `k`.
- Initially count the vowels in the first `k` characters.
- Slide the window one character at a time:
  - Add the new character to the count if it's a vowel.
  - Subtract the character going out of the window if it was a vowel.
- Keep track of the maximum number of vowels encountered in any window throughout the process.

This method ensures linear time complexity `O(n)`, making it optimal for large strings.

---
