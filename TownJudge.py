class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_count = {}
        for person in range(1, N+1):
            trust_count[person]=0
        for trustor,trustee in trust:
            trust_count[trustor] -= 1
            trust_count[trustee] += 1
        for person, trust_person_count in trust_count.items():
            if trust_person_count ==  N-1:
                return person
        return -1