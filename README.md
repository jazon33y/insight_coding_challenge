Insight Data Engineering - Coding Challenge Solutions by Jason O'Rawe
===========================================================

To redescribe the challenge, it is to implement these two features:

1. Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.
2. Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

To satisfy the challenge, I have written two python scripts implimenting these features.  Specifically ./src/tweets_cleaned.py will

- remove escape characters and unicode and return the processed JSON tweet in the below format:
<contents of "text" field> (timestamp: <contents of "created_at" field>),

- track the number of tweets that contain unicode, and return following message at the bottom of the output file:
<number of tweets that had unicode> tweet(s) contained unicode.

The ./src/tweets_cleaned.py python program output the results of this first feature to a text file named `ft1.txt` in the `tweet_output` directory, with each new tweet on a newline.

- A Twitter hashtag graph is a graph connecting all the hashtags that have been mentioned together in a single tweet using tweets that arrived in the last 60 seconds as compared to the timestamp of the latest tweet. 

- The average degree will be calculated by summing the degrees of all nodes in all graphs and dividing by the total number of nodes in all graphs.


The output of the second feature should be a file in the `tweet_output` directory named `ft2.txt` that contains the rolling average for each tweet in the file (e.g. if there are three input tweets, then there should be 3 averages), following the format above.  The precision of the average should be two digits after the decimal place (i.e. rounded to the nearest hundredths place).


Alternatively, here is example output of the `tree` command:

	├── README.md  
	├── run.sh  
	├── src  
	│   ├── average_degree.py  
	│   └── tweets_cleaned.py  
	├── tweet_input  
	│   └── tweets.txt  
	└── tweet_output  
	    ├── ft1.txt  
	    └── ft2.txt  

