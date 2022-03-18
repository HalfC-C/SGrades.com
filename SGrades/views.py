from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class GlobalRankingView(TemplateView):
    template_name = 'globalranking.html'


class SubjectRankingView(TemplateView):
    template_name = 'subjectranking.html'


class ExpedientView(TemplateView):
    template_name = 'expedient.html'


class GradesView(TemplateView):
    template_name = 'grades.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
