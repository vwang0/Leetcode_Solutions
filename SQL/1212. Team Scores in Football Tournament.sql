/*
1212. Team Scores in Football Tournament
Table: Teams

+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| team_id       | int      |
| team_name     | varchar  |
+---------------+----------+
team_id is the primary key of this table.
Each row of this table represents a single football team.
Table: Matches

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| host_team     | int     |
| guest_team    | int     | 
| host_goals    | int     |
| guest_goals   | int     |
+---------------+---------+
match_id is the primary key of this table.
Each row is a record of a finished match between two different teams. 
Teams host_team and guest_team are represented by their IDs in the teams table (team_id) and they scored host_goals and guest_goals goals respectively.
 

You would like to compute the scores of all teams after all matches. Points are awarded as follows:
A team receives three points if they win a match (Score strictly more goals than the opponent team).
A team receives one point if they draw a match (Same number of goals as the opponent team).
A team receives no points if they lose a match (Score less goals than the opponent team).
Write an SQL query that selects the team_id, team_name and num_points of each team in the tournament after all described matches. Result table should be ordered by num_points (decreasing order). In case of a tie, order the records by team_id (increasing order).

The query result format is in the following example:


 
Teams table:
+-----------+--------------+
| team_id   | team_name    |
+-----------+--------------+
| 10        | Leetcode FC  |
| 20        | NewYork FC   |
| 30        | Atlanta FC   |
| 40        | Chicago FC   |
| 50        | Toronto FC   |
+-----------+--------------+

Matches table:
+------------+--------------+---------------+-------------+--------------+
| match_id   | host_team    | guest_team    | host_goals  | guest_goals  |
+------------+--------------+---------------+-------------+--------------+
| 1          | 10           | 20            | 3           | 0            |
| 2          | 30           | 10            | 2           | 2            |
| 3          | 10           | 50            | 5           | 1            |
| 4          | 20           | 30            | 1           | 0            |
| 5          | 50           | 30            | 1           | 0            |
+------------+--------------+---------------+-------------+--------------+

Result table:
+------------+--------------+---------------+
| team_id    | team_name    | num_points    |
+------------+--------------+---------------+
| 10         | Leetcode FC  | 7             |
| 20         | NewYork FC   | 3             |
| 50         | Toronto FC   | 3             |
| 30         | Atlanta FC   | 1             |
| 40         | Chicago FC   | 0             |
+------------+--------------+---------------+
*/

select Teams.team_id,
       Teams.team_name,
       sum(case
               when team_id=host_team
                    and host_goals>guest_goals then 3
               else 0
           end) + sum(case
                          when team_id=host_team
                               and host_goals=guest_goals then 1
                          else 0
                      end) + sum(case
                                     when team_id=guest_team
                                          and host_goals<guest_goals then 3
                                     else 0
                                 end) + sum(case
                                                when team_id=guest_team
                                                     and host_goals=guest_goals then 1
                                                else 0
                                            end) as num_points
from Teams
left join Matches on Teams.team_id = Matches.host_team
or Teams.team_id = Matches.guest_team
group by Teams.team_id
order by num_points desc,
         Teams.team_id asc
;         


-- Write your MySQL query statement below
With team_pnts AS (

SELECT host_team team_id, CASE WHEN host_goals>guest_goals THEN 3
                     WHEN host_goals=guest_goals THEN 1
                     WHEN host_goals<guest_goals THEN 0 END points
FROM Matches
    
UNION ALL                    

SELECT guest_team team_id, CASE WHEN guest_goals>host_goals THEN 3
                     WHEN guest_goals=host_goals THEN 1
                     WHEN guest_goals<host_goals THEN 0 END points
FROM Matches
)

SELECT t.team_id, t.team_name, IF(SUM(points) IS NOT NULL, SUM(points), 0) num_points
FROM Teams t
LEFT JOIN team_pnts tp
ON t.team_id = tp.team_id
GROUP BY 1,2
ORDER BY 3 DESC, 1