import os
print("Setting DJANGO_SETTINGS_MODULE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'workflow.settings')

import django
django.setup()

from users.models import *
from faker import Faker
fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=fakegen.name().split()
        fake_fname=fake_name[0]
        fake_lname=fake_name[1]
        fake_email=fakegen.email()

        user=Users.objects.get_or_create(fname=fake_fname,lname=fake_lname,email=fake_email)[0]


if __name__=='__main__':
    print('populating database')
    populate(20)
    print('complete')