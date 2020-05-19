"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Constraints:

    1 <= N <= 1000
    0 <= trust.length <= 10^4
    trust[i].length == 2
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N

"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1: return 1
        if len(trust) == 1: return trust[0][1]
        # if N == 2: return trust[0][1]
        ppl = {}
        trus = {}
        for pair in trust:
            if pair[0] in ppl:
                ppl[pair[0]] += 1
            else:
                ppl[pair[0]] = 1
            if pair[1] in trus:
                trus[pair[1]] += 1
            else:
                trus[pair[1]] = 1
        # print(ppl,trus)
        n = 0
        ans = 0
        for x in trus:
            if x not in ppl and trus[x] > 1:
                n += 1
                ans = x
        if n == 1:
            return ans
        else:
            return -1
