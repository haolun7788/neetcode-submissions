class Solution:
    def climbStairs(self, n: int) -> int:
        computed = {}

        def doRec(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in computed:
                return computed[n]
            else:
                do = doRec(n - 1) + doRec(n - 2)
                computed[n] = do
                return do
        
        return doRec(n)