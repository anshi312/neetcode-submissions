class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        med1 = med2 = 0
        i, j = 0, 0
        for count in range((len1+len2)//2 + 1):
            med2 = med1
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    med1 = nums1[i]
                    i += 1
                else:
                    med1 = nums2[j]
                    j += 1
            elif i < len1:
                med1 = nums1[i]
                i += 1
            else:
                med1 = nums2[j]
                j += 1
            
        if (len1+len2)%2 == 1:
            return float(med1)
        else: 
            return (med1 + med2) / 2.0