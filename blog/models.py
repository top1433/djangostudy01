from django.db import models

# Create your models here.


class Person(models.Model):
    # def __init__(self,name,password):
    #     self.name = name
    #     self.password = password
    name = models.TextField(200)
    password = models.TextField(200)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text =models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text