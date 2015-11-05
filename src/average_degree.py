import sys
import warnings
import itertools
import re
import json
import dateutil
import datetime
from datetime import timedelta
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#========================
# define helper functions
#========================

def get_tags(text):
	'''Return unique lists of hastags from twitter text, by splitting text
	and returing unique strings that start with #'''
	return list( set(tag for tag in text.split() if tag.startswith('#')) )

def create_graph(list_of_lists):
	'''given a list conprising of lists of hashtags, construct a graph.
	If the list is greater than 2 or more, make sure to create all possible
	edges given the hashtag combination.  If the list is 0, do nothing and 
	if it is of size 1 then just create a node.'''
	G=nx.Graph()    
	for i in list_of_lists:
		if len(i)>1:
			G.add_edges_from(list(itertools.combinations(i,2)))
		elif len(i)==0:
			continue
		elif len(i)==1:
			G.add_node(*i)
	return G

def get_time_groups(df, sec):
	'''Find groups of hashtags in 60 second windows.'''
	lag = df.index - timedelta(seconds=sec)
	idx = pd.DataFrame({"date": df.index, 
						"text": df.text.values,
						"end_loc": np.searchsorted(df.index.astype(np.int64), lag.astype(np.int64),side='right')}) # find values within 60 seconds of each other
	idx["index"]=idx.index
	return idx


#=========
# do work
#=========

if __name__ == "__main__":

	out = []
	verbose=False
	for i in open(sys.argv[1], 'r').readlines():
		try:
			data = json.JSONDecoder().raw_decode(i)
			hash = list(data)[0]
			text = hash["text"].rstrip('\n\r') # remove newline characters
			clean_text = text.encode("ascii","ignore") # removes unicode
			date = dateutil.parser.parse(hash["created_at"])
			out.append([map(lambda x:x.upper(),get_tags(clean_text)),date]) # make hashtags uppercase to avoid case-senstive duplications
		except:
			if verbose==True: print "No useable data on this line:", hash
			continue

	out.sort(key=lambda l_t: l_t[1]) # make sure the data are date sorted, otherwise searching will be not be fast

	df = pd.DataFrame(out)
	df.columns = ['text', 'date']
	df = df.set_index('date')
	df = get_time_groups(df, 61.0)

	def windowed_mean_degree(z, plot=False): # can change plot to True to generate network graphs
		with warnings.catch_warnings():
			warnings.simplefilter("ignore", category=RuntimeWarning) # catch and ignore nan warnings
			g =  create_graph( [x for x in df["text"][z["end_loc"]:z["index"]+1].values.tolist() if x] ) # note that df is not private to this function...
			to_prune = nx.isolates(g) # find isolate nodes
			g.remove_nodes_from(to_prune) # remove isolate nodes
			m_d = np.mean( nx.degree(g).values() )
			if plot==True:
				nx.draw(g,with_labels=True)
				a = str(datetime.datetime.now())
				plt.savefig("path"+a+".png")
				plt.close()
			return np.round(m_d, decimals=2) # return to 2 decimals

	mean_degrees = df.apply(windowed_mean_degree,axis=1)

	for i in mean_degrees:
		print i