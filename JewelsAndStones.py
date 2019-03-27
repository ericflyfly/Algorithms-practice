#771. Jewels and Stones

"""You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A"."""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0
        res, jewSet = 0, set()
        for j in J:
            jewSet.add(j)
        for s in S:
            if s in jewSet:  res += 1
        return res

#Time: O(N + M) <-- N: length of first string, M:length of second string
#Space: O(N)