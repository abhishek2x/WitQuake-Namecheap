from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.deletion import CASCADE
from django.db.models import CharField

# Create your models here.


class Dashboard(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(16)])
    gender = models.CharField(max_length=40, default="female",
        choices=(("male", "male"), ("female", "female"), ("prefer not to tell", "prefer not to tell"),
                 ("other", "other")))

    profession = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='default1.jpeg')
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.user.username


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=Dashboard, on_delete=CASCADE, null=True, blank=True)
    claps = models.IntegerField(default=0)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.id


class AddReply(models.Model):
    reply = models.TextField(default="")
    to = models.ForeignKey(to=Question, on_delete=CASCADE, null=True, blank=True)
    by = models.ForeignKey(to=Dashboard, on_delete=CASCADE, null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.by
