class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        placed = [False] * n

        for i in range(n):
            for j in range(n):
                if not placed[j] and baskets[j] >= fruits[i]:
                    placed[j] = True
                    break
            else:
                fruits[i] = -1

        return fruits.count(-1)
