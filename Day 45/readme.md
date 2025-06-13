# LeetCode Problem Solutions

## ✅ 1071. Greatest Common Divisor of Strings

### Problem Statement
Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.  
A string `t` divides string `s` if `s = t + t + ... + t` (t repeated one or more times).

### Logic
- The only way two strings can have a common divisor string is if concatenating them in both orders gives the same result (`str1 + str2 == str2 + str1`).
- If the above condition is met, the answer will be the substring from the beginning of the string of length equal to the greatest common divisor (GCD) of the lengths of `str1` and `str2`.

### Approach
- Check if `str1 + str2 == str2 + str1`.
- If not, return an empty string.
- If yes, compute `gcd(len(str1), len(str2))`.
- Return the substring `str1[0:gcd_length]` as the result.


---

## ✅ 997. Find the Town Judge

### Problem Statement
In a town with `n` people labeled `1` to `n`, one person is the judge if:
1. The judge trusts nobody.
2. Everybody else trusts the judge.
3. Exactly one person satisfies both conditions.

### Logic
- The judge will have a **net trust score** of `n-1` (trusted by everyone except themselves, and trusts nobody).
- Every other person will have a **net trust score** less than `n-1`.

### Approach
- Create a trust score list initialized to zero.
- For every pair `[a, b]` in the trust list:
  - Decrease trust score for `a` (since `a` trusts someone).
  - Increase trust score for `b` (since `b` is being trusted).
- Traverse the trust score array:
  - Return the person with a trust score equal to `n-1`.
- If no such person exists, return `-1`.
