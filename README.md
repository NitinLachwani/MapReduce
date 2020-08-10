# MapReduce

Disclaimer: This was part of the Hadoop training that I took and these were my test examples.

Q. Given a data set of movie ID, ratings and user ID, find the # of ratings + popular movies.

Data set: u.data
Code:
MovieRatings.py for getting list of count per ratings
MoviePopularityRatings.py for getting a sorted list of the most popular movies

Commands to run:
python MovieRatings.py u.data
python MoviePopularityRatings u.data

Local:

On Hadoop:
python MovieRatings.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data
python MoviePopularityRatings.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data

