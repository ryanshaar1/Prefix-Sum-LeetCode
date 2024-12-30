class Solution(object):
    def largestAltitude(self, gain):
        high = 0
        s = 0
        for i in range(len(gain)):
            s+=gain[i]
            if s>high:
                high=s
        return
        