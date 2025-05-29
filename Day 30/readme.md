# Problem Overviews & Approaches

This write-up covers the thought process and approach behind solving two popular LeetCode problems. The goal is to explain the intuition behind each solution in a way that's easy to understand—even if you're just revisiting the problems after a while.

---

## 🔹 1. Diameter of a Binary Tree (LeetCode 543)

### 📝 What's the problem?

You're given the root of a binary tree and asked to find its diameter. The diameter here means the longest path between any two nodes in the tree. Keep in mind, this path doesn't necessarily have to pass through the root.

Also, "length" means the number of **edges**, not nodes.

### 💡 What's the idea?

The key insight is to realize that for any given node, the **longest path** that passes through it is the sum of the heights of its left and right subtrees. So, if we can figure that out for every node, we can track the maximum value among them.

We use a recursive function that:
- Computes the height of each subtree.
- While doing so, updates a global maximum whenever it finds a longer path (left height + right height).

### ⏱️ How efficient is it?

- **Time complexity:** O(n) — because we visit each node once.
- **Space complexity:** O(h), where `h` is the height of the tree (due to recursion stack).

---

## 🔹 2. Find the Duplicate Number (LeetCode 287)

### 📝 What's the problem?

You’re given an array of `n + 1` integers where each number is in the range `1` to `n`. That means at least one number is repeated. The task is to find that duplicate **without changing the array**, and using only **constant space**.

### 💡 What's the idea?

This problem looks like it's about arrays, but a clever trick is to treat it like a **cycle detection** problem in a linked list.

Imagine each number in the array as a pointer to another index (i.e., `nums[i]` points to `nums[nums[i]]`). This forms a cycle because one number is repeated, meaning two "pointers" lead to the same place.

We can use **Floyd's Tortoise and Hare** algorithm:
1. Move a slow and fast pointer until they meet — this confirms there's a cycle.
2. Reset one pointer to the beginning, and move both one step at a time — they'll meet again at the start of the cycle, which is the duplicate number.

### ⏱️ How efficient is it?

- **Time complexity:** O(n) — we go through the array at most twice.
- **Space complexity:** O(1) — we use only two pointers.

---

