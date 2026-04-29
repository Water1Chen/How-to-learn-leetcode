"""
LC 155. Min Stack (最小栈)
Difficulty: Medium
Tags: Stack, Design
Link: https://leetcode.cn/problems/min-stack/
Category: stack
"""


# ===== 暴力解法 =====
# 思路: Use a standard list as the main stack. On getMin(), scan the entire stack
#       to find the minimum element. This is O(n) per getMin call.
# 复杂度: push/pop/top: O(1), getMin: O(n) time, O(n) space for stack
class MinStackBrute:
    """
    Stack that supports getMin() with O(n) scan.
    """
    def __init__(self) -> None:
        # WHY: Internal list to store all stack elements
        self._stack: list = []

    def push(self, val: int) -> None:
        # WHY: Standard push — append to the end of the list
        self._stack.append(val)

    def pop(self) -> None:
        # WHY: Standard pop — remove and return the top element
        self._stack.pop()

    def top(self) -> int:
        # WHY: Return the top element without removing it
        return self._stack[-1]

    def getMin(self) -> int:
        # WHY: Scan the entire stack to find the minimum element
        return min(self._stack)


# ===== 最优解法 =====
# 思路: Use an auxiliary stack that stores the minimum value at each level.
#       When pushing a new value, compare with current minimum and push the
#       smaller one onto the min_stack. This way, the min_stack top always
#       stores the global minimum, and we can track min after pop.
# 复杂度: All operations O(1) time, O(n) space for the auxiliary min stack
class MinStackOptimal:
    """
    Stack that supports getMin() in O(1) using an auxiliary min stack.
    """
    def __init__(self) -> None:
        # WHY: Main stack stores all pushed elements
        self._stack: list = []
        # WHY: Auxiliary stack stores the minimum value at each stack level
        self._min_stack: list = []

    def push(self, val: int) -> None:
        # WHY: Always push val onto the main stack
        self._stack.append(val)

        # WHY: If min_stack is empty, val is the first element = current minimum
        if not self._min_stack:
            self._min_stack.append(val)
        else:
            # WHY: Push the smaller of val and current minimum onto min_stack
            # WHY: This ensures min_stack[i] = min(values[:i+1])
            current_min: int = self._min_stack[-1]
            self._min_stack.append(min(val, current_min))

    def pop(self) -> None:
        # WHY: Remove element from both stacks to maintain alignment
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        # WHY: Return the top of the main stack
        return self._stack[-1]

    def getMin(self) -> int:
        # WHY: O(1) retrieval of the minimum — top of min_stack holds current min
        return self._min_stack[-1]


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Min Stack...")

    # Test case 1: Standard operations
    stack_opt = MinStackOptimal()
    stack_opt.push(-2)
    stack_opt.push(0)
    stack_opt.push(-3)
    assert stack_opt.getMin() == -3, f"Test 1 getMin failed: {stack_opt.getMin()}"
    stack_opt.pop()
    assert stack_opt.top() == 0, f"Test 1 top failed"
    assert stack_opt.getMin() == -2, f"Test 1 getMin after pop failed"
    print("Test 1 (standard operations) passed!")

    # Test case 2: Brute force verification
    stack_brute = MinStackBrute()
    stack_brute.push(-2)
    stack_brute.push(0)
    stack_brute.push(-3)
    assert stack_brute.getMin() == -3, f"Test 2 getMin failed"
    stack_brute.pop()
    assert stack_brute.top() == 0, f"Test 2 top failed"
    assert stack_brute.getMin() == -2, f"Test 2 getMin after pop failed"
    print("Test 2 (brute force verification) passed!")

    # Test case 3: Single element
    stack3 = MinStackOptimal()
    stack3.push(42)
    assert stack3.top() == 42, "Test 3 top failed"
    assert stack3.getMin() == 42, "Test 3 getMin failed"
    stack3.pop()
    print("Test 3 (single element) passed!")

    # Test case 4: Duplicate minimums
    stack4 = MinStackOptimal()
    stack4.push(1)
    stack4.push(2)
    stack4.push(1)
    assert stack4.getMin() == 1, "Test 4 getMin failed"
    stack4.pop()
    assert stack4.getMin() == 1, "Test 4 getMin after pop should still be 1"
    print("Test 4 (duplicate mins) passed!")

    print("Brute force verification done!")
    print("All tests passed!")
