class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #we can approach this with a "cycle search"
        #for a constant space approach, we need to avoid stating "visited" nodes
        #most commonly, this is solved by a rabbit and tortiose approach where rabbit moves twice as fast as tortiose.
        #assume a move is going to the index specified by the value, eventually we reach the point where we reurn to the same node!
        #we abuse the fact that rabbit is twice as fast as tortoise, so they're almost never on the same tile but at some point their paths will collide and that will be the start of the cycle.
        rabbit = 0
        tortoise = 0
        #have them "move" once so they're not ==

        rabbit = nums[nums[rabbit]]
        tortoise = nums[tortoise]

        while rabbit != tortoise:
            rabbit = nums[nums[rabbit]]
            tortoise = nums[tortoise]
        
        #cool math by someone much smarter than me (floyd) stated that since rabbit moves twice as fast
        #the distance from the start to dupe happens to be == to collision point distance from dupe
        #that means that moving one of the pointers back to the start and they both move at 1 speed, they will both reach the dupe indices

        #lets slow down the rabbit
        rabbit = 0
        while rabbit != tortoise:
            tortoise = nums[tortoise]
            rabbit = nums[rabbit]

        #return whatver val rabbit had
        return rabbit

