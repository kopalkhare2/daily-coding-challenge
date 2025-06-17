# 🧠 LeetCode Practice Solutions

This repository contains clean and optimized solutions to selected LeetCode problems, including the approach and logic behind each solution.

---

## ✅ Problem 1: 136. Single Number

### 🔍 Problem Statement
Given a **non-empty** array of integers, every element appears **twice** except for one. Find that single one.  
The solution must have **linear runtime complexity** and use only **constant extra space**.

### 💡 Approach & Logic

This problem can be efficiently solved using the **bitwise XOR operator (^)**.

- XOR of a number with itself is `0` → `a ^ a = 0`
- XOR of a number with 0 is the number itself → `a ^ 0 = a`
- XOR is **commutative** and **associative**, so the order doesn’t matter.

**Strategy:**
- Initialize a variable `result = 0`.
- Traverse the array and XOR every element with `result`.
- Duplicate numbers cancel out, and the result will hold the number that appears only once.

### ✅ Time Complexity
- **O(n)** — Traverse the list once.

### ✅ Space Complexity
- **O(1)** — Uses constant space.

---

## ✅ Problem 2: 204. Count Primes

### 🔍 Problem Statement
Given an integer `n`, return the number of prime numbers that are **strictly less than** `n`.

### 💡 Approach & Logic

Use the **Sieve of Eratosthenes** algorithm — an efficient way to find all primes less than a given limit.

**Strategy:**
1. Create a boolean list `isPrime` of size `n` and initialize all entries to `true`.
2. Set `isPrime[0]` and `isPrime[1]` to `false`, since 0 and 1 are not prime.
3. For every number `i` starting from 2:
   - If `isPrime[i]` is still true, mark all multiples of `i` (starting from `i*i`) as `false`.
4. Finally, count how many entries in `isPrime` are `true`.

This technique avoids redundant checks and improves performance over checking each number individually.

### ✅ Time Complexity
- **O(n log log n)** — Optimized sieve runtime.

### ✅ Space Complexity
- **O(n)** — For storing the primality of numbers.

---
