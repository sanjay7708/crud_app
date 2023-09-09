from django.db import models

# Create your models here.
class student(models.Model):
    choices=(
        (17,'17'),
        (18,'18'),
        (19,'19'),
        (20,'20'),
        (21,'21'),
        (22,'22'),
        (23,'23'),
        (24,'24'),
        (25,'25'),

    )
    student_name=models.CharField(max_length=100)
    age=models.IntegerField(choices=choices)
    course=models.CharField(max_length=50)
    passed_out_year=models.CharField(max_length=4)
    insitute_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_No=models.CharField(max_length=10)

    def __str__(self):
        return self.student_name

