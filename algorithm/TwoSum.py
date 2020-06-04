class Solution:
    def twoSum(self, nums, target):
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [i, hash_map[target - x]]
            hash_map[x] = i


if __name__ == '__main__':
    l = [2, 7, 9, 15]
    l.append(2)
    print(l)
    s = Solution()
    print(s.twoSum([2, 7, 9, 15], 9))
