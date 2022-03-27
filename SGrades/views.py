from django.views.generic import ListView, TemplateView, DeleteView, DetailView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .models import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

def GlobalRankingView(request):

    Grades_list = Grade.objects.all()
    Student_list = Student.objects.all()
    Subject_number = Subject.objects.count()

    # print(Subject_number)
    counter = 1
    best_students = []

    for student in Student_list:
        student.Expedient = student.expedient_mean
        # print(student.Expedient)

        if best_students == []:
            best_students.append(student)
        else:
            for best in best_students:
                index = best_students.index(best)
                if student.Expedient <= best.Expedient:
                    best_students.insert(index + 1, student)
                    break
                else:
                    best_students.insert(index, student)
                    break

    for student in best_students:
        student.Ranking = best_students.index(student) + 1
    # print(best_students)


    # means = []
    # expedient_means = []
    # best_students = []

    # for student in Student_list:
    #     for grade in Grades_list:
    #         grade.Mean = grade.mean
    #         # print(grade.Mean)
        
    #         if grade.Student.Name == student.Name:
    #             means.append(grade.Mean)
    #             # print(grade.Student.Name)   
        
    #     expedient_mean = sum(means)/Subject_number
    #     print(expedient_mean)
         
    #     means = []

   
    context = {
        'best_students' : best_students,
        # 'counter' : counter,
    }

    return render(request, 'globalranking.html', context)

# class GlobalRankingView(TemplateView):
#     template_name = 'globalranking.html'


def SubjectRankingView(request):

    Grades_list = Grade.objects.all()
    Subject_list = Subject.objects.all()

    for grades in Grades_list:
        grades.Mean = grades.mean
        # print(grades.Mean)

    best_students = []

    for subject in Subject_list:
        for grades in Grades_list:
            if grades.Subject_Grades.Subject_Name == subject.Subject_Name:
                # print(subject)
                # print(grades.Student.Name)
                # print(grades.Mean)

                if best_students == []:
                    best_students.append(grades.Student)
                else:
                    for best in best_students:
                        index = best_students.index(best)
                        if grades.Student.Expedient <= best.Expedient:
                            best_students.insert(index + 1, grades.Student)
                            break
                        else:
                            best_students.insert(index, grades.Student)
                            break

        # print(best_students)
        subject.Best_Student = best_students[0]
        # print(subject.Best_Student)
        best_students = []
        

    context = {
        'Subject_list': Subject_list,
        'Grades_list' : Grades_list,
    }
    return render(request, 'subjectranking.html', context)
     


# class ExpedientView(TemplateView):
#     template_name = 'expedient.html'

def ExpedientView(request):

    try:
        current_student = User.objects.get(username = request.user)
    except:
        context = {}
        return render(request, 'grades.html', context)

    missing_user = True
    Student_list = Student.objects.all()

    for student in Student_list:
        if current_student.username == student.Name:
            missing_user = False


   # Student_list = Student.objects.get(Name = current_student)
    Subjects_list = Subject.objects.all()
    Grades_list = Grade.objects.all()
    # Item_list = Item.objects.all()

    # Submit_list = Submit.objects.all()

    context = {
        'missing_user' : missing_user,
        'current_student' : current_student.username,
        'Subjects_list' : Subjects_list,
        'Grades_list' : Grades_list
    }

    for grades in Grades_list:
        # print(grades)
        # print(f'{grades.Student.Name} --- {grades.Subject_Grades.Subject_Name} --- {grades.mean}')
        grades.Mean = grades.mean
        # print('\n')

    # grades = []

    # for grade in Grades_list:
    #     for subject in Subjects_list:
    #         if grade.Student.Name == current_student.username and grade.Subject_Grades.Subject_Name == subject.Subject_Name:
    #             for submit in Submit_list:
    #                 for item in Item_list:
    #                     if submit.Student.Name == current_student.username \
    #                         and item.Item_From_Subject.Subject_Name == subject.Subject_Name \
    #                         and submit.Item_Submitted.Item_Name == item.Item_Name:
    #                         value = item.Ponderation * (submit.Punctuation / 100)
    #                         grades.append(value)

    #             grade.Mean = round(sum(grades), 2)
    #             grades = []

    return render(request, 'expedient.html', context)

# class GradesView(TemplateView):
#     template_name = 'grades.html'


