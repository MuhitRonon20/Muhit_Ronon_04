from collections import deque

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins = sorted(set(coins))
        
        queue = deque([(0, 0)]) 
        visited = {0}
        
        while queue:
            curr, count = queue.popleft()
            
            for coin in coins:
                nxt = curr + coin
                if nxt == amount:
                    return count + 1
                if nxt > amount:
                    break 
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, count + 1))
                    
        return -1