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

    Student_list = Student.objects.get(Name = current_student)
    Subjects_list = Subject.objects.all()
    Grades_list = Grade.objects.all()
    Item_list = Item.objects.all()

    Submit_list = Submit.objects.all()

    context = {
        'Student_list' : Student_list,
        'Subjects_list' : Subjects_list,
        'Grades_list' : Grades_list
    }

    grades = []
    # grades2 = []
    # student_subjects = []
    # student_items = []

    for grade in Grades_list:
        for subject in Subjects_list:
            if grade.Student.Name == current_student.username and grade.Subject_Grades.Subject_Name == subject.Subject_Name:
                # print(subject)
                for submit in Submit_list:
                    for item in Item_list:
                        if submit.Student.Name == current_student.username \
                            and item.Item_From_Subject.Subject_Name == subject.Subject_Name \
                            and submit.Item_Submitted.Item_Name == item.Item_Name:
                            # print(f'{subject.Subject_Name} --- {submit.Item_Submitted.Item_Name} -- {item.Ponderation} --- {submit.Punctuation}')
                            value = item.Ponderation * (submit.Punctuation / 100)
                            # print(item.Ponderation * (submit.Punctuation / 100))
                            grades.append(value)

                grade.Mean = sum(grades)

                grades = []
                # print(f'{subject.Subject_Name} --- {grade.Mean}')

    return render(request, 'expedient.html', context)


# class GradesView(TemplateView):
#     template_name = 'grades.html'


def GradesView(request):

    try:
        current_student = User.objects.get(username = request.user)
    except:
        context = {}
        return render(request, 'grades.html', context)

    Submit_list = Submit.objects.all()
    Student_list = Student.objects.get(Name = current_student)
    Grades_list = Grade.objects.all()
    Item_list = Item.objects.all()

    # for grades in Grades_list:
    #     if grades.Student_Nif.Name == Student_list.Name:
    #         print(grades.Subject_Grades.Subject_Name)

    #         for item in Item_list:
    #             if item.Item_From_Subject.Subject_Name == grades.Subject_Grades.Subject_Name:
    #                 print(item.Puntuation)

    context = {
        'Submit_list' : Submit_list,
        'Student_list' : Student_list,
        'Grades_list' : Grades_list,
       # 'Item_list' : Item_list,
    }

    return render(request, 'grades.html', context)




# class LoginView(TemplateView):
#     template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'

