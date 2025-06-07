# LeetCode Problem Solutions 📘

This repository contains clean, accepted solutions to selected LeetCode problems using Python and C++. Each problem includes a summary of the approach and logic used.

---

## ✅ Problem 1: [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
**Difficulty:** Easy  
**Language Used:** Python

### 🧩 Description:
Given a string `s` consisting of lowercase English letters, the task is to repeatedly remove pairs of adjacent, equal letters until no such pairs remain.

### 🧠 Approach:
- Use a **stack** data structure.
- Traverse each character in the string:
  - If the top of the stack matches the current character, pop it (remove the pair).
  - Otherwise, push the character onto the stack.
- Join the stack at the end to get the final result.

---

## ✅ Problem 2: [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
**Difficulty:** Medium  
**Language Used:** C++

### 🧩 Description:
Given the root of a Binary Search Tree (BST) and a value to insert, return the updated root node after the insertion. It is guaranteed that the new value does not exist in the tree.

### 🧠 Approach:
- Apply **recursive traversal** to find the correct position.
- If the root is null, insert the new node here.
- If the value is smaller than the root's value, recurse into the left subtree.
- If the value is greater, recurse into the right subtree.
- Return the root after insertion.

---

## 🛠️ Tools Used
- LeetCode Online Judge
- Python and C++ IDEs

---

## ✨ Author
**Kopal Khare**  
B.Tech Artificial Intelligence & Machine Learning, VIT Bhopal  
GitHub: [your-profile-link]  
Email: [your-email@example.com]

---

## 📌 Notes
- Solutions are optimized for runtime and accepted with 0 ms in submissions.
- This repository will be continuously updated with more problems and approaches.
