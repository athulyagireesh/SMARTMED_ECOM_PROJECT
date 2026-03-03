# from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    age = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


# class Task(models.Model):
#     STATUS_CHOICES = (
#         ('To Do', 'To Do'),
#         ('In Progress', 'In Progress'),
#         ('On Testing', 'On Testing'),
#         ('Completed', 'Completed'),
#     )

#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     assigned_date = models.DateField(auto_now_add=True)
#     deadline = models.DateField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')

#     def __str__(self):
#         return self.title