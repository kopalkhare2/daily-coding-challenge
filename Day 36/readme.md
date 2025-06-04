# LeetCode Problem Solutions

This repository contains structured explanations and approaches for solving selected LeetCode problems.

---

## 📘 Problem 1: 129. Sum Root to Leaf Numbers

### 📝 Problem Statement
You are given the root of a binary tree where each node contains a digit from 0 to 9. Each root-to-leaf path represents a number created by concatenating the digits along the path. The task is to return the total sum of all such numbers formed from root to leaf paths.

### 💡 Logic
Each path from the root to a leaf node forms a number by progressively appending digits (just like forming a number in base-10). At every node, the current number is updated as `current = current * 10 + node value`. Once a leaf node is reached, that number is finalized and added to the total.

### 🧠 Approach
- Implement a **recursive DFS** function.
- Use a `current` variable to track the path number as you traverse.
- When you reach a leaf node (no left or right children), return the current number.
- Recursively call the function for left and right subtrees.
- Add the results of left and right subtrees to obtain the final sum.

---

## 📗 Problem 2: 345. Reverse Vowels of a String

### 📝 Problem Statement
Given a string `s`, reverse only the vowels in the string and return the new string. Vowels include: `'a', 'e', 'i', 'o', 'u'` and their uppercase versions.

### 💡 Logic
The order of all characters should remain the same except the vowels, which need to be reversed in-place. This can be achieved efficiently using two pointers scanning from both ends.

### 🧠 Approach
- Use two pointers (`left` and `right`) to traverse the string from both ends.
- Convert the string to a list to allow in-place character swapping.
- Move `left` forward until it points to a vowel.
- Move `right` backward until it points to a vowel.
- Swap the characters at `left` and `right` pointers.
- Repeat the process until `left` meets or crosses `right`.
- Join the list to return the final modified string.
