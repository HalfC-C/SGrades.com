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
    path('item/<str:pk>/edit_change_student/', EditorChangeStudentView.as_view(), name='edit_change_student'),
    path('editormode/student_list/', StudentListView, name='student_list'),
    path('student/<str:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('item/<str:pk>/edit_delete_student/', EditorDeleteStudentView.as_view(), name='edit_delete_student'),
    
    path('editormode/editornewgrade/', EditorNewGradeView.as_view(), name='editornewgrade'),
    path('grade/<int:pk>/edit_change_grade/', EditorChangeGradeView.as_view(), name='edit_change_grade'),
    path('editormode/grades_list/', GradesListView, name='grades_list'),
    path('grade/<int:pk>', GradeDetailView.as_view(), name='grade_detail'),
    path('grade/<int:pk>/edit_delete_grade/', EditorDeleteGradeView.as_view(), name='edit_delete_grade'),
    
    path('editormode/editornewitem/', EditorNewItemView.as_view(), name='editornewitem'),
    path('item/<str:pk>/edit_change_item/', EditorChangeItemView.as_view(), name='edit_change_item'),
    path('editormode/item_list/', ItemListView, name='item_list'),
    path('item/<str:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('item/<str:pk>/edit_delete_item', EditorDeleteItemView.as_view(), name='edit_delete_item'),
    
    path('editormode/editornewsubject/', EditorNewSubjectView.as_view(), name='editornewsubject'),
    path('subject/<str:pk>/edit_change_subject/', EditorChangeSubjectView.as_view(), name='edit_change_subject'),
    path('editormode/subject_list/', SubjectListView, name='subject_list'),
    path('subject/<str:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subject/<str:pk>/edit_delete_subject/', EditorDeleteSubjectView.as_view(), name='edit_delete_subject'),
    
    path('editormode/editornewsubmit/', EditorNewSubmitView.as_view(), name='editornewsubmit'),
    path('submit/<int:pk>/edit_change_submit/', EditorChangeSubmitView.as_view(), name='edit_change_submit'),
    path('editormode/submit_list/', SubmitListView, name='submit_list'),
    path('submit/<int:pk>/', SubmitDetailView.as_view(), name='submit_detail'),
    path('submit/<int:pk>/edit_delete_submit/', EditorDeleteSubmitView.as_view(), name='edit_delete_submit'),
]