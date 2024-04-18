class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [
            [4, 6],
            [8, 6],
            [7, 9],
            [4, 8],
            [9, 0, 3],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        MOD = 10**9 + 7

        # columns are squares (10)
        # rows represent the number of remaining moves
        dp = [[0] * 10 for i in range(n)]

        for square in range(10):
            dp[0][square] = 1 # we can only jump from square in 1 way with 0 moves

        for moves in range(1, n):
            for square in range(0, 10):
                ans = 0
                for nextSquare in jumps[square]:
                    ans = (ans + dp[moves - 1][nextSquare]) % MOD

                dp[moves][square] = ans

        res = 0

        for square in range(10):
            res = (res + dp[n - 1][square]) % MOD

        return res