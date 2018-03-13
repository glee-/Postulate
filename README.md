# Postulate
A tool for osu! to calculate the true amount of PP gained upon the completion of a song

We predict the amount of actual scores using exponential regression, using the following formula:
y = ab^x, where y represents the weighted pp for song x in the list of all scores.

Using this methodology, we are able to create a good estimation for the lower bound of
the bonus pp that is actually accumulated.

Once the amount of bonus pp that is accumulated is known, it is trivial to estimate a lower bound for
the number of scores for unique maps that were set from the following equation:
Bonus pp = 416.6667 * (1 - 0.9994 ^ N)

Once we are able to estimate the lower bound for number of scores, we are able to
create an estimation for the amount of pp gained solely through performance on maps.
We can calculate this using the following formula:
Map pp = PP[1] * 0.95^0 + PP[2] * 0.95^1 + PP[3] * 0.95^2 + ... + PP[n] * 0.95^(n-1)

The total amount of pp that has been obtained is then the following: Map pp + Bonus pp

From this point, it is trivial to calculate the amount of pp that would be gained

Todo:
Integrate oppai to be able to upload a .osu file and find potential pp gains.
Find the minimum amount of rank gained based on the new potential pp.
Use scores and accuracy to provide other sources of estimation for number of unique scores.
--> give a range of possible gain

#Example Usage
Install dependencies: flask, numpy, scipy
Change directory into the Postulate directory
Run the following command in a terminal session: FLASK_APP=app.py flask run

References:
https://osu.ppy.sh/wiki/Performance_Points#Weightage_system
