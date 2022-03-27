from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Student(models.Model):

    COURSES = (
        ('3', 'Tercer curso'),
    )

    Student_Nif = models.CharField(primary_key=True, max_length=10)
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=50)
    Expedient = models.FloatField(blank=True, default=0, editable=False)
    # DisplayFields = ['Student_Nif', 'Name', 'Surname']
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
            # print(grade.Mean)    
            if grade.Student.Name == self.Name:
                means.append(grade.Mean)
                # print(grade.Student.Name)   
            
        expedient_mean = sum(means)/Subject_number
        # print(expedient_mean)       

        return expedient_mean

class Subject(models.Model):
    #TODO: se supone que el usuario debe poder poner estas cosas, mirar como se hace para que el usuario pueda interactuar
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

class Teaching(models.Model):
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
     #TODO: una asignatura se puede dar en diferentes clases a diferentes horarios
    
    HOURS = (
        ('9', '9:00 - 10:50'),
        ('11', '11:10 - 13:00'),
        ('15', '15:00 - 16.50'),
        ('17', '17:10 - 19:00'),
        ('19', '19:10 - 21:00')
    )
    ROOMS = (
        ('3', '0.03'),
        ('4', '0.04'),
        ('1.01', 'Alcatel'),
        ('1.03', 'Sala master'),
    )

    DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    )
    
    Schedule = models.CharField(choices=HOURS, max_length=2)
    Classroom = models.CharField(choices=ROOMS, max_length=4)
    Professor = models.CharField(max_length=50)
    Day = models.CharField(choices=DAYS, max_length=3)

    def __str__(self):
        return f'{self.Subject}'


class Item(models.Model):
    Item_Name = models.CharField(primary_key=True, max_length=100)
    Item_From_Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Ponderation = models.FloatField('Grades percentage, from 0 to 100%')
    #Puntuation = models.FloatField(max_length=5, default=0)
    Date = models.DateField()

    def __str__(self):
        return f'{self.Item_Name}'

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.pk)])


#TODO: esta clase no es necesaria, porque lo puede mostrar la vista y ya. Se puede conservar como forma de conservar los datos, pero que no hace falta
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

        Subjects_list = Subject.objects.all()
        Grades_list = Grade.objects.all()
        Item_list = Item.objects.all()
        Submit_list = Submit.objects.all()

        grades = []
        means = []


        # for subject in Subjects_list:
        #     if subject.Subject_Name == self.Subject_Grades.Subject_Name:
        #         print(subject)
        #         for submit in Submit_list:
        #             for item in Item_list:
        #                 if item.Item_From_Subject.Subject_Name == subject.Subject_Name \
        #                     and submit.Item_Submitted.Item_Name == item.Item_Name \
        #                     and self.Student.Name == submit.Student.Name:
        #                     print(f'{self.Student.Name} in subject {self.Subject_Grades.Subject_Name}, item {submit.Item_Submitted.Item_Name} got punctuation of {submit.Punctuation}')
        #                     value = item.Ponderation * (submit.Punctuation / 100)
        #                     grades.append(round(value, 2))
        #                     print(round(value, 2))
        #                     mean_value = round(sum(grades), 2)
        #                     print(mean_value)
        #                     self.Mean = mean_value
                    
        #             grades = []
        # return mean_value


        for item in Item_list:
            #print(f'item: {item}')
            if self.Subject_Grades.Subject_Name == item.Item_From_Subject.Subject_Name:
             #   print(f'{self.Subject_Grades.Subject_Name} : {item.Item_Name}')
                for submit in Submit_list:
                    if submit.Item_Submitted.Item_Name == item.Item_Name \
                        and submit.Student.Name == self.Student.Name:
                        value = item.Ponderation * (submit.Punctuation / 100)
                        grades.append(round(value, 2))
                        # print(submit.Punctuation)
                        # print(grades)
                        means.append(round(value, 2))
                # return sum(means)
        return(round(sum(means), 2))



        return 'no more none'
        # for grade in Grades_list:
        #     for subject in Subjects_list:
        #         if grade.Subject_Grades.Subject_Name == subject.Subject_Name:
        #             for submit in Submit_list:
        #                 for item in Item_list:
        #                     if item.Item_From_Subject.Subject_Name == subject.Subject_Name \
        #                         and submit.Item_Submitted.Item_Name == item.Item_Name \
        #                             and grade.Student.Name == submit.Student.Name:
        #                         value = item.Ponderation * (submit.Punctuation / 100)
        #                         grades.append(value)
        #             mean = round(sum(grades), 2)
        #             grade.Mean = mean
        #             means.append(grade)
        #             grades = []
        # return means

class Submit(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Item_Submitted = models.ForeignKey(Item, on_delete=models.CASCADE)
    Punctuation = models.FloatField(max_length=5, default=0)

    def __str__(self):
        return f'{self.Student} --- {self.Item_Submitted}'

    def get_absolute_url(self):
        return reverse('submit_detail', args=[str(self.pk)])

