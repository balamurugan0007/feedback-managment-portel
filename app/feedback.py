from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import  JsonResponse
from .models import products,review
from  vaderSentiment.vaderSentiment  import SentimentIntensityAnalyzer

def feed(request):
    return render(request,"feedback.html")



def portel(request):
    if request.method=="POST":
        name=request.POST["user"]
        
        password1=request.POST['pass1']
       
        
        if name=='':
            return render(request,"feed.html",{'error':'please enter the username'})
        
        
                    

        if password1=='':
            return render(request,"feed.html",{'error':'please enter the password'})
        
        return render(request,"feedback.html")
        
        
       
       


    return render(request,'feed.html')











def Ratings(request,id):
    if request.method=="POST":
        name=request.POST["user"]
        email=request.POST['rate']
        password1=request.POST['feedback']
      
        

        obj=review()
        obj.name=name
        obj.rate=email
        obj.reviews=password1


        #.......product name.........
        if(products.objects.filter(id=id)):
            name=products.objects.filter(id=id)
            for item in name:
                product_name=item.name
        
                obj.productname = product_name
        
        
        
        #........sentiment analysis.........

        sentence=password1

        #.........analysor sentiment........
        analyzer = SentimentIntensityAnalyzer()
        
        sentiment_dict=analyzer.polarity_scores(sentence)

        print("overall sentiment dictonary is :",sentiment_dict)
        Positive=sentiment_dict['neg']
        Neutral=sentiment_dict['neu']
        Negative=sentiment_dict['pos']
        obj.pos=Positive
        obj.neu=Neutral
        obj.neg=Negative



            #........setiment splitting.............

        if sentiment_dict['compound']>0.05 and sentiment_dict['compound']<-0.05:
            a='normal'
            obj.overall=a

        elif sentiment_dict['compound']<= -0.05:
            b="negative"
            obj.overall=b
            
        else:
            c="positive"
            obj.overall=c
        
      
        #obj.save()

        #catogory spliting.................................................


# catogories splitting  , keywords for catogory spliting ............ 
        categories = {
                
                'Service': ['waiter', 'staff', 'service', 'friendly', 'attentive'],
                
                'Price': ['value', 'expensive', 'affordable', 'cheap','money','price'],
                'Appearance':['looks','look','feel','color'],
                'Quality':['lifetime','works','working','process','quality','product']

                }

# Get user feedback
        feedback = password1
        a=[]

# Check which category the feedback falls into
        for category,keywords in categories.items():
            for keyword in keywords:
                if keyword in feedback.lower():
                    print('Your feedback is:', category)
                    cat=category
                    a.append(cat)
                    print(a)

        obj.catogory=a
                    
                    
            


        # .......objects has storedin a database............
        obj.save()






        
    return render(request,"ratings.html")


def Sentiment(request):
    feedback=review.objects.all()

    if request.method=="POST":
        find = request.POST.get('search')
        print(find)
        if (products.objects.filter(name=find)):
            product_details=products.objects.filter(name=find)
        if (review.objects.filter(productname=find)):
            review_details=review.objects.filter(productname=find)

            return render (request,'seprate.html',{'data':review_details,"product":product_details})

            
                
                    
        

    return render(request,"analysis.html",{"data":feedback})


def seprate(request):
    
    return render(request,'seprate.html')
    


