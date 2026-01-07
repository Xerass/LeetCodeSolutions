class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #starting from the end, we set a "goal" if we can move to the index before goal and that index allows us to move to goal, then we know we only need to reach this point to reacg goal
        #that means we can simply move the goal to there and be able to reach the actual goal anyways.
        #this allows us to simply check if n-1 can reach n.
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            print(f"Evaluation {i} + {nums[i]}, goal = {goal}")
            if i + nums[i] >= goal:
                print(f"Replacing {goal} with {i}")
                #move over goal to that index
                goal = i


        if goal == 0:
            return True
        else:
            return False
