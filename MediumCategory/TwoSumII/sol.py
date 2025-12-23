class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer approach
        i = 0
        j = len(numbers) - 1

        #add both if nums[i] + nums[j] > target j can never be included in the sum since we already added it to the smallest digit

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                #move j down
                j -= 1
            elif sum < target:
                #move i up
                i += 1
            elif sum == target:
                #is the answer so we know that i and j are the indices
                return [i+1, j+1]
