# Generated by Django 4.0.3 on 2022-03-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGrades', '0004_subject_best_student_alter_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Course',
            field=models.CharField(choices=[('3', 'Tercer curso')], max_length=1),
        ),
    ]
