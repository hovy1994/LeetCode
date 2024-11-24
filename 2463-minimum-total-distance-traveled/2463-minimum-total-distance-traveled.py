class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robotLen = len(robot)
        factoryLen = len(factory)
        dp = [[float('inf')] * (factoryLen + 1) for _ in range(robotLen + 1)]
        robot.sort()
        factory.sort()
        
        dp[0][0]=0
        
        for i in range(robotLen+1):
            for f in range(1, factoryLen+1):
                pos, limit = factory[f-1]
                dp[i][f] = dp[i][f-1]
                factory_distance = 0
                for j in range(1, min(limit, i) + 1):
                    factory_distance+=abs(robot[i-j]-pos)
                    dp[i][f] = min(dp[i][f], dp[i-j][f-1]+factory_distance)
                    
        return dp[robotLen][factoryLen]