def GradesView(request):

    try:
        current_student = User.objects.get(username = request.user)
    except:
        context = {}
        return render(request, 'grades.html', context)

    missing_user = True
    Student_list = Student.objects.all()

    for student in Student_list:
        if current_student.username == student.Name:
            missing_user = False

    Submit_list = Submit.objects.all()
    Grades_list = Grade.objects.all()

    context = {
        'Submit_list' : Submit_list,
        'Grades_list' : Grades_list,
        'missing_user' : missing_user,
        'current_student' : current_student.username,
    }

    return render(request, 'grades.html', context)




# class LoginView(TemplateView):
#     template_name = 'login.html'




def EditorModeView(request):

    context = {}
    return render(request, 'editormode.html', context)

class EditorNewStudentView(CreateView):
    model = Student#, Subject, Grade, Submit, Item
    template_name = 'edit_new_student.html'    
    fields = ['Student_Nif', 'Name','Surname', 'Course']

class EditorDeleteStudentView(DeleteView):
    model = Student
    template_name = 'edit_delete_student.html'
    success_url = reverse_lazy('student_list')

class EditorChangeStudentView(UpdateView):
    model = Student
    template_name = 'edit_change_student.html'
    fields = ['Student_Nif', 'Name','Surname', 'Course']

def StudentListView(request):
    return render(request, 'student_list.html', {'Student_list' : Student.objects.all()})

class StudentDetailView(DetailView):
    model = Student
    template_name = 'detail_student.html'




class EditorNewGradeView(CreateView):
    model = Grade#, Subject, Grade, Submit, Item
    template_name = 'edit_new_grade.html'    
    fields = ['Student', 'Subject_Grades']

def GradesListView(request):
    return render(request, 'grades_list.html', {'Grades_list' : Grade.objects.all()})

class EditorChangeGradeView(UpdateView):
    model = Grade
    template_name = 'edit_change_grade.html'
    fields = ['Student', 'Subject_Grades']

class EditorDeleteGradeView(DeleteView):
    model = Grade
    template_name = 'edit_delete_grade.html'
    success_url = reverse_lazy('grades_list')

class GradeDetailView(DetailView):
    model = Grade
    template_name = 'detail_grade.html'



class EditorNewSubmitView(CreateView):
    model = Submit#, Subject, Grade, Submit, Item
    template_name = 'edit_new_submit.html'    
    fields = ['Student', 'Item_Submitted','Punctuation']

class EditorDeleteSubmitView(DeleteView):
    model = Submit
    template_name = 'edit_delete_submit.html'
    success_url = reverse_lazy('submit_list')

class EditorChangeSubmitView(UpdateView):
    model = Submit
    template_name = 'edit_change_submit.html'
    fields = ['Student', 'Item_Submitted','Punctuation']

def SubmitListView(request):
    return render(request, 'submit_list.html', {'Submit_list' : Submit.objects.all()})
class SubmitDetailView(DetailView):
    model = Submit
    template_name = 'detail_submit.html'



class EditorNewItemView(CreateView):
    model = Item#, Subject, Grade, Submit, Item
    template_name = 'edit_new_item.html'    
    fields = ['Item_Name', 'Item_From_Subject','Ponderation', 'Date']

class EditorDeleteItemView(DeleteView):
    model = Item
    template_name = 'edit_delete_item.html'
    success_url = reverse_lazy('item_list')

class EditorChangeItemView(UpdateView):
    model = Item
    template_name = 'edit_change_item.html'
    fields = ['Item_Name', 'Item_From_Subject','Ponderation', 'Date']

def ItemListView(request):
    return render(request, 'item_list.html', {'Item_list' : Item.objects.all()})
class ItemDetailView(DetailView):
    model = Item
    template_name = 'detail_item.html'



class EditorNewSubjectView(CreateView):
    model = Subject#, Subject, Grade, Submit, Item
    template_name = 'edit_new_subject.html'    
    fields = ['Subject_Name', 'Course']

class EditorChangeSubjectView(UpdateView):
    model = Subject
    template_name = 'edit_change_subject.html'

class EditorDeleteSubjectView(DeleteView):
    model = Subject
    template_name = 'edit_delete_subject.html'
    success_url = reverse_lazy('subject_list')

def SubjectListView(request):
    return render(request, 'subject_list.html', {'Subject_list' : Subject.objects.all()})
class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'detail_subject.html'

