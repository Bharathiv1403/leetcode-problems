nums1=[1,3]
nums2=[2]
total=nums1+nums2
len=0
for i in total:
    len+=1
n=len+1
print(n/2)

# l = nums1 + nums2
# l.sort()
# n = len(l)
# print(n)
# if n%2 !=0:
#     median = l[int(n/2)]
#     print(median)
# else:
#     b = int(n/2)
#     a = b -1
#     median = (l[a] + l[b])/2
#     print(median)
# print(int(3/2))

# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#         total=nums1 + nums2
#         total.sort()
#         n=len(total)
#         if n%2 !=0:
#              median = total[int(n/2)]
#         else:
#             b = int(n/2)
#             a = b-1
#             median= (total[a] + total[b])/2
#         return median




# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#         l = nums1 + nums2
#         l.sort()
#         n = len(l)
#         if n%2 != 0:
#             median = l[int(n/2)]
#         else:
#             b = int(n/2)
#             a = b-1
#             median = (l[a] + l[b]) / 2
#         return median
# sol=Solution
# print(sol.findMedianSortedArrays([[1,3],[2]]))