# Leetcode Solutions

This repository contains well-explained solutions for the following Leetcode problems:

1. **1791. Find Center of Star Graph**
2. **762. Prime Number of Set Bits in Binary Representation**

---

## 🌟 1791. Find Center of Star Graph

### 🧠 Logic
In a star graph, there is one central node that is connected to all other nodes. This means the center node will appear in every edge. By examining just the first two edges, the common node between them must be the center of the graph.

### 🔍 Approach
- Compare the first two edges.
- Identify the common node between them.
- Return the common node as the center.
- This works because only the center node is connected to all others.

---

## 🔢 762. Prime Number of Set Bits in Binary Representation

### 🧠 Logic
The goal is to count numbers in a given range `[left, right]` such that the number of 1's in their binary representation (set bits) is a **prime number**. A prime number has no divisors other than 1 and itself.

### 🔍 Approach
- Iterate through each number from `left` to `right`.
- Convert each number to its binary representation.
- Count the number of set bits (1’s).
- Check if this count is a prime number.
- Maintain a counter for how many numbers meet the condition.

---

📁 This file explains the core logic and approach for both problems without diving into implementation or examples, making it suitable for revision and documentation purposes.
