# LeetCode Problem Summaries

## ✅ 1250. Check If It Is a Good Array

### 🔍 Problem Statement
Given an array of positive integers, determine whether it's possible to obtain a sum of 1 from any subset of the array by multiplying each element with some integer and summing the results.

### 💡 Logic & Approach
This problem reduces to checking whether it's possible to obtain a linear combination of the array elements that equals 1. By **Bézout’s identity**, this is only possible if the **Greatest Common Divisor (GCD)** of the array is 1.

- Start with the first element.
- Iteratively compute the GCD of the current result with the next number.
- If the final GCD is 1, return `true` (array is good), else `false`.

This approach is efficient and leverages fundamental number theory.

---

## ✅ 461. Hamming Distance

### 🔍 Problem Statement
Calculate the Hamming distance between two integers, which is the number of positions at which the corresponding bits are different.

### 💡 Logic & Approach
To compute the Hamming distance:
1. Use the **bitwise XOR (^)** of the two numbers. This operation highlights the differing bits as 1.
2. Count the number of set bits (1s) in the XOR result.

This count gives the total number of differing positions (i.e., the Hamming distance). The bitwise operations ensure the solution is optimal in terms of performance.

---
