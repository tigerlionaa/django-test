from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# class CustomerRegistration(AbstractUser):
#     phone_number = models.CharField(max_length=40, unique=True)

#     username =
#     other_number = 
    
#     REQUIRED_FIELDS = ['phone_number', 'username']

#     def __str__(self):
#         return self.user.username


PLAN_CHOICES = (
    ('Bronze', 'Globalnet Bronze'),
    ('Silver', 'Globalnet Silver'),
    ('Gold', 'Globalnet Gold')
)

COMPANY_CHOICES = (
    ('Robi', 'Robi'),
    ('Airtel', 'Airtel'),
    ('Grameenphone', 'Grameenphone'),
    ('Teletalk', 'Teletalk')
)

class SubscriptionInfo(models.Model):
    plan_type = models.CharField(choices=PLAN_CHOICES, max_length=6, blank=True)
    subscriber = models.ForeignKey('auth.User', related_name='SubscriptionInfo', on_delete=models.CASCADE)
    primary_phone_number = models.CharField(max_length=14, unique=True)
    other_phone_number = models.CharField(max_length=14, blank=True)
    subscription_price = models.FloatField(blank=True, default=0)
    subscribed_company = models.CharField(choices=COMPANY_CHOICES, max_length=14)
    contract_initiated = models.DateTimeField(auto_now_add=True)
    phone_number_owner = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.plan_type == 'Bronze':
            self.subscription_price = 500
        elif self.plan_type == 'Silver':
            self.subscription_price = 750
        elif self.plan_type == 'Gold':
            self.subscription_price = 1500
        super(SubscriptionInfo, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.plan_type:
            self.phone_number_owner = self.subscriber
        else:
            self.phone_number_owner = self.subscribed_company

        super(SubscriptionInfo, self).save(*args, **kwargs)


    # To get a customer's contract remaining days
    def get_contract_remaining_day(self):
        if PLAN_CHOICES[2][0]:
            return "No termination period, you can cancel any time"
        else:
            today = date.today()
            remaining_day = self.contract_initiated.date() - today
            remaining_day_stripped = str(remaining_day).split(",", 1)[0]
            return f"Contact will end after {remaining_day_stripped} days"

        
    # if a subscriber has a paid plan_type subscriber will own the phone number otherwise the company
    @property
    def get_phone_num_owner(self):
        if self.plan_type:
            return self.subscriber
        return self.subscribed_company

    # To get the price per plan, there's three plan in PLAN_CHOICES 
    def get_plan_price_per_month(self):
        if PLAN_CHOICES[0][0]:
            bronze = 500
            return int(bronze)
        elif PLAN_CHOICES[1][0]:
            silver = 750
            return int(silver)
        else:
            gold = 1500
            return int(gold)
    


    # ordering models data based on contract initiated date of a customer
    class Meta:
        ordering = ['contract_initiated']
