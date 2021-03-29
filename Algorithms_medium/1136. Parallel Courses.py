"""
1136. Parallel Courses
Medium

You are given an integer n which indicates that we have n courses, labeled from 1 to n. You are also given an array relations where relations[i] = [a, b], representing a prerequisite relationship between course a and course b: course a has to be studied before course b.

In one semester, you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses. If there is no way to study all the courses, return -1.

 

Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they depend on each other.
 

Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
1 <= a, b <= n
a != b
All the pairs [a, b] are unique.
"""
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        visited = [0 for _ in range(n + 1)]
        depth = [1 for _ in range(n + 1)]
        for x, y in relations:
            d[x].append(y)
        for i in range(1, n + 1):
            if not self.dfs(i, d, visited, depth, 1):
                return -1
        #print(depth)
        return max(depth)

    def dfs(self, i, d, visited, depth, cnt):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for j in d[i]:
            if not self.dfs(j, d, visited, depth, cnt):
                return False
            depth[i] = max(depth[i], depth[j] + 1)
        visited[i] = 2
        return True