
from django.db import models

# This code added from Github account.

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    esal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ename

