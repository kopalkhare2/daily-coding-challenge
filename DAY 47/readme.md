# LeetCode Problem Summaries and Approaches

This document provides a brief overview of the logic and approach for solving two LeetCode problems:  
1. **1358. Number of Substrings Containing All Three Characters**  
2. **191. Number of 1 Bits**

---

## 🟠 1358. Number of Substrings Containing All Three Characters

### ✅ Problem Statement
Given a string `s` consisting only of characters `a`, `b`, and `c`, return the number of substrings that contain at least one occurrence of each of the characters.

### 🔍 Logic & Approach

- This problem is best tackled using the **sliding window technique**.
- Maintain a window using two pointers (`left` and `right`) and a frequency counter for characters `a`, `b`, and `c`.
- As you iterate using the `right` pointer, increment the count of the current character.
- Once all three characters are present at least once within the window, calculate how many substrings ending at the current `right` can be formed by shrinking the window from the `left`.
- The key idea is: as soon as a valid window is found, any further substring starting from the current `left` to `right` (inclusive) and extending beyond will also be valid.
- Continue shrinking the window from the left until it becomes invalid again.
- Sum all such valid substring counts to get the final answer.

---

## 🟢 191. Number of 1 Bits

### ✅ Problem Statement
Given an integer `n`, return the number of set bits (1s) in its binary representation, also known as the Hamming weight.

### 🔍 Logic & Approach

- The task is to **count the number of bits set to 1** in the binary form of an unsigned integer.
- A common approach is to **use bitwise AND** to isolate the rightmost 1-bit.
- Continuously perform `n & 1` to check if the last bit is 1, and right-shift the number (`n >>= 1`) until it becomes 0.
- Alternatively, more optimized solutions may involve **Brian Kernighan’s Algorithm**: repeatedly apply `n = n & (n - 1)` which removes the lowest set bit in each iteration, incrementing the counter until `n` becomes zero.
- Both approaches achieve a time-efficient solution, particularly suitable for fixed-width integers.

---

📌 These summaries are designed to reinforce your problem-solving understanding without exposing full code solutions. The logic focuses on optimal strategies and reasoning techniques used in top submissions.
