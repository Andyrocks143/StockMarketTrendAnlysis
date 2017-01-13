import sys
import json

def main():
	tweetScores={}
	if (len(sys.argv) ==3):
		print ("Please enter the sentiment file followed by the tweet file.")
	else:
		sent_file = open("AFINN-111.txt",'r')
		tweet_file = open("test_set_tweets.txt",'r')
		
		#Dictionary for storing the word's sentiment score.
		sentiment_dict = {}
		for line in sent_file:
			word,score = line.split("\t")
			sentiment_dict.setdefault(word,score)
		
		#Fetching all tweets from tweet file.
		count = 0
		tweets=[]
		for line in tweet_file:
			tweets.append(line.split('\t')[2].strip())
			count += 1
			if count > 1000:
				break;
		
		#Assigning scores for the tweets.    		
		for tweet in tweets:
			tweetScore = 0
			for word in tweet.split():
				if (word in sentiment_dict.keys()):
					wordScore = int(sentiment_dict[word])
				else:
					wordScore = 0
				tweetScore += wordScore
			tweetScores.setdefault(tweet,tweetScore)
		#Sorting the tweets in descending order of sentiment scores.
		sortedSentiScore = sorted(tweetScores,key=tweetScores.get, reverse = True)
		
		list_len =  (len(sortedSentiScore))
		#Printing top 10 happiest tweets.
		for values in range(0,10):
			print (tweetScores[sortedSentiScore[values]],": ",sortedSentiScore[values])
		#Printing bottom 10 unhappiest tweets.
		for values in range(list_len-10,list_len):
			print (tweetScores[sortedSentiScore[values]],": ",sortedSentiScore[values])

if __name__ == '__main__':
    main()
