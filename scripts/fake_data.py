import django
from django.contrib.auth.models import User
from faker import Faker
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

django.setup()


def user_set():
    fake = Faker(['en_US'])

    first_name = fake.first_name()
    last_name = fake.last_name()
    user_name = f"{first_name.lower()}_{last_name.lower()}"
    email = f"{user_name}@{fake.domain_name()}"

    print(first_name, email)

    user_check = User.objects.filter(username=user_name)
    while user_check.exists():
        user_name = user_name + str(random.randrange(1, 999))
        user_check = User.objects.filter(username=user_name)

    user = User(
        username=user_name,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=fake.boolen(chance_of_getting_true=25),
    )
    user.set_password('123456.Ys')
    user.save()
    print('User is recorded', user_name)
