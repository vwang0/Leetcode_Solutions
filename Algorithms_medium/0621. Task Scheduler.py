"""
0621. Task Scheduler
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) :
        freq = Counter(tasks)
        most_freq = freq.most_common()[0][1]
        found_most = sum([freq[key] == most_freq for key in freq])
        return max(len(tasks), (most_freq-1)*(n+1)+found_most)

# ========= not correct!
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) :
#         length = len(tasks)
#         if length<=1: return length
#         task_map = dict()
#         for task in task_map:
#             task_map[task] = task_map.get(task,0)+1
#         task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
#         max_task_count = task_sort[0][1]
#         res = (max_task_count - 1) * (n + 1)
#         for sort in task_sort:
#             if sort[1] == max_task_count:
#                 res += 1
#         return res if res >= length else length

# ========= not correct!
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int):
#         n, c = len(tasks), Counter(tasks)
#         most = c.most_common()
#         first_freq, cnt = most[0][1], 0
#         for i in range(1, len(most)):
#             if most[i][1] == first_freq:
#                 cnt += 1
#         res = (first_freq - 1) * (n + 1) + cnt
#         return res if res>=n else n
