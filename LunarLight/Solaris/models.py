import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Course(models.Model):
    name = models.CharField('Course Name', max_length=160)
    creation_date = models.DateTimeField('Creation date', default=timezone.now(), editable=False)
    description = models.TextField('Description', max_length=1000)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')

    def __str__(self):
        return self.name

    def was_started_recently(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    name = models.CharField('Topic Name', max_length=160)
    creation_date = models.DateTimeField('Creation date', default=timezone.now(), editable=False)
    description = models.TextField('Description', max_length=1000)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')

    def __str__(self):
        return self.name

    def was_started_recently(self):
        return self.start_date >= timezone.now() - datetime.timedelta(days=1)

