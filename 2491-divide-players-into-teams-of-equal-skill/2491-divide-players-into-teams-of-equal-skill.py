class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        team_count = len(skill)/2
        share, remainder = divmod(sum(skill), team_count)
        share = int(share)
        if remainder !=0:
            return -1
        
        members = {}
        for personal_skill in skill:
            members[personal_skill] = members.get(personal_skill,0)+1
            
        
        product_sum = 0
        for person in skill:
            if(members[person]==0): continue
            members[person]-=1
            if share < person or members.get(share-person,0)<=0:
                return -1
            
            members[share-person]-=1
            product_sum += person*(share-person)
            
        
        return int(product_sum)