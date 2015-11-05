import sys
import json
from dateutil.parser import parse

#=========
# do work
#=========
if __name__ == "__main__":

	num_unicode = 0

	verbose=False
	for i in open(sys.argv[1], 'r').readlines():
		try:
			data = json.JSONDecoder().raw_decode(i)
			hash = list(data)[0]
			text = hash["text"].rstrip('\n\r') # remove newline characters
			clean_text = text.encode("ascii","ignore").replace('\n', ' ') # removes unicode and get rid of interspersed newline characters
			date = parse(hash["created_at"])
			print clean_text, "(timestamp: " + str(date) + ")" # printing as string literals will process the escape characters
		except KeyError:
			if verbose==True: print "No useable data on this line:", hash
			continue
		try:
			text.decode('utf-8') # should fail in contact with unicode characters
		except UnicodeError:
			num_unicode+=1 # count number of unicode tweets
			continue

	print "\n" + str(num_unicode) + " tweet(s) contained unicode"