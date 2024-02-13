from django.db import models

class Position(models.Model):
    title = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    position = models.ForeignKey(Position,on_delete = models.CASCADE)
    
