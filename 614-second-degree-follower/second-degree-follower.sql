/*
Selecting the Columns:

f1.follower: This column represents the users who are following others (i.e., the followers).
COUNT(DISTINCT f2.follower) AS num: This counts the distinct followers of a user who is also a followee 
of another user. The DISTINCT ensures that we don't double count any followers.
JOIN Operation:

JOIN follow f2 ON f1.follower = f2.followee: This is a self-join on the follow table. We join the table with 
itself where the follower in the first instance (f1.follower) is equal to the followee in the second 
instance (f2.followee). This helps us find all users who are followed by someone else and are also following 
at least one other user.
Grouping the Results:

GROUP BY f1.follower: We group the results by the f1.follower, meaning that each follower will have their own 
row in the result with the count of their followers.
Ordering the Results:

ORDER BY f1.follower: The results are ordered alphabetically by the follower column.
*/

/*
Example Setup:
Assume we have the following data in the follow table:

followee	follower
Alice	    Bob
Alice	    Charlie
Bob	        David
Charlie	    Alice
David	    Alice
David	    Charlie

Understanding the Data:

Bob follows Alice.
Charlie follows Alice.
David follows Bob.
Alice follows Charlie.
Alice follows David.
Charlie follows David.

Step-by-Step Execution:
Step 1: Perform the JOIN Operation
We join the follow table with itself (f1 and f2) where f1.follower = f2.followee. The idea is to find all pairs where a follower (f1.follower) is also a followee (f2.followee).

For the provided data:

f1.follower	f2.followee	f2.follower
David	    David	    Alice
David	    David	    Charlie
Alice	    Alice	    Bob
Alice	    Alice	    Charlie
Charlie	Charlie	Alice
David follows Bob and is followed by Alice and Charlie.
Alice follows Charlie and is followed by Bob and Charlie.
Charlie follows David and is followed by Alice.
Step 2: Count the Followers
For each unique f1.follower, count how many distinct f2.follower they have.

Results:

f1.follower	num
David	    2
Alice	    2
Charlie	    1

David has 2 followers: Alice and Charlie.
Alice has 2 followers: Bob and Charlie.
Charlie has 1 follower: Alice.

Step 3: Group and Order the Results
Group the results by f1.follower and order them alphabetically.

Final output:

follower	num
Alice	    2
Charlie	    1
David	    2

Explanation Recap:

The JOIN operation finds all second-degree connections.
COUNT(DISTINCT f2.follower) counts the number of distinct users following each second-degree follower.
The GROUP BY ensures the count is grouped by each follower.
The ORDER BY arranges the results alphabetically by the follower's name.
*/

-- NOTE: followee is the person that got followed, follower is the person that is following the followee


select f1.follower, count(distinct f2.follower) as num
from follow f1
join follow f2 on f1.follower = f2.followee
group by f1.follower
order by f1.follower;