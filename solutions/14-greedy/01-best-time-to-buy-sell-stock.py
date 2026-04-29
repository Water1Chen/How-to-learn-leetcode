"""
LC 121. Best Time to Buy and Sell Stock (买卖股票的最佳时机)
Difficulty: Easy
Tags: Array, Dynamic Programming
Link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
Category: greedy
"""

from typing import List


# ===== 暴力解法 =====
# 思路: Try every possible buy day and sell day combination (buy before sell).
#       Calculate profit = prices[sell] - prices[buy] and track the maximum.
# 复杂度: O(n^2) time, O(1) space
def solution_brute(prices: List[int]) -> int:
    """
    Find maximum profit by trying all buy/sell pairs.
    """
    n: int = len(prices)
    max_profit: int = 0

    # WHY: Try every day as the buy day
    for buy in range(n):
        # WHY: Try every later day as the sell day
        for sell in range(buy + 1, n):
            # WHY: Calculate profit for this buy/sell pair
            profit: int = prices[sell] - prices[buy]
            # WHY: Update maximum profit if current pair is better
            if profit > max_profit:
                max_profit = profit

    return max_profit


# ===== 最优解法 =====
# 思路: One-pass greedy. Track the minimum price seen so far. For each day, calculate
#       profit if we sell today (price - min_price). Update max profit and
#       potentially update min_price if today's price is lower.
#       This is greedy because we always try to buy at the lowest seen price.
# 复杂度: O(n) time, O(1) space
def solution_optimal(prices: List[int]) -> int:
    """
    Find maximum profit in one pass by tracking minimum price seen so far.
    """
    if not prices:
        # WHY: Empty price list cannot yield any profit
        return 0

    # WHY: Track the minimum price encountered so far
    min_price: int = prices[0]
    # WHY: Track the maximum profit achievable so far
    max_profit: int = 0

    # WHY: Iterate through each day's price
    for price in prices:
        # WHY: If current price is lower than any seen before, update min_price
        if price < min_price:
            min_price = price
        else:
            # WHY: Calculate profit if we sell at current price (bought at min_price)
            profit: int = price - min_price
            # WHY: Update max profit if this is better
            if profit > max_profit:
                max_profit = profit

    return max_profit


# ===== 测试 =====
if __name__ == '__main__':
    print("Testing Best Time to Buy and Sell Stock...")

    # Test case 1: Standard case with profit
    prices1 = [7, 1, 5, 3, 6, 4]
    assert solution_optimal(prices1) == 5, f"Test 1 optimal failed: {solution_optimal(prices1)}"
    assert solution_brute(prices1) == 5, f"Test 1 brute failed"
    print("Test 1 ([7,1,5,3,6,4] -> 5) passed!")

    # Test case 2: Decreasing prices (no profit possible)
    prices2 = [7, 6, 4, 3, 1]
    assert solution_optimal(prices2) == 0, f"Test 2 optimal failed"
    assert solution_brute(prices2) == 0, f"Test 2 brute failed"
    print("Test 2 (decreasing -> 0) passed!")

    # Test case 3: Single day (cannot buy and sell on same day)
    assert solution_optimal([1]) == 0, "Test 3 optimal failed"
    assert solution_brute([1]) == 0, "Test 3 brute failed"
    print("Test 3 (single day -> 0) passed!")

    # Test case 4: Two days increasing
    prices4 = [1, 10]
    assert solution_optimal(prices4) == 9, f"Test 4 optimal failed"
    assert solution_brute(prices4) == 9, f"Test 4 brute failed"
    print("Test 4 ([1,10] -> 9) passed!")

    # Test case 5: Empty array
    assert solution_optimal([]) == 0, "Test 5 optimal failed"
    assert solution_brute([]) == 0, "Test 5 brute failed"
    print("Test 5 (empty -> 0) passed!")

    print(f"Brute force verification: {solution_brute([7,1,5,3,6,4])}")
    print("All tests passed!")
