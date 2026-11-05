class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [-1] * n
        dist[src] = 0
        for i in range(k+1):
            temp = dist.copy()
            for fro, to, price in flights:
                if dist[fro] != -1:
                    new_cost = dist[fro] + price
                    if temp[to]==-1 or new_cost<temp[to]:
                        temp[to] = new_cost
            dist = temp

        return dist[dst]

