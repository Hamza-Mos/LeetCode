class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balanceMap = defaultdict(int)

        # build hashmap that maps a person to their net balance
        for source, destination, amount in transactions:
            balanceMap[source] -= amount
            balanceMap[destination] += amount

        # add all non-zero net balances to the balance list
        balanceList = [ netBalance for netBalance in balanceMap.values() if netBalance ]

        # backtrack(currPerson) should return the min number of transactions to settle balanceList[currPerson:]
        def backtrack (currPerson):
            # reached end of balanceList so return 0 transactions
            if currPerson == len(balanceList):
                return 0

            # current person already has a zero net balance so move to next person
            if balanceList[currPerson] == 0:
                return backtrack(currPerson + 1)

            # min number of transactions
            minTransactions = float('inf')

            # find next person to transfer current person's balance to
            for nextPerson in range(currPerson + 1, len(balanceList)):
                # next person's net balance must be opposite of current person's to be able to transfer
                if balanceList[nextPerson] * balanceList[currPerson] < 0:
                    # transfer net balance
                    balanceList[nextPerson] += balanceList[currPerson] 

                    # recursively call function on next person (currPerson + 1)
                    minTransactions = min(minTransactions, 1 + backtrack(currPerson + 1))

                    # backtrack - remove net balance from next person to explore other people to transfer to
                    balanceList[nextPerson] -= balanceList[currPerson]

            return minTransactions

        return backtrack(0)