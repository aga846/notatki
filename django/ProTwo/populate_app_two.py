import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django 
django.setup()

from app_two.models import User
from faker import Faker

fakegen = Faker()

def populate(n=5):
    for i in range(n):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.ascii_email()
        
        u = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email = fake_email)
    
if __name__ == "__main__":
    populate(20)
