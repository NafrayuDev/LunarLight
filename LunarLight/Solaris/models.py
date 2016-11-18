import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=160)
    creation_date = models.DateTimeField('creation date')
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    def __str__(self):
        return self.attr_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    name = models.CharField(max_length=160)
    creation_date = models.DateTimeField('creation_date')
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField('start_date')
    end_date = models.DateTimeField('end_date')

    def __str__(self):
        return self.attr_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

