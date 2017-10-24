from django.db import models
import datetime
from datetime import timedelta
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text 

class Store(models.Model):
    store_user = models.ForeignKey('User', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    store_account = models.ForeignKey('Account', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50)


class User(models.Model):
    user_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_position = models.CharField(max_length=50)

class Account(models.Model):
    acount_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    ZipCode = models.ForeignKey('ZipCode', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    routing_number = models.CharField(max_length=50)
    account_name = models.CharField(max_length=50)
    account_street = models.CharField(max_length=50)
    account_state = models.CharField(max_length=50)
    checks_bounced = models.CharField(max_length=50)

class Check(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    check_amount = models.CharField(max_length=50)
    check_number = models.CharField(max_length=50)
    cashier_name = models.CharField(max_length=50)
    check_status = models.CharField(max_length=50)
    letter_date1 = models.CharField(max_length=50)
    letter_date2 = models.CharField(max_length=50)
    letter_date3 = models.CharField(max_length=50)




class ZipCode(models.Model):
    Zip_Code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Client(models.Model):
    client_name = models.CharField(max_length=50)


class Bank(models.Model):
    bank_name = models.CharField(max_length=50)