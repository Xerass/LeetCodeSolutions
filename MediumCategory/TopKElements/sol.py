class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dict for counts
        count = {} #(num, counts)
        n = len(nums)
        for i in nums:
            count[i] = count.get(i, 0) + 1

        #setup a frequency sort where each bucket is an index and we place a digit there if they are within that count(bucket)
        bucket = []

        #build the containers one by one, + 1 since max counts is +1 to len
        for i in range(n + 1):
            bucket.append([])
        
        #place the buckets into their containers
        for num in count:
            #index is frequency
            index = count[num]

            bucket[index].append(num)

        #now simply squish the array into a 1d one
        result = []

        #go backwards
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                result.append(j)
        

        return result[:k]
