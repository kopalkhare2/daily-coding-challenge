# LeetCode Solutions - README

This repository includes solutions for common LeetCode problems. Below are explanations for two questions with the logic and approach used to solve them.

## ✅ Problem 1: 169. Majority Element

### 🔗 Problem Link:
[Majority Element](https://leetcode.com/problems/majority-element/)

### 📄 Problem Statement:
Given an array `nums` of size `n`, return the **majority element**. The majority element is the element that appears more than `n / 2` times. It is guaranteed that a majority element always exists in the array.

### 💡 Logic and Approach:
We use the **Boyer-Moore Voting Algorithm**, which is efficient for finding the majority element in linear time and constant space.

#### 🔁 Steps:
1. Initialize `count = 0` and `candidate = None`.
2. Traverse the array:
   - If `count == 0`, assign the current number as the `candidate`.
   - If the current number is the same as the candidate, increment `count`.
   - Otherwise, decrement `count`.
3. At the end of traversal, the `candidate` is guaranteed to be the majority element.

## ✅ Problem 2: 1249. Minimum Remove to Make Valid Parentheses

### 🔗 Problem Link:
[Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

### 📄 Problem Statement:
Given a string `s` containing `'('`, `')'`, and lowercase letters, remove the **minimum number** of parentheses to make the input string valid. A valid string is:
- Empty or contains only lowercase letters.
- Can be expressed as `A(B)` or `AB` where both `A` and `B` are valid.

### 💡 Logic and Approach:
This is solved using a **stack** and a two-pass approach:

#### 🔁 Steps:
1. **First Pass (Left to Right)**:
   - Use a stack to track the indices of unmatched `'('`.
   - If a `')'` is found with no matching `'('`, mark its index for removal.
2. **Second Pass (Right to Left)**:
   - Remove any remaining unmatched `'('` in the stack by marking them.
3. **Final Step**:
   - Build the result string, skipping characters that were marked for removal.
