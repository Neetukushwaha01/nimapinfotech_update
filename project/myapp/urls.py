from django.urls import path
from . import views
urlpatterns = [

    path('clients/',views.ClientList.as_view()),
    path('login/',views.LoginView.as_view()),
    path('signup/',views.RagistationView.as_view()),
    path('clients/<pk>',views.ClientDetails.as_view()),

# ClientDetails.get(pk)


    path('projects/',views.ProjectList.as_view()),
    path('index/',views.index_view),

]