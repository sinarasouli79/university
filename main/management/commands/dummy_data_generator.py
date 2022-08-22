from django.core.management.base import BaseCommand
from main.models import Instructor
from faker import Faker
from random import randint


class Command(BaseCommand):
    help = 'create dummy data for the app to test'

    # def facker_person_name(self, )
    
    def handle(self, *arg, **options):

        fake = Faker(['fa-IR'])

        for i in range(100):
            Instructor.objects.create(first_name=fake.first_name(
            ), last_name=fake.last_name())
