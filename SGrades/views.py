import statistics
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class GlobalRankingView(TemplateView):
    template_name = 'globalranking.html'


class SubjectRankingView(TemplateView):
    template_name = 'subjectranking.html'


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
    Item_list = Item.objects.all()

    Submit_list = Submit.objects.all()

    context = {
        'missing_user' : missing_user,
        'current_student' : current_student.username,
        'Subjects_list' : Subjects_list,
        'Grades_list' : Grades_list
    }

    grades = []

    for grade in Grades_list:
        for subject in Subjects_list:
            if grade.Student.Name == current_student.username and grade.Subject_Grades.Subject_Name == subject.Subject_Name:
                for submit in Submit_list:
                    for item in Item_list:
                        if submit.Student.Name == current_student.username \
                            and item.Item_From_Subject.Subject_Name == subject.Subject_Name \
                            and submit.Item_Submitted.Item_Name == item.Item_Name:
                            value = item.Ponderation * (submit.Punctuation / 100)
                            grades.append(value)

                grade.Mean = round(sum(grades), 2)
                grades = []

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


class RegisterView(TemplateView):
    template_name = 'register.html'

