from django.urls import path
from learn import views

urlpatterns = [

    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    # path('home/', views.index, name='index'),
    # path('team/', views.team, name='team'),

    path('education/article/', views.article, name='article'),
    path('education/mindpuzzle/', views.mindPuzzle, name='mindPuzzle'),
    path('services/', views.services, name='services'),
    # path('techmagic/', views.techmagic, name='techmagic'),
    path('contact/', views.contact, name='contact'),
    # path('software/', views.software, name='software'),
    # path('', views.index, name='index'),      ---->          PAGE-7 NOT USED
    path('education/training/', views.training, name='training'),
]
