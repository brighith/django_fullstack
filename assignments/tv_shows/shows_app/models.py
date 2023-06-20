from django.db import models
from datetime import datetime, date


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        relaised = datetime.strptime(
            postData['release_date'], '%Y-%m-%d')
        if len(postData['title']) == 0:
            errors["title"] = "Title is requerid"
        if len(postData['network']) == 0:
            errors["network"] = "Network is a must"
        # if len(postData['description']) == 0:
        #     errors["description"] = "Description is preferable"
        if 0 < len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if 0 < len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if 0 < len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        if relaised > datetime.today():
            errors["release_date"] = "The date should be in the past"
        if Show.objects.filter(title=postData['title']):
            errors["title"] = 'This Title Exist, try to use a unique Title'

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
