from django.db import models
from datetime import datetime


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.price}: {self.release_date}'

    def create(self, phone_d):
        self.id = phone_d['id']
        self.name = phone_d['name']
        self.image = phone_d['image']
        self.price = float(phone_d['price'])
        self.release_date = datetime.strptime(phone_d['release_date'], '%Y-%m-%d')
        self.lte_exists = bool(phone_d['lte_exists'])
        self.slug = phone_d['name']
