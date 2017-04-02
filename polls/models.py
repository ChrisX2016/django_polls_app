import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
DEFAULT_USER_ID = 2

# todo user profile
# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#
#     def __str__(self):
#         return '<%s>' % self.user.get_username()


class Question(models.Model):
    error_css_class = 'error'
    question_text = models.CharField('Question',max_length=200)
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User,default=DEFAULT_USER_ID)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return '<%s>' % self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '<%s>' % self.question


class Vote(models.Model):
    choice = models.ForeignKey(Choice)
    voter = models.ForeignKey(User,default=DEFAULT_USER_ID)
    vote_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<%s, voter:%s>' % (self.choice, self.voter)


class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name="profile")
    username = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.username