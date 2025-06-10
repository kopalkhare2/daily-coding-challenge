# LeetCode Problem Explanations

## 1. Problem 98: Validate Binary Search Tree

### 🧠 Logic:
A Binary Search Tree (BST) is a binary tree where:
- The left subtree of any node contains only nodes with values **less than** the node’s value.
- The right subtree of any node contains only nodes with values **greater than** the node’s value.
- Both left and right subtrees must themselves also be BSTs.

This property must hold **recursively for every node** in the tree.

### 🛠️ Approach:
Use recursion to traverse the tree and validate that each node's value falls within a specified range:
- For the root node, the valid range is `(-∞, ∞)`.
- For the left child, the range becomes `(min, current_node_value)`.
- For the right child, the range becomes `(current_node_value, max)`.
If at any point a node violates this constraint, return `false`. Otherwise, continue the recursion.

Alternatively, an **inorder traversal** can be used to ensure that the node values are strictly increasing — which is a characteristic of BSTs when traversed inorder.

---

## 2. Problem 151: Reverse Words in a String

### 🧠 Logic:
The task is to reverse the order of words in a given string. Words are defined as sequences of non-space characters. The output must:
- Contain all words in reverse order.
- Have only a **single space** between words.
- **Exclude** leading, trailing, and extra spaces between words.

### 🛠️ Approach:
The solution involves:
1. **Trimming** the input string to remove leading and trailing spaces.
2. **Splitting** the string by whitespace to extract all words.
3. **Reversing** the list of words.
4. **Joining** the reversed list with a single space to form the final output.

This approach ensures that extra spaces are removed and the words are correctly reversed.

---
