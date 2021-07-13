Idea: Queue solution, keep a record of all past 0s. Once it reaches K (the max number that can be flipped) that first 0 in queue is the "boundary" for the NEXT slice of the array
The boundary of THIS slice is whatever was there before as the "head", and this current position - 1


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        queue = []
        head = -1
        long = 0
        for i, j in enumerate(nums):
            if j == 0:
                queue.append(i)
                if len(queue) > k:
                    long = max(long, i-head-1)
                    head = queue.pop(0)
        return max(long, i-head)