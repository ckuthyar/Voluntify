from django.db import models
class users(models.Model):
    name1=models.CharField(max_length=100)
    date1=models.DateField()
    activity1=models.CharField(max_length=500)
    duration1=models.IntegerField()

    def __str__(self):
        return self.name1
   


