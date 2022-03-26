from django.db import models

# Create your models here.


class Student(models.Model):
    Student_Nif = models.CharField(primary_key=True, max_length=10)
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=50)
    Expedient = models.FloatField(blank=True, default=0, editable=False)
    # DisplayFields = ['Student_Nif', 'Name', 'Surname']

    def __str__(self):
        return f'{self.Name} {self.Surname}'

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
   
    

    def __str__(self):
        return f'{self.Subject_Name}'

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
    Ponderation = models.IntegerField('Grades percentage, from 0 to 100%')
    #Puntuation = models.FloatField(max_length=5, default=0)
    Date = models.DateField()

    def __str__(self):
        return f'{self.Item_Name}'

#TODO: esta clase no es necesaria, porque lo puede mostrar la vista y ya. Se puede conservar como forma de conservar los datos, pero que no hace falta
class Grade(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject_Grades = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Mean = models.FloatField(editable=False, default=0)

    class Meta:
        unique_together = (('Student', 'Subject_Grades'),)

    def __str__(self):
        return f'{self.Student} ----- {self.Subject_Grades}'
        
    # @property
    # def mean(self):
    #     grades = []
    #     grades_list = Grades.objects.all()
    #     items_list = Item.objects.all()
    #     for grades in grades_list:
    #         print(grades)

class Submit(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Item_Submitted = models.ForeignKey(Item, on_delete=models.CASCADE)
    Punctuation = models.FloatField(max_length=5, default=0)

    def __str__(self):
        return f'{self.Student} --- {self.Item_Submitted}'

