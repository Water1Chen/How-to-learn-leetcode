"""
LC 32. Longest Valid Parentheses (最长有效括号)
Difficulty: Hard
Tags: String, Dynamic Programming, Stack
Link: https://leetcode.cn/problems/longest-valid-parentheses/
Category: 15-dp
"""


# ===== 方法一：栈 =====
# 思路: 使用栈来匹配括号，栈中存储的是括号的索引。遇到'('时将索引入栈，
#        遇到')'时弹出栈顶元素，如果栈为空则将当前索引入栈作为新的基准，
#        否则用当前索引减去栈顶索引即为当前有效括号长度。
# 复杂度: O(n) time, O(n) space
def solution_stack(s: str) -> int:
    # WHY: 初始化最大长度为0
    max_len = 0
    # WHY: 使用列表作为栈，存储括号索引，初始放入-1作为基准（处理边界）
    stack = [-1]
    # WHY: 遍历字符串中的每个字符及其索引
    for i, ch in enumerate(s):
        # WHY: 如果是左括号，将其索引入栈
        if ch == '(':
            stack.append(i)
        else:
            # WHY: 遇到右括号，弹出栈顶元素（匹配左括号或基准）
            stack.pop()
            # WHY: 如果栈为空，说明没有左括号可匹配，将当前索引入栈作为新的基准
            if not stack:
                stack.append(i)
            else:
                # WHY: 栈不为空，当前索引减去栈顶索引即为有效括号长度
                max_len = max(max_len, i - stack[-1])
    # WHY: 返回最大长度
    return max_len


# ===== 方法二：动态规划 =====
# 思路: dp[i]表示以s[i]结尾的最长有效括号子串的长度。根据s[i]是')'的情况讨论：
#        如果s[i-1]='('，则dp[i] = dp[i-2] + 2；
#        如果s[i-1]=')'且s[i-dp[i-1]-1]='('，则dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2。
# 复杂度: O(n) time, O(n) space
def solution_dp(s: str) -> int:
    # WHY: 初始化最大长度为0
    max_len = 0
    # WHY: dp[i]表示以s[i]结尾的最长有效括号子串长度
    dp = [0] * len(s)
    # WHY: 从索引1开始遍历（长度至少为2才能形成括号对）
    for i in range(1, len(s)):
        # WHY: 只有右括号才可能形成有效的括号对
        if s[i] == ')':
            # WHY: 情况1：前一个字符是'('，形如"...()"
            if s[i - 1] == '(':
                # WHY: dp[i] = dp[i-2] + 2（如果i>=2，否则直接为2）
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            else:
                # WHY: 情况2：前一个字符是')'，形如"...))"，需要检查i-dp[i-1]-1是否是'('
                # WHY: i-dp[i-1]-1是与当前')'配对的左括号位置
                left = i - dp[i - 1] - 1
                if left >= 0 and s[left] == '(':
                    # WHY: dp[i] = dp[i-1] + 内部有效长度 + dp[left-1] + 2
                    dp[i] = dp[i - 1] + (dp[left - 1] if left >= 1 else 0) + 2
            # WHY: 更新全局最大长度
            max_len = max(max_len, dp[i])
    # WHY: 返回最大长度
    return max_len


# ===== 方法三：双指针计数（最优 O(1) 空间）=====
# 思路: 从左到右扫描，用left和right分别计数左括号和右括号的数量。
#        当left == right时，更新最大长度；当right > left时，重置计数。
#        再从右到左扫描一次处理"(()"这种情况。
# 复杂度: O(n) time, O(1) space
def solution_optimal(s: str) -> int:
    # WHY: 初始化最大长度、左括号计数和右括号计数
    max_len = 0
    left = 0
    right = 0
    # WHY: 从左到右扫描
    for ch in s:
        # WHY: 统计左右括号数量
        if ch == '(':
            left += 1
        else:
            right += 1
        # WHY: 如果左右括号数量相等，更新最大长度
        if left == right:
            max_len = max(max_len, 2 * right)
        # WHY: 如果右括号多于左括号，重置计数（当前子串无效）
        elif right > left:
            left = 0
            right = 0
    # WHY: 重置计数，从右到左再扫描一次（处理左括号多于右括号的情况，如"(()"）
    left = 0
    right = 0
    # WHY: 从右到左遍历字符串
    for ch in reversed(s):
        # WHY: 统计左右括号数量（注意方向反了）
        if ch == '(':
            left += 1
        else:
            right += 1
        # WHY: 如果左右括号数量相等，更新最大长度
        if left == right:
            max_len = max(max_len, 2 * left)
        # WHY: 如果左括号多于右括号（从右往左右括号多意味着无效），重置计数
        elif left > right:
            left = 0
            right = 0
    # WHY: 返回最大长度
    return max_len


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Longest Valid Parentheses...")

    # 测试用例1: "(()" → 2 (有效子串"()")
    test1 = "(()"
    expected1 = 2
    assert solution_stack(test1) == expected1, f"stack test1 failed"
    assert solution_dp(test1) == expected1, f"dp test1 failed"
    assert solution_optimal(test1) == expected1, f"optimal test1 failed"

    # 测试用例2: ")()())" → 4 (有效子串"()()")
    test2 = ")()())"
    expected2 = 4
    assert solution_stack(test2) == expected2, f"stack test2 failed"
    assert solution_dp(test2) == expected2, f"dp test2 failed"
    assert solution_optimal(test2) == expected2, f"optimal test2 failed"

    # 测试用例3: "" → 0
    test3 = ""
    expected3 = 0
    assert solution_stack(test3) == expected3, f"stack test3 failed"
    assert solution_dp(test3) == expected3, f"dp test3 failed"
    assert solution_optimal(test3) == expected3, f"optimal test3 failed"

    print(f"Stack method: {solution_stack(test1)}")
    print(f"DP method: {solution_dp(test1)}")
    print(f"Two-pass method: {solution_optimal(test1)}")
    print("All tests passed!")
