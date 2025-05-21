# LeetCode Solutions - README

This repository contains my solutions to some frequently encountered LeetCode problems. Below, I’ve shared detailed explanations for two problems, including the reasoning behind the approaches I used to solve them.


## ✅ Problem 1: 169. Majority Element

### 🔗 Problem Link:  
[Majority Element](https://leetcode.com/problems/majority-element/)

### 📄 Problem Overview:  
You’re given an array `nums` containing `n` elements. Your task is to find the element that appears more than half the time in the array — this is known as the majority element. The problem guarantees that such an element always exists.

### 💡 How I Approached It:  
To solve this efficiently, I used the **Boyer-Moore Voting Algorithm**. This clever algorithm lets you identify the majority element in a single pass using constant extra space.

#### Step-by-step Explanation:  
1. Keep two variables: a `candidate` for the majority element and a `count` to track its dominance.  
2. Iterate over each number in the array:  
   - If `count` is zero, pick the current number as the new candidate.  
   - If the current number matches the candidate, increase `count`.  
   - Otherwise, decrease `count`.  
3. By the end of this process, the candidate will be the majority element.

This works because every time you encounter a number different from your candidate, you "cancel out" one occurrence of the candidate. Since the majority element appears more than half the time, it will always remain by the end.

## ✅ Problem 2: 1249. Minimum Remove to Make Valid Parentheses

### 🔗 Problem Link:  
[Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

### 📄 Problem Overview:  
Given a string that contains lowercase letters and parentheses `(` and `)`, the goal is to remove the fewest parentheses possible to make the string valid. A valid string means:  
- It contains only lowercase letters or,  
- Parentheses are balanced and properly nested.

### 💡 How I Approached It:  
I tackled this with a two-pass technique using a stack to keep track of unmatched parentheses.

#### Step-by-step Explanation:  
1. **First pass (left to right):**  
   - Walk through the string, pushing the indices of each `'('` onto a stack.  
   - When you encounter a `')'`, check the stack:  
     - If the stack isn’t empty, pop one `'('` off because you found a match.  
     - If it is empty, mark this `')'` as invalid (because it has no matching `'('`).  
2. **Second pass (right to left):**  
   - After the first pass, any indices left in the stack represent unmatched `'('`. Mark these for removal.  
3. **Build the result:**  
   - Construct a new string by skipping all the characters marked for removal.

This approach ensures only the minimum number of parentheses are removed while keeping the rest of the string intact and valid.

