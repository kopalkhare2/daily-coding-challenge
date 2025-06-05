# LeetCode Problem Summaries

This repository documents the understanding, logic, and approach behind solutions to selected LeetCode problems.

---

## ✅ Problem: 2108. Find First Palindromic String in the Array

**Difficulty**: Easy  
**Topic**: Strings

---

### 🧠 Problem Summary
You are given an array of strings. Your task is to return the **first palindromic string** in the array.  
A string is **palindromic** if it reads the same forward and backward.  
If no palindrome exists in the array, return an empty string.

---

### ⚙️ Logic
- A palindrome is a word that equals its reverse.
- We need to go through the list and return the **first** such word.
- If none match, we return `""`.

---

### 🚀 Approach
1. Loop through each word in the given list of strings.
2. For each word, check if it equals its reverse (`word[::-1]`).
3. If a palindrome is found, return it immediately.
4. If the loop completes with no matches, return an empty string.

---

## ✅ Problem: 103. Binary Tree Zigzag Level Order Traversal

**Difficulty**: Medium  
**Topic**: Binary Tree, Breadth-First Search (BFS)

---

### 🧠 Problem Summary
Perform a **zigzag level order traversal** of a binary tree.  
Zigzag means:  
- Traverse one level **left to right**,  
- Then the next level **right to left**,  
- Then again **left to right**, and so on...

---

### ⚙️ Logic
- The traversal is similar to a **level order BFS**, but with an alternating direction.
- Use a queue to traverse the tree level by level.
- At each level, insert elements in order or reversed order depending on the current direction.

---

### 🚀 Approach
1. Initialize an empty queue and push the root node.
2. Use a boolean flag `leftToRight` starting as `true`.
3. While the queue is not empty:
   - Determine the number of nodes at the current level.
   - Initialize an empty list for that level.
   - For each node:
     - Pop from the queue.
     - Add its value to the list.
     - Enqueue left and right children if present.
   - If `leftToRight` is `false`, reverse the level list before appending to result.
   - Toggle `leftToRight` for the next level.
4. Continue until all nodes are processed.
5. Return the final result list containing the zigzag order traversal.

---
