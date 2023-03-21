class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []
        for price, amount, orderType in orders:
            if orderType == 0:
                heapq.heappush(buy, [-price, amount])
            else:
                heapq.heappush(sell, [price, amount])
            while buy and sell and -buy[0][0] >= sell[0][0]:
                if buy[0][1] > sell[0][1]:
                    buy[0][1] -= sell[0][1]
                    heapq.heappop(sell)
                elif buy[0][1] < sell[0][1]:
                    sell[0][1] -= buy[0][1]
                    heapq.heappop(buy)
                else:
                    heapq.heappop(buy)
                    heapq.heappop(sell)
        return sum([amount for price, amount in buy + sell])