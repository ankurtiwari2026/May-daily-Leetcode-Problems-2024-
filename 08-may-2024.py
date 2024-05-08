class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        list1=sorted(score,reverse=True)
        count={}
        for i in range(len(list1)):
            if i==0:
                count[list1[i]]="Gold Medal"
            elif i==1:
                count[list1[i]]="Silver Medal"
            elif i==2:
                count[list1[i]]="Bronze Medal"
            else:
                count[list1[i]]=str(i+1)
        res=[]
        for i in score:
            res.append(count[i])
        return res                        




        
        
