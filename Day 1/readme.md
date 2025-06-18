# LeetCode Solutions: Missing Number & Reverse Linked List

This document explains the logic and approach for solving two common LeetCode problems using C++.

---

## 🧩 Problem 1: Missing Number (LeetCode 268)

### 🔍 Problem Statement:
Given an array containing `n` distinct numbers in the range `[0, n]`, find the one number that is missing from the array.

### 💡 Logic & Approach:

To solve this problem, we use a mathematical approach:

1. **Mathematical Sum Formula**:
   - The sum of the first `n` natural numbers (including 0) is given by the formula:  
     \[
     \text{Sum}_{expected} = \frac{n \cdot (n + 1)}{2}
     \]
   - Where `n` is the length of the array.

2. **Actual Sum**:
   - Calculate the sum of all numbers present in the input array.

3. **Missing Number**:
   - Subtract the actual sum from the expected sum:
     \[
     \text{Missing Number} = \text{Sum}_{expected} - \text{Sum}_{actual}
     \]

This approach works in **O(n)** time and **O(1)** space.

---

## 🔄 Problem 2: Reverse Linked List (LeetCode 206)

### 🔍 Problem Statement:
Given the head of a singly linked list, reverse the list and return the new head.

### 💡 Logic & Approach:

To reverse a singly linked list, we use an **iterative pointer-based approach**:

1. **Initialize Three Pointers**:
   - `prev` to store the previous node (initially `nullptr`)
   - `curr` to track the current node (starting from `head`)
   - `nextNode` to temporarily hold the next node

2. **Traversal and Rewiring**:
   - Loop through the list:
     - Save the next node.
     - Reverse the current node’s pointer to point to the previous node.
     - Move `prev` and `curr` one step forward.

3. **Return New Head**:
   - At the end of the loop, `prev` will point to the new head of the reversed list.

This method has **O(n)** time complexity and **O(1)** space complexity.

---

### ✅ Notes:
- These problems are tagged as **Easy**, yet they are fundamental for building deeper understanding in algorithms and data structures.
- Mastering these patterns helps with more complex problems like cycle detection, sorting-based problems, and linked list operations.

