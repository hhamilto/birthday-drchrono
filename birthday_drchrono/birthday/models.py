from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField('Birthday')
    doctor = models.ForeignKey(Doctor)
    def __unicode__(self):
        return self.name


'''class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''