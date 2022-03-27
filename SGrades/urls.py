from django.urls import path
from .views import *

urlpatterns = [
    path('globalranking/', GlobalRankingView, name='Global Ranking'),
    path('expedient/', ExpedientView, name='Expedient'),
    path('grades/', GradesView, name='Grades'),
    path('subjectgrades/', SubjectRankingView, name='Subject Ranking'),
   # path('login/', LoginView.as_view(), name='Login'),
    #path('register/', RegisterView.as_view(), name='Register'),
    path('', HomePageView.as_view(), name='home'),
    path('editormode/', EditorModeView, name='editormode'),
    path('editormode/editornewstudent/', EditorNewStudentView.as_view(), name='editornewstudent'),
    path('editormode/editornewgrade/', EditorNewGradeView.as_view(), name='editornewgrade'),
    path('editormode/editornewitem/', EditorNewItemView.as_view(), name='editornewitem'),
    path('editormode/editornewsubject/', EditorNewSubjectView.as_view(), name='editornewsubject'),
    path('editormode/editornewsubmit/', EditorNewSubmitView.as_view(), name='editornewsubmit'),

]