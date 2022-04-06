# O co chodzi z population  
Population to zapełnienie modeli z przykładowymi danymi. Do tego celu można użyć biblioteki Faker, która stworzy skrypt.  
  
Najpierw trzeba zainstalować Faker (pip install Faker).  
Dokumentacja Fakera: https://faker.readthedocs.io/en/master/  
  
Używa się tego w następujący sposób:  
```
from faker import Faker
fake = Faker()

fake.name()
fake.adress()
fake.text() 
```  
czyli tworzy się obiekt klasy Faker i do tego obiektu stosuje różne metody z tej klasy, tworzące przykładowe dane.  
  
W głównym folderze projektu tworzy się plik (np. populate_first_app.py). W tym pliku:  
```
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
```
Druga linijka konfiguruje ustawienia dla projektu. Trzeba to zrobić przed manipulowaniem poszczególnymi modelami.  
Następnie importuję django i stosuje setup(), które stworzy i skonfiguruje ustawienia projektu.  
```
import django 
django.setup()
```
  
Teraz tworzę skrypt tworzący przykładowe dane:  
importuję random,  
importuję modele z pliku models,  
importuję klasę Faker z modułu faker,  
tworzę obiekt klasy Faker,  
tworzę listę obiektów mojej klasy (np. w klasie Topic będą następujące tematy stron: Search, Social, Marketplace, News, Games):  
```
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]  
```  
teraz tworzę metodę, która rzeczywiście będzie dodawała topics:  
```
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
```  
object.get_or_create weźmie istniejący lub stworzy topic, z dostarczonego mu randomowego wyboru z listy topics i ten topic przypisze do kolumny top_name.  
Topic.objects to po prostu odwołanie się do obiektów klasy Topic.  
t.save() zapisuje zmiany.
Zwracamy t, a t jest obiektem klasy Topic od indeksu 0, tj. obiekt klasy Topic składa się z Primary Key oraz z top_name (Primary Key oraz top_name to nazwy KOLUMN), więc t[0] będzie równy Primary Key danego obiektu.  
  
Dalej dodaję funkcję, która rzeczywiście produkuje przykładowe (fake) dane i wywołuję ją na samym końcu pliku:  
```
def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("populating scirpt!")
    populate(20)
    print("Populating complete!")
```  
W funkcji populate robię pętlę, która powtórzy się tyle razy, ile podam przy wywołaniu tej funkcji (w przykładzie: 20). Pętla będzie:
1. tworzyła obiekt klasy Topic poprzez wywołanie funkcji add_topic i przypisanie do jej wyniku zmiennej top;  
2. tworzyła url, date i nazwę (tu: nazwę firmy),  
3. tworzyła obiekt klasy Webpage - tak jak stworzyliśmy obiekt klasy Topic, ale za topic podstawia Primary Key obiektu klasy Topic,  
4. tworzyła obiekt klasy AccessRecord, podobnie jak wyżej - za name podstawia Primary Key obiektu klasy WebPage.
