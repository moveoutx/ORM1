import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for phone in phone_reader:
                r_phone = Phone(id=phone[0],
                                name=phone[1],
                                image=phone[2],
                                price=float(phone[3]),
                                release_date=datetime.strptime(phone[4], '%Y-%m-%d'),
                                lte_exists=bool(phone[5]))

                r_phone.save()
