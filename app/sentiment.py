from  vaderSentiment.vaderSentiment  import SentimentIntensityAnalyzer


    # passitive feedback
sentence="Perfect fit nice quality fabrics awesome and fast delivery thanks meesho"

#negative feedback
#sentence="Sleepy service, poor food quality, and when we asked why it was like this they stated that their kitchen was backed up, yet the restaurant was damn near empty."
sid_obj=SentimentIntensityAnalyzer()
sentiment_dict=sid_obj.polarity_scores(sentence)

print("overall sentiment dictonary is :",sentiment_dict)
print("sentence rated",sentiment_dict['neg']*100,"%Nagative")
print("sentence rated",sentiment_dict['neu']*100,"%Neutral")
print("sentence rated",sentiment_dict['pos']*100,"%Positive")

a=print(sentiment_dict["neg"])
b=print(sentiment_dict["neu"])
c=print(sentiment_dict["pos"])


#largest number 

if sentiment_dict['compound']>0.05 and sentiment_dict['compound']<-0.05:
    print("normal")

elif sentiment_dict['compound']<= -0.05:
    print("negative")
else:
    print("positve")
