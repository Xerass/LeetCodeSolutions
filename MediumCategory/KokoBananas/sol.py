class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #perform a binary search over a range of values 1 - max pile

        left = 1
        right = max(piles)

        result = right
        #we need a small helper func to quickly determine if hours taken to eat:
        def hoursToEat(rate: int) -> int:
            hours = 0
            for pile in piles:
                #cool ceiling trick
                hours += (pile + rate - 1) // rate

            return hours
        

        #bin search
        while left <= right:
            mid = (left + right)//2

            hours = hoursToEat(mid)

            if hours <= h:  
                #means there is still time left means maybe there is still a smaller rate possible
                result = mid
                #we dont need to check if mid < result since we're halving it anyway, if it does go through the if its always gonna be smaller
                right = mid - 1
            else:
                left = mid + 1

        return result
