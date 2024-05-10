
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        li=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):   li.append(arr[i]/arr[j])
        li.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]/arr[j]==li[k-1]:   return [arr[i],arr[j]]
