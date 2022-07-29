Kiedy tworzę użytkownika, nie tworzy się dla niego automatycznie token.  
  
## Przekazywania hasła przy tworzeniu usera    
W serializerze User do fields dodaję "password". Potem tworzę:  
```
extra_kwargs = {"password": {"required": True, "write_only": True}}
```
Czyli w fieldach jest password, jest ustawione jako wymagane, ale jedynie do pisania (tylko przy metodzie POST), czyli nie wyświetli się przy pokazywaniu wszystkich userów. W ten sposób password będzie przekazywany przy POŚCIE.  
  
Password musi zostać zhashowany. Robię nową metodę w tym serializerze:  
```
def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user 
```

## Tworzenie tokena  
Można w metodzie create od razu tworzyć token albo w bardziej skomplikowany sposób. W models:  
```
from django.dispatch import receiver 
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
      if created:
          Token.objects.create(user=instance)
```

Czyli receiver zadziała, jak zasave'ujemy użytkownika - zostanie aktywowany po tym, jak powyższa metoda create zostanie wyegzekwowana. 
