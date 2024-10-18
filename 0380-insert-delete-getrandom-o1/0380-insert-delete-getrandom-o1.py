import random

class RandomizedSet(object):
    def __init__(self):
        self.num_set = []

    def insert(self, val):
        if val in self.num_set:
            return False
        
        self.num_set.append(val)
        

    def remove(self, val):
        if val in self.num_set:
            self.num_set.remove(val)
            return True
        
        return False
        """
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        randomIdx = random.randrange(0, len(self.num_set))
        if len(self.num_set)==0:
            return None
        return self.num_set[randomIdx]
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()