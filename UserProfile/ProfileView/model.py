from django.db import models
from django.db.models import CheckConstraint, Q, F

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    nid_number = models.CharField(max_length=10, unique=True)
    tax_id = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(max_length=20, unique=True)
    occupation = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, blank=True)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)
    CheckConstraint(condition=Q(age__gte=18), name='%(app_label)s_%(class)s_is_adult')
    