Insight Data Engineering - Coding Challenge Solutions by Jason O'Rawe
===========================================================

To redescribe the challenge, it is to implement these two features:

1. Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.
2. Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

To satisfy the challenge, I have written two python scripts implementing these features.  Specifically ./src/tweets_cleaned.py implements the first feature by:

- removing escape characters and unicode and returning the processed JSON tweet in the prescribed format,

- tracking the number of tweets that contain unicode, and returning a message at the bottom of the output file describing that number.

The ./src/tweets_cleaned.py python program outputs the results of this first feature to a text file named `ft1.txt` in the `tweet_output` directory, with each new tweet on a newline.  ./src/average_degree.py implements the second feature by:

- constructing a Twitter hashtag graph connecting all the hashtags that have been mentioned together in a single tweet using tweets that arrived in the last 60 seconds as compared to the timestamp of the latest tweet,

- calculating the average degree by summing the degrees of all nodes in all graphs and dividing by the total number of nodes in all graphs, removing and discounting isolate nodes.

The ./src/average_degree.py python program outputs the results of this second feature to a text file named `ft2.txt` in the `tweet_output` directory, which contains the rolling average for each tweet in the file, with a precision defined as being two digits after the decimal place.

Here is the general directory structure:

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

One can execute the python programs by executing run.sh.

The code was tested and run on a Unix system using the Anaconda Python distribution and the below Python modules:

- sys
- warnings
- itertools
- re
- json
- dateutil
- datetime
- numpy
- pandas
- networkx
- matplotlib
