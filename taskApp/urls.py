from django.urls import path
from taskApp import views
urlpatterns=[

                path('home',views.home),
                path('tasks',views.task),
                path('result/<str:slug>',views.result),
            ]
