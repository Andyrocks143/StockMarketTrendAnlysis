from nltk.classify import NaiveBayesClassifier
from nltk.sentiment.util import demo_tweets
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk import FreqDist
import pickle

tokenizer = TweetTokenizer()

pos_tweet_file = "pos_tweets_list.txt"
neg_tweet_file = "neg_tweets_list.txt"

word_list = list()

def tokenize_tweet(tweet):
    #Tokenizes the tweet and removes stopwords
    tokenized_tweet = tokenizer.tokenize(tweet)
    final_tweet = list()
    english_stopwords = stopwords.words('english')
    for word in tokenized_tweet:
        if word not in english_stopwords:
            final_tweet.append(word.lower())
    return final_tweet


#Stuff to do:
#Create the bag of words

def find_tokens(filename):
    file_tokens = list()
    with open(filename, 'r') as f:
        for line in f:
            file_tokens += tokenize_tweet(line)
    return file_tokens


def create_token_list():
    token_list = list()
    token_list += find_tokens(pos_tweet_file)
    token_list += find_tokens(neg_tweet_file)
    return token_list

def find_feature_for_tweet(tweet):
    global word_list
    tokenized_tweet = tokenize_tweet(tweet)
    feature = dict()
    for token in tokenized_tweet:
        feature[token] = (token in word_list)
    return feature

def create_feature_list(word_list):
    feature_list = list()
    with open(pos_tweet_file, 'r') as f:
        for tweet in f:
            feature_list.append([find_feature_for_tweet(tweet), 'positive'])

    with open(neg_tweet_file, 'r') as f:
        for tweet in f:
            feature_list.append([find_feature_for_tweet(tweet), 'negative'])

    return feature_list


#Train the NaiveBayesClassifier
def train_classifier(word_list):
    feature_list = create_feature_list(word_list)
    classifier = NaiveBayesClassifier.train(feature_list)
    class_f = open('naive_bayes_classifier', 'w+')
    pickle.dump(classifier, class_f)
    class_f.close()


tweet_token_list = create_token_list()
bag_of_words = FreqDist(tweet_token_list)
word_list = list(bag_of_words.keys())

train_classifier(word_list)
