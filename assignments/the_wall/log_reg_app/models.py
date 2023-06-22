from datetime import datetime, timedelta
from django.db import models
import datetime
import re


today = datetime.datetime.today()
# ini_time_for_now = datetime.now()
past_date_before_13yrs = today - \
    timedelta(days=4628)


class UserManager(models.Manager):
    def basic_validator(self, post_data):
        date_format = "%Y-%m-%d"
        errors = {}

        if len(post_data['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        if len(post_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if len(post_data['password']) != len(post_data['confirm_password']):
            errors["password"] = "Password doesnt match"
        if datetime.datetime.strptime(post_data['birthday'], date_format) > past_date_before_13yrs:
            errors['birthday'] = "User should be at least 13 years old"
        if datetime.datetime.strptime(post_data['birthday'], date_format) > datetime.datetime.today():
            errors['birthday'] = "Birthday should be in the past"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateField()
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
