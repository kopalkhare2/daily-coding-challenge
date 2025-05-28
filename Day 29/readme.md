# 📘 LeetCode Problem Write-Up

Hey there! 👋  
This file explains how I approached and solved two LeetCode problems. I’ve broken down the logic and thought process behind each solution - the idea behind it.

---

## 🔸 1. Kth Largest Element in an Array (Problem 215)

### 🧠 What’s the Problem?
You’re given an array of integers and a number `k`. You need to return the **kth largest element** in that array.  
Important: It’s not the kth **unique** element—just the kth largest **overall** when the array is sorted.

### 💡 How I Approached It:
Sorting the entire array would work, but it’s not the most efficient way—especially when the array is big.  
So, I used a **heap** approach (specifically, Python’s `heapq.nlargest` method). This lets you pull out the top `k` largest numbers quickly.

Once you have those `k` numbers, the smallest among them (i.e., the last one) is the kth largest in the full array. Easy and efficient!

### ⏱️ Why It Works Well:
- We avoid full sorting (which is O(n log n)).
- This approach runs in O(n log k) time, which is faster when `k` is much smaller than `n`.

---

## 🔹 2. Sum of Left Leaves (Problem 404)

### 🧠 What’s the Problem?
Given a binary tree, you need to find the **sum of all the left leaves**.  
A “left leaf” means it’s a leaf node (no children) and it’s on the **left side** of its parent.

### 💡 How I Approached It:
I used a simple **recursive (DFS)** approach to walk through the tree.

At each node:
- I check if it has a left child.
- If it does, and that left child has **no children**, I add its value to the sum.
- Then I continue exploring both left and right subtrees.

This way, I don’t miss any left leaves no matter how deep or complex the tree is.

### ✅ Why It Makes Sense:
- It’s clean and easy to understand.
- Uses recursion to cover the whole tree.
- Only adds values of nodes that meet both conditions (left + leaf).

---

## 🚀 Wrap-Up

These two problems helped me practice:
- Efficient number selection using heaps.
- Tree traversal and understanding node conditions.
