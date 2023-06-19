from django.db import models
import re
from datetime import date, datetime
import bcrypt
from dateutil.relativedelta import relativedelta


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2 or not postData['fname'].isalpha():
            errors["fname"] = "first name should be at least 2 chars and contains letters only"
        if len(postData['lname']) < 2 or not postData['fname'].isalpha():
            errors["lname"] = "last name should be at least 2 chars and contains letters only"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "THe password must be 8 characters minimum"
        if postData['password'] != postData['pwdconfirm']:
            errors['password'] = "Passwords are note the same"
        # validation for the user birthday
        if postData['birthday'] == '':
            errors['birthday'] = "Please enter birthday"
        else:
            user_birthday = datetime.strptime(
                postData['birthday'], '%Y-%m-%d')
            if user_birthday > datetime.today():
                errors['release_date'] = "User birthday must be in the past!"

            if user_birthday > datetime.today() - relativedelta(years=13):
                errors["release_date"] = "User must be at least 13"
        return errors

    def login_validator(self, postData):
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors2 = {}
        email2 = postData['email2']
        password2 = postData['password2']
        usr = User.objects.filter(email=email2)
        if len(email2) < 1:
            errors2["email2"] = "Email cannot be empty!"
        elif not EMAIL_REGEX.match(email2):
            errors2["email2"] = "Invalid Email Address!"

        elif not bcrypt.checkpw(password2.encode(), usr[0].password.encode()):
            errors2["password2"] = "Incorrect password. Try again!"

        return errors2


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    birthday = models.DateField(default='1900-01-01')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
