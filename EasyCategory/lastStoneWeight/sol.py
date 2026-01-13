import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #negate everything
        maxHeap = [-num for num in stones]
        #heapify
        heapq.heapify(maxHeap)
        #no in built way to support max heap in heapq, so we can negate everything so everything is sorted in reverse then simply negate them back

        #keep going till heap has only one left
        while len(maxHeap) > 1:
            #now the largest is technically the smallest, bubbling them to the top
            #simply negate it
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)

            if stone1 == stone2:
                #dont push anything since both stones are destroyed
                continue
            elif stone1 < stone2:
                #push in stone2 - stone1 (in this case techincally stone1 - stone2  so its neg)
                heapq.heappush(maxHeap, stone1 - stone2)    
            elif  stone1 > stone2:
                heapq.heappush(maxHeap, stone2 - stone1)
        

        return -maxHeap[0] if maxHeap else 0
