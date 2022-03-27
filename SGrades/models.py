from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Student(models.Model):

    COURSES = (
        ('3', 'Tercer curso'),
    )

    Student_Nif = models.CharField(primary_key=True, max_length=10)
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=50)
    Expedient = models.FloatField(blank=True, default=0, editable=False)
    Ranking = models.IntegerField(editable=False, default=0)
    Course = models.CharField(choices=COURSES, max_length=1)

    def __str__(self):
        return f'{self.Name} {self.Surname}'

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.pk)])

    @property
    def expedient_mean(self):

        Grades_list = Grade.objects.all()
        Subject_number = Subject.objects.count()

        means = []

        for grade in Grades_list:
            grade.Mean = grade.mean
            if grade.Student.Name == self.Name:
                means.append(grade.Mean)
            
        expedient_mean = sum(means)/Subject_number
        return expedient_mean

class Subject(models.Model):
    NAMES = (
        ('IR', 'Ingenirería de Requisitos'),
        ('MP', 'Modelos de Proceso'),
        ('QMI', 'Gestión y mejora de la calidad'),
        ('WP', 'Proyecto Web'),
        ('ABDIS', 'Ampliación de bases de datos e Ingeniería del Software'),

    )
    COURSES = (
        ('3', 'Tercer curso'),
    )
    
    Subject_Name = models.CharField(primary_key=True, choices=NAMES, max_length=5)
    Course = models.CharField(choices=COURSES, max_length=1)
    Best_Student = models.ForeignKey(Student, on_delete=models.CASCADE, editable=False)
    

    def __str__(self):
        return f'{self.Subject_Name}'

    def get_absolute_url(self):
        return reverse('subject_detail', args=[str(self.pk)])


class Item(models.Model):
    Item_Name = models.CharField(primary_key=True, max_length=100)
    Item_From_Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Ponderation = models.FloatField('Grades percentage, from 0 to 100%')

    Date = models.DateField()

    def __str__(self):
        return f'{self.Item_Name}'

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.pk)])


class Grade(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject_Grades = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Mean = models.FloatField(editable=False, default=0)

    class Meta:
        unique_together = (('Student', 'Subject_Grades'),)

    def get_absolute_url(self):
        return reverse('grade_detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.Student} ----- {self.Subject_Grades}'
        
    @property
    def mean(self):
        Item_list = Item.objects.all()
        Submit_list = Submit.objects.all()

        grades = []
        means = []

        for item in Item_list:
            if self.Subject_Grades.Subject_Name == item.Item_From_Subject.Subject_Name:
                for submit in Submit_list:
                    if submit.Item_Submitted.Item_Name == item.Item_Name \
                        and submit.Student.Name == self.Student.Name:
                        value = item.Ponderation * (submit.Punctuation / 100)
                        grades.append(round(value, 2))
                        means.append(round(value, 2))
        return(round(sum(means), 2))

class Submit(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Item_Submitted = models.ForeignKey(Item, on_delete=models.CASCADE)
    Punctuation = models.FloatField(max_length=5, default=0)

    def __str__(self):
        return f'{self.Student} --- {self.Item_Submitted}'

    def get_absolute_url(self):
        return reverse('submit_detail', args=[str(self.pk)])

