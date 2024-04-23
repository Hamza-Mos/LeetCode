class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # unbounded knapsack problem 
        # cols represent 0-amount (just like how cols represent capacity in unbounded knapsack)
        # rows represent indices of coins (just like how rows represent indices of weights in unbounded knapsack)

        # dp[coin][amount] = dp[lastCoin][amount] + dp[coin][amount - coin]

        # we can optimize the space complexity so that we do not need a 2D grid by keeping track of
        # the previous row and current row

        numCoins = len(coins)
        prevRow = [0] * (amount + 1)
        prevRow[0] = 1

        for currCoin in range(numCoins):
            currRow = [0] * (amount + 1)
            for currAmount in range(amount + 1):
                currRow[currAmount] = prevRow[currAmount]

                if currAmount - coins[currCoin] >= 0:
                    currRow[currAmount] += currRow[currAmount - coins[currCoin]]

            print(currRow)

            prevRow = currRow

        return prevRow[-1]

        