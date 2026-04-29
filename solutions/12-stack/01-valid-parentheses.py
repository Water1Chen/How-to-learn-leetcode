"""
LC 20. Valid Parentheses (有效的括号)
Difficulty: Easy
Tags: String, Stack
Link: https://leetcode.cn/problems/valid-parentheses/
Category: stack
"""


# ===== 暴力解法 =====
# 思路: Repeatedly replace matching bracket pairs ("()", "[]", "{}") with empty string
#       until no more replacements can be made. If the final string is empty, it's valid.
# 复杂度: O(n^2) time, O(n) space for string copies
def solution_brute(s: str) -> bool:
    """
    Check if parentheses string is valid by repeatedly replacing pairs.
    """
    # WHY: Work with a mutable copy of the string
    result: str = s

    # WHY: Keep replacing pairs until no more replacements occur
    while True:
        # WHY: Track the current length to detect if any replacement happened
        prev_len: int = len(result)

        # WHY: Replace all three types of matching bracket pairs
        result = result.replace("()", "")
        result = result.replace("[]", "")
        result = result.replace("{}", "")

        # WHY: If length unchanged, no more pairs to replace — terminate
        if len(result) == prev_len:
            break

    # WHY: Valid if all brackets were eliminated (empty string)
    return result == ""


# ===== 最优解法 =====
# 思路: Use a stack. When encountering an opening bracket, push it onto the stack.
#       When encountering a closing bracket, check if it matches the top of the stack.
#       If it matches, pop; otherwise invalid. At the end, the stack must be empty.
# 复杂度: O(n) time, O(n) space for the stack
def solution_optimal(s: str) -> bool:
    """
    Check if parentheses string is valid using a stack.
    """
    # WHY: Mapping of closing brackets to their corresponding opening brackets
    matching: dict = {')': '(', '}': '{', ']': '['}
    # WHY: Stack to track unmatched opening brackets
    stack: list = []

    # WHY: Iterate through each character in the input string
    for char in s:
        # WHY: If character is a closing bracket, it should match the top of stack
        if char in matching:
            # WHY: Get the expected opening bracket from the mapping
            expected: str = matching[char]
            # WHY: If stack is empty or top doesn't match, string is invalid
            if not stack or stack[-1] != expected:
                return False
            # WHY: Pop the matched opening bracket from stack
            stack.pop()
        else:
            # WHY: Character is an opening bracket — push onto stack
            stack.append(char)

    # WHY: Valid only if all opening brackets were matched (stack empty)
    return not stack


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Valid Parentheses...")

    # Test case 1: Valid string with all bracket types
    assert solution_optimal("()[]{}") == True, "Test 1 optimal failed"
    assert solution_brute("()[]{}") == True, "Test 1 brute failed"
    print("Test 1 (\"()[]{}\" -> true) passed!")

    # Test case 2: Invalid — unmatched opening bracket
    assert solution_optimal("(]") == False, "Test 2 optimal failed"
    assert solution_brute("(]") == False, "Test 2 brute failed"
    print("Test 2 (\"(]\" -> false) passed!")

    # Test case 3: Invalid — wrong order
    assert solution_optimal("([)]") == False, "Test 3 optimal failed"
    assert solution_brute("([)]") == False, "Test 3 brute failed"
    print("Test 3 (\"([)]\" -> false) passed!")

    # Test case 4: Nested valid brackets
    assert solution_optimal("{[]}") == True, "Test 4 optimal failed"
    assert solution_brute("{[]}") == True, "Test 4 brute failed"
    print("Test 4 (\"{[]}\" -> true) passed!")

    # Test case 5: Empty string (valid)
    assert solution_optimal("") == True, "Test 5 optimal failed"
    assert solution_brute("") == True, "Test 5 brute failed"
    print("Test 5 (empty string) passed!")

    print(f"Brute force verification: {solution_brute('()')}")
    print("All tests passed!")
