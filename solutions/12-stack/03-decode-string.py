"""
LC 394. Decode String (字符串解码)
Difficulty: Medium
Tags: String, Stack, Recursion
Link: https://leetcode.cn/problems/decode-string/
Category: stack
"""


# ===== 暴力解法 =====
# 思路: Recursive parsing. Scan the string character by character. When we encounter
#       a digit, parse the full number k, then recursively decode the enclosed string
#       inside the brackets, and repeat it k times.
# 复杂度: O(n * k) time (depends on nesting and repeat counts), O(n) space for recursion
def solution_brute(s: str) -> str:
    """
    Decode an encoded string using recursive parsing.
    """

    # WHY: Recursive helper that decodes from index i and returns (result, next_index)
    def decode(i: int) -> tuple:
        result: list = []  # WHY: Use list for efficient string building
        num: int = 0       # WHY: Accumulate the current repeat count

        # WHY: Process characters until end of string or closing bracket
        while i < len(s):
            ch: str = s[i]

            if ch.isdigit():
                # WHY: Build the repeat count (may be multi-digit like "12")
                num = num * 10 + int(ch)
                i += 1
            elif ch == '[':
                # WHY: Start decoding the enclosed substring from position i+1
                decoded_str, i = decode(i + 1)
                # WHY: Repeat the decoded substring k times and append to result
                result.append(decoded_str * num)
                # WHY: Reset num for the next potential encoding
                num = 0
            elif ch == ']':
                # WHY: End of current encoded block — return to caller
                return ''.join(result), i + 1
            else:
                # WHY: Regular character — append directly
                result.append(ch)
                i += 1

        return ''.join(result), i

    result, _ = decode(0)
    return result


# ===== 最优解法 =====
# 思路: Use two stacks — one for repeat counts and one for partial strings.
#       Iterate through the string: accumulate digits for count, push onto stacks
#       when encountering '[', build decoded string when encountering ']'.
#       This avoids recursion overhead.
# 复杂度: O(n) time (each character processed once), O(n) space for stacks
def solution_optimal(s: str) -> str:
    """
    Decode an encoded string using two stacks (iterative).
    """
    # WHY: Stack to store repeat counts for nested encoded blocks
    count_stack: list = []
    # WHY: Stack to store the string built so far before each '[' encountered
    string_stack: list = []

    current_str: list = []  # WHY: List to build the current decoded string
    k: int = 0              # WHY: Accumulator for the current repeat count

    # WHY: Iterate through each character of the encoded string
    for ch in s:
        if ch.isdigit():
            # WHY: Build the repeat count (handles multi-digit numbers)
            k = k * 10 + int(ch)
        elif ch == '[':
            # WHY: Save current state before starting the nested block
            count_stack.append(k)        # WHY: Push the repeat count for this block
            string_stack.append(''.join(current_str))  # WHY: Push string built so far
            # WHY: Reset for the inner encoded block
            current_str = []
            k = 0
        elif ch == ']':
            # WHY: End of an encoded block — decode and append to outer string
            # WHY: Get the string decoded inside this block
            inner_str: str = ''.join(current_str)
            # WHY: Get the repeat count for this block
            repeat_count: int = count_stack.pop()
            # WHY: Get the string state before this block
            prev_str: str = string_stack.pop()
            # WHY: Build: outer_prev + (inner * repeat_count)
            current_str = [prev_str] + [inner_str * repeat_count]
        else:
            # WHY: Regular character — append to current building string
            current_str.append(ch)

    # WHY: Join the final decoded string
    return ''.join(current_str)


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Decode String...")

    # Test case 1: Simple single encoding
    assert solution_optimal("3[a]2[bc]") == "aaabcbc", \
        f"Test 1 optimal failed: {solution_optimal('3[a]2[bc]')}"
    assert solution_brute("3[a]2[bc]") == "aaabcbc", \
        f"Test 1 brute failed"
    print("Test 1 (\"3[a]2[bc]\" -> \"aaabcbc\") passed!")

    # Test case 2: Nested encoding
    assert solution_optimal("3[a2[c]]") == "accaccacc", \
        f"Test 2 optimal failed: {solution_optimal('3[a2[c]]')}"
    assert solution_brute("3[a2[c]]") == "accaccacc", \
        f"Test 2 brute failed"
    print("Test 2 (\"3[a2[c]]\" -> \"accaccacc\") passed!")

    # Test case 3: Two-digit repeat count
    assert solution_optimal("10[a]") == "a" * 10, f"Test 3 optimal failed"
    assert solution_brute("10[a]") == "a" * 10, f"Test 3 brute failed"
    print("Test 3 (\"10[a]\" -> 10 a's) passed!")

    # Test case 4: No encoding (plain string)
    assert solution_optimal("abc") == "abc", f"Test 4 optimal failed"
    assert solution_brute("abc") == "abc", f"Test 4 brute failed"
    print("Test 4 (\"abc\" -> \"abc\") passed!")

    # Test case 5: Complex nested and adjacent encodings
    assert solution_optimal("2[abc]3[cd]ef") == "abcabccdcdcdef", \
        f"Test 5 optimal failed: {solution_optimal('2[abc]3[cd]ef')}"
    assert solution_brute("2[abc]3[cd]ef") == "abcabccdcdcdef", \
        f"Test 5 brute failed"
    print("Test 5 (\"2[abc]3[cd]ef\" -> \"abcabccdcdcdef\") passed!")

    print(f"Brute force verification: {solution_brute('3[a]2[bc]')}")
    print("All tests passed!")
