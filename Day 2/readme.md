# 📘 LeetCode Problem Explanations

This repository contains my approach and logic for solving selected LeetCode problems efficiently, without including full code or examples.

---

## ✅ [258. Add Digits](https://leetcode.com/problems/add-digits/)

### 🧩 Problem Summary:
Given a non-negative integer `num`, repeatedly add its digits until the result has only one digit. Return that final single digit.

### 💡 Logic and Approach:
- This problem is based on the mathematical concept of the **digital root**.
- Instead of repeatedly summing digits with loops or recursion, we can use a **constant time formula**:
  - If `num == 0`, return `0`.
  - Otherwise, return `1 + (num - 1) % 9`.
- This works because every number in base-10 reduces to a pattern that repeats every 9 steps.

### 🧠 Insight:
- No loops or recursion are needed.
- The formula is derived from modular arithmetic and number theory.
- Time complexity: **O(1)**  
- Space complexity: **O(1)**

---

## ✅ [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

### 🧩 Problem Summary:
Given the head of a singly linked list, return the **middle node**. If there are two middle nodes, return the **second** one.

### 💡 Logic and Approach:
- Use the **two-pointer technique**:
  - `slow` moves one step at a time.
  - `fast` moves two steps at a time.
- When `fast` reaches the end of the list, `slow` will be at the middle.
- For even-length lists, `slow` naturally reaches the **second middle node** as required.

### 🧠 Insight:
- This approach requires only one traversal of the list.
- It works for both odd and even-length lists.
- Time complexity: **O(n)**  
- Space complexity: **O(1)**

---
