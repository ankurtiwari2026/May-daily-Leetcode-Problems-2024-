class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        count=0
        for turn,score in enumerate(happiness):#turn suru hoga 0 se and score is the start from 
        # happiness array ke phle element se
            if turn==k:
                return count
            count+=max(0,score-turn)
        return count
