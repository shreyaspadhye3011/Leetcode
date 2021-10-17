# https://leetcode.com/problems/network-delay-time/
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        neighbors = createNeighborDirectory(times)
        reachable = [k]
        reached = set()
        reached_count = 0
        while reachable:
            # TODO: check if popLeft() required
            node = reachable.pop()
            if node not in reached:
                reached_count += 1
                reached.add(node)
                for neighbor in neighbors[node]:
                    pass