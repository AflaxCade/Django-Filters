from django.core.management.base import BaseCommand
from  people.models import Person
from datetime import datetime
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with fake Person data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        sex_choices = ["Male", "Female"]

        # Set the start and end dates for the created_at field
        # start_date = datetime.strptime('2022-01-01', '%Y-%m-%d').date()
        # end_date = datetime.strptime('2022-08-31', '%Y-%m-%d').date()

        for _ in range(100):
            Person.objects.create(
                name=fake.name(),
                age=random.randint(18, 80),
                sex=random.choice(sex_choices),
                created_at=fake.date_this_year()
                #created_at=fake.date_between(start_date=start_date, end_date=end_date)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake people'))
