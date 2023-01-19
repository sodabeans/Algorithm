class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = []
        if len(nums1) < len(nums2):
            nums1 = Counter(nums1)
            for i in range(len(nums2)):
                if nums2[i] in nums1 and nums1[nums2[i]] > 0:
                    nums1[nums2[i]] -= 1
                    answer.append(nums2[i])
        else:
            nums2 = Counter(nums2)
            for i in range(len(nums1)):
                if nums1[i] in nums2 and nums2[nums1[i]] > 0:
                    nums2[nums1[i]] -= 1
                    answer.append(nums1[i])

        return answer
