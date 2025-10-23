class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        m,n = len(A),len(B)
        total = m + n
        half = (total + 1)//2

        #perform a binary search over the 2 arrays
        #check to see which one was shorter
        if m > n:
            A, B = B, A
            m, n = n, m

        low = 0
        high = m

        while low <= high:
            i = (low + high)//2#get i elements from A on the left
            j = half - i #get  j elemnts from B on the left

            leftA  = A[i-1] if i > 0 else float("-inf")
            rightA = A[i]   if i < m else float("inf")
            leftB  = B[j-1] if j > 0 else float("-inf")
            rightB = B[j]   if j < n else float("inf")

            #view if partiotion is allowed (left <= all right)

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    #if num is odd, simply return the max 
                    return float(max(leftA, leftB))
                else:
                    #if even get ave
                    leftmax = max(leftA, leftB)
                    rightmin = min(rightA, rightB)
                    return (leftmax + rightmin)/2.0
            elif leftA > rightB:
                #we goot to many from A move back left
                high = i - 1
            else:
                #leftB > rightA, took too little from A, go back right
                low = i + 1
