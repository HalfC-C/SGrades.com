from django.urls import path
from .views import *

urlpatterns = [
    path('globalranking/', GlobalRankingView, name='Global Ranking'),
    path('expedient/', ExpedientView, name='Expedient'),
    path('grades/', GradesView, name='Grades'),
    path('subjectgrades/', SubjectRankingView.as_view(), name='Subject Ranking'),
   # path('login/', LoginView.as_view(), name='Login'),
    #path('register/', RegisterView.as_view(), name='Register'),
    path('', HomePageView.as_view(), name='home'),
]