from django.urls import path
from django.urls.conf import include
from community import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('', views.Welcome.as_view(), name='forum'),
    # path('about/', views.About.as_view()),

    path('question', views.QuestionListView.as_view()),
    path('question/<int:pk>', views.QuestionDetailView.as_view()),   
    path('question/create/', views.QuestionCreate.as_view(success_url="/forum/question")),

    path('dashboard/', views.DashboardListView.as_view()),
    path('dashboard/<int:pk>', views.DashboardDetailView.as_view()),   
    path('dashboard/edit/<int:pk>/',
         views.DashboardUpdateView.as_view(success_url="/forum/question")),
    
    # path('question/upload', views.QuestionUpload.as_view(), name='reply_ajax_create'),
    path('question/upload', views.quesUpload),

    # path('question/<int:pk>', views.  ReplayLayover, name='ReplayLayover'),
    
    # path('ajax/increase_clap/', views.ajax_increase_clap, name='ajax_increase_clap')
]
