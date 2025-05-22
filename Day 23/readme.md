#  Leetcode Problem 35: Search Insert Position

**Difficulty:** Easy  
**Problem Link:** [Leetcode 35 - Search Insert Position](https://leetcode.com/problems/search-insert-position/)

##  Problem Statement

Given a sorted array of **distinct integers** and a **target** value, return the **index** if the target is found.  
If not, return the **index where it would be if it were inserted in order**.

You **must** write an algorithm with **O(log n)** runtime complexity.

## Approach: Binary Search

Since the input array is **sorted in ascending order**, the most optimal approach is to use **Binary Search**.

## Logic

1. Initialize two pointers:
   - `left = 0`
   - `right = nums.size() - 1`

2. Use a **while loop** to perform binary search:
   - Calculate `mid = left + (right - left) / 2`
   - If `nums[mid] == target`:  
     → Return `mid` (target found)
   - If `nums[mid] < target`:  
     → Search right half → `left = mid + 1`
   - If `nums[mid] > target`:  
     → Search left half → `right = mid - 1`

3. If target is not found in the loop:  
   → Return `left` as the correct **insertion index**.

This works because `left` will end up at the first index where `nums[left] >= target`.

# LeetCode Problem 32: Longest Valid Parentheses

##  Problem Statement

Given a string containing just the characters `'('` and `')'`, return the length of the **longest valid (well-formed)** parentheses substring.

##  Approach: Stack-based Method

We use a **stack** to store indices and track valid open parentheses `'('`.

###  Steps:
1. Initialize a stack and push `-1` as a base index.
2. Traverse the string character by character:
   - If `'('` is found → push its index to the stack.
   - If `')'` is found → pop the top (match with `'('`):
     - If the stack becomes empty → push the current index (reset base).
     - Else → calculate `i - st.top()` and update max length.
3. Return the maximum length found.
