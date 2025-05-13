from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    expire_date = models.DateTimeField('expired date')
    
    def __str__(self):
        return self.question_text