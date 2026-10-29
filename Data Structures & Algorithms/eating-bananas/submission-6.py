class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = [1,4,3,2]
        index    0 1 2 3  # of bananas
        h = hours you have to eat all the bananas
        k = bananas eating rate per hour
        return min eating rate k that you can finish all the bananas in h hours
        '''
        def finish_all(k):
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            return hours <= h

        left = 0
        right = max(piles)

        while left + 1 < right:
            mid = (left + right) // 2
            if finish_all(mid):
                right = mid
            else:
                left = mid
        return right

        

       


