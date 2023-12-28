class Solution:
    def knapsack(self, W, wt, val, N):
        def solve(n, cap):
            if n == 0 or cap == 0:
                return 0
            else:
                cwt = wt[n-1]
                cval = val[n-1]
                if cwt > cap:
                    return solve(n-1, cap)
                else:
                    c1 = cval+solve(n-1, cap-cwt)
                    c2 = solve(n-1, cap)
                    return max(c1, c2)
        return solve(N,W)
    
print(Solution().knapsack(4, [1,2,3], [4,5,1], 3))
                