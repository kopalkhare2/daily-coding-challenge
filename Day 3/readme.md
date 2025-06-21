# LeetCode Problem Solving – Approaches & Logic

This README summarizes the problem-solving approach and core logic behind two classic LeetCode problems:  
1. **Merge Two Sorted Lists**
2. **Perfect Number**

---

## 1. Merge Two Sorted Lists

### 🔍 Problem Overview:
Given two sorted singly linked lists, the task is to merge them into one sorted linked list by splicing together their nodes without allocating extra space for new nodes.

### 🧠 Approach:
- Use a **dummy node** to simplify edge-case handling and act as a fixed starting point.
- Maintain a pointer (`tail`) that builds the merged list by comparing the current nodes of both input lists.
- At each step:
  - Compare the current node values of `list1` and `list2`.
  - Append the node with the smaller value to `tail->next`.
  - Advance the pointer of the list from which the node was selected.
- Once either list is exhausted, append the remaining nodes of the other list.
- Return the merged list starting from `dummy.next`.

### ✅ Why This Works:
- It preserves the sorted order due to the element-wise comparison.
- The dummy node ensures clean pointer manipulation without needing special handling for the head.

---

## 2. Perfect Number

### 🔍 Problem Overview:
A perfect number is a **positive integer equal to the sum of its proper positive divisors**, excluding the number itself.

### 🧠 Approach:
- Handle edge case: numbers less than or equal to 1 can’t be perfect numbers.
- Initialize a sum starting with 1 (since 1 is a divisor of all numbers >1).
- Iterate from 2 up to √num (square root of the number):
  - For each `i` that divides `num`:
    - Add both `i` and `num / i` to the sum (if they are different).
- After the loop, compare the sum of divisors to `num`.

### ✅ Why This Works:
- Any divisor pair `(i, num/i)` contributes to the total divisor sum.
- Looping only up to √num keeps the algorithm efficient (O(√n) time complexity).
- Avoids unnecessary checks and duplication of divisors.

---
