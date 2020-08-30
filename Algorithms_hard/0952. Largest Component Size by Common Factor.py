"""
0952. Largest Component Size by Common Factor
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000

"""


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        primes = []
        for x in range(2, int(max(A)**0.5) + 1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)

        factors = collections.defaultdict(list)
        for a in A:
            x = a
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    factors[a].append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                factors[a].append(x)
                primes.append(x)

        primes = list(set(primes))
        n = len(primes)
        p2i = {p: i for i, p in enumerate(primes)}

        parent = [i for i in range(n)]

        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pi] = pj

        for a in A:
            if factors[a]:
                p0 = factors[a][0]
                for p in factors[a][1:]:
                    union(p2i[p0], p2i[p])

        count = collections.Counter(
            find(p2i[factors[a][0]]) for a in A if factors[a])
        return max(count.values())



