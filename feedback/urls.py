"""fashionworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app import feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign_in,name='signin'),
    path('home',views.home,name='home'),
    
    path('home/<int:id>',views.collectionsview,name="collections"),
    path('home/catogory/products/<int:id>',views.productview,name="products"),
    
    path('login', views.login,name='login'),
    
    
    path('search',views.search,name='search'),
    path('err',views.search,name='err'),
    
    
    
    #feedback portes views
    
    path('portel',feedback.portel,name='portel'),
    path('feedbackportel',feedback.feed,name="feed"),
   
    path('home/ratings/<int:id>',feedback.Ratings,name='ratings'),
    path('portel/sentiment',feedback.Sentiment,name='sentiment'),
    path('portel/seprate',feedback.seprate,name='seprate'),
     path('portel/seprate/<str:name>',feedback.seprate,name='seprate12'),

    
    

    ]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)