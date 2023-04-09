from django.urls import path
from home import views
from blog import views as bv
from diary import views as dv
from chatbot import views as cv

urlpatterns = [
    path('', views.index, name="index"),
    path('community/', views.index2, name="community"),
    path('login.html',views.login1 ,name="login"),
    path('afterlogin.html',views.afterlogin,name="afterlogin"),
    path('blog_index.html', bv.PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', bv.PostDetail.as_view(), name='blog_post_detail'),
    path('diary.html',dv.index,name='diary_home'),
    path('add.html', dv.add,name='add'),
    path('chatbot/index.html',cv.index,name='index'),
    path('getResponse',cv.getResponse,name='getResponse'),
    path('therapist.html',views.therapist,name="therapist"),
    path('games.html',views.games,name="games"),
    path('sos.html',views.sos,name="sos"),

]
