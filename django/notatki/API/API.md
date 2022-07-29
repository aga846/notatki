# ViewSet  
## Zmiana queryset  
```
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
```

```
class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    
    def get_queryset(self):
      qs = Film.objects.filter(after_premiere=True)
      return qs
```  
   
Domyślnie queryset zawiera wszystkie pozycje z bazy danych.    
Mogę ustawiać, co zwraca mi queryset za pomocą metody get_queryset().  
  
### Metody list i retrieve  
Są metody np. list i retrieve. Żeby się do nich dostać: przytrzymać ctrl i kliknąć w viewsach ModelViewSet. To przekieruje nas do pliku z kodem, w którym znajduje się klasa ModelViewSet, gdzie są podane różne mixiny. Znowu przytrzymuję ctrl i klikam ListModelMixin. To przekieruje do mixinów, gdzie znajdę klasy konkretnych mixinów, jak m.in. ListModelMixin. Mogę skopiować tę klasę i wkleić do swojej klasy FilmViewSet. Tam mogę zmodyfikować ten kod, tj. zmienić domyślne wylistowanie wszystkich na wylistowanie tylko konkretnych rekordów.  
  
```
def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = FilmSerializer(queryset, many=True)
        return Response(serializer.data)
```
  
Ta metoda (list) dotyczy wylistowania wszystkich rekordów.  
Metoda retrieve dotyczy wyświetlania informacji na temat konkretnego rekordu.  
Mogę np. zrobić nowy serializer FilmMiniSerializer, w którym wyświetlam tylko tytuł. I jako wartość serializer w metodzie list podać ten nowy serializer, ale w retrieve podać normalny FilmSerializer. Wtedy w liście wszystkich rekordów podaje mi tylko tytuł, ale w szczegółach danego rekordu podaje mi wszystkie informacje.  
```
def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = FilmMiniSerializer(queryset, many=True)
        return Response(serializer.data)

def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)
```
  
### Metoda create  
Wchodzę w kod CreateModelMixin, kopiuję go do viewsów i zmieniam na swoje:  
```
def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            film = Film.objects.create(title=request.data['title'],
                                    description=request.data['description'],
                                    after_premiere=request.data['after_premiere'])
            serializer = FilmSerializer(film, many=False)
            return Response(serializer.data)
        return HttpResponseNotAllowed()
```
Na stronie nie będzie działało (bo formularz wysyła boolean z małych), ale na Postmanie tak (z tym że bez ifa sprawdzającego, czy user.is_staff).  
  
### Metoda update  
W Postmanie będzie to metoda PUT.  
```
def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.title = request.data['title']
        film.description = request.data['description']
        film.after_premiere = request.data['after_premiere']
        film.save()
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)
```  
  
### Metoda delete (destroy)  
```
def destroy(self, request, *args, **kwargs):
        film = self.get_object()
        film.delete()
        return Response('Movie deleted')
```
Mogę też nie chcieć, żeby było w ogóle dostępne delete - wtedy tę metodę nadpisuję, dając tylko return np. Response("Not allowed").  
  
### Własne metody  
Np. metoda zmieniająca jakąś wartość z False na True.  
Przed metodą - dekorator action z parametrem detail=True - żeby odnosiła się tylko do jednego rekordu. Wtedy link będzie: /films/3/nazwa_metody.  
```
@action(detail=True)
def premiere(self, request, **kwargs):
    film = self.get_object()
    film.after_premiere = True
    film.save()
    serializer = FilmSerializer(film, many=False)
    return Response(serializer.data)
```  
  
Funkcja, która odnosi się do wszystkich rekordów:  
```
@action(detail=False)
def before_premiere_all(self, request, **kwargs):
    films = Film.objects.all()
    films.update(after_premiere=False)
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)
```
  
Funkcja, która odnosi się do wszystkich rekordów i uzależnia to, co zrobi, od tego, co podamy w POST - zamiast pisania dwóch funkcji, które robią swoją odwrotność (zmiana after_premiere na True/False), mogę napisać jedną, która udostępnia metodę post, i w zależności od tego, co w niej podamy, to będzie robiła:  
```
@action(detail=False, methods=['post'])
def premiere_all(self, request, **kwargs):
    films = Film.objects.all()
    films.update(after_premiere=request.data['after_premiere'])
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)
```
  
# Serializers   
## read_only  
Przy definiowaniu jakiegoś pola, które ma się wyświetlać, poprzez odniesienie do innego serializera - jeśli chcę, żeby tego pola można było nie podawać przy POST, mogę dodać argument read_only=True.  
```
class ActorSerializer(serializers.ModelSerializer):
    films = FilmMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ["first_name", "last_name", "films"]
```
   
## create - tworzenie obiektu innego modelu połączonego z głównym modelem  
Mogę nie chcieć mieć read_only, ale mogę chcieć, żeby w jednym requeście dało się stworzyć obiekty różnych tabel - np. dodając aktora i podając filmy, w których grał, mogę chcieć od razu stworzyć dany film do tabeli Filmy. Do tego muszę to określić w funkcji create dla aktora - w serializerze.  
```
def create(self, validated_data):
        films = validated_data["films"]
        del validated_data["films"]

        actor = Actor.objects.create(**validated_data)

        for film in films:
            f = Film.objects.create(**film)
            actor.films.add(f)

        actor.save()

        return actor
```  
  
## Tworzenie obiektów osobno, potem ich łączenie ze sobą  
Wracam do read_only=True.  
Żeby połączyć aktora z filmem, potrzebuję zdefiniować metody w views.  
```
@action(detail=True, methods=['post'])
    def join_actor_to_film(self, request, **kwargs):
        actor = self.get_object()
        film = Film.objects.get(id=request.data["film"])
        actor.films.add(film)

        serializer = ActorSerializer(actor, many=False)
        return Response(serializer.data)
```
  
## Fieldy w serializerze  
Mogę je wymienić w liście, a jeśli chcę wszystkie, wystarczy "__all__".  
  
## depth  
Mogę określić w serializerze atrybut depth - odnosi się do tego, jak głęboko chcę wyświetlać, tj. jeśli w reviews mam field "film", to bez określenia depth wyświetlam tylko id tego filmu. Jeśli depth ustawię na 1, wyświetlam wszystkie informacje z filmu, ale tylko z pierwszego poziomu, tj. jeśli film ma odniesienie dalej (np. extra_info), to tego fieldu nie będzie widać całego, a samo jego id. Jeśli depth na 2, wtedy całe extra info będzie wyświetlane.
  
## exclude  
Wskazuję, które fieldy chcę wyłączyć (z kolejnego poziomu).  
  
## read_only_fields  
Wskazuję, które fieldy są read_only (nie muszę tego robić w każdym serializatorze).  
  
  
# Gdzie umieszczać metody?  
W modelach - te, które wiążą się z modelem - np. obliczanie czegoś z modelu, sumowanie, robienie danych statystycznych, dawanie dodatkowych informacji, których potem mogę gdzieś użyć.  
W views - te, do których odnoszą się requesty - dodatkowa logika, walidacja. ViewSet - tylko odnośnik do endpointów.  
W serializers - sposób, w jaki układam dane w bazie danych (w jaki sposób chcę wysyłać i odbierać dane).  
  
# Queryset params  
Wyświetlanie za pomocą metody all(), get() lub filter().  
Można dodać też własne filtry - w url wpisać po slashu: ?key=value (np. ?year=2000), a w metodzie:  
```
year = self.request.query_params['year']
films = Film.objects.filter(year=year)
```
Mogę też z domyślną wartością - żeby zapewnić, że jeśli nie zostanie podany w url żaden rok, to nie będzie błędu:   
```
year = self.request.query_params.get('year', None)
films = Film.objects.filter(year=year)
```
A jeśli mimo niepodania roku chcę wyświetlać (wszystkie na przykład), to muszę zrobić ifa (if rok, filtruj po roku, else, wyświetl wszystkie). 
  
Podawanie więcej parametrów - w url: ?key=value&key=value, a w metodzie robię to co wyżej, ale dla kolejnego parametru.  
  
## Filtry Django  
Tak jak w powyższym pisałam przy filter(year=year), tak mogę filtrować bardziej dokładnie: 
- title__contains (wszystkie wyniki zawierające daną frazę),  
- title__icontains (zawierające daną frazę, bez względu na wielkość liter),  
- title__exact (musi być zupełnie taki sam, jak w parametrach),  
- title__iexact (case insensitive - bez względu na wielkość liter),  
- premiera__lte (mniejsza lub taka sama - też odnośnie do daty),  
- premiera__gte (większa lub taka sama),  
- premiera__year=2000 (odnośnik do samego roku przy DateField).  
Więcej - w dokumentacji "Making queries".  
  
## Plugin - filter fields   
Trzeba zainstalować django-filter, dodać django-filters do zainstalowanych aplikacji i utworzyć w settings.py słownik REST_FRAMEWORK (w dokumentacji Django-rest-framework), tj. dodać plugin.  
W FilmViewSet mogę podać listę filter_fields, w której wymieniam fieldy, po których chcę filtrować. Żeby to zadziałało, muszę usunąć własną definicję metody list, zamiast tego korzystać w domyślnej.  
To działa tak samo, jak manualne ustawianie filtrów,, tj. w url mogę wpisać nazwy tych fieldów (wraz z wartościami), które określiłam właśnie w filter_fields.  
  
## Search fields  
Trzeba z rest_framework zimportowac filters. Potem ustawiam (w FilmViewSet) filter_backends = [filter.SearchFilter] oraz podaję w liście search_fields fieldy, po których chcę przeszukiwać, tj. jeśli zamieściłam tam filtry "title" i "description", to jeśli w url wpiszę ?search=Avatar, to przeszuka mi wszystkie tytuły oraz opisy filmów i wyświetli mi te filny, w których tytule lub opisie znajduje się "Avatar". Nie będzie szukać np. w recenzjach.  
W dokumentacji wskazane, w jaki sposób można używać search - ^=@$.  
  
## Porządkowanie (ordering)  
Trzeba w ViewSet ustawić filter_backend = [filters.OrderingFilter] oraz stworzyć listę ordering_fields, w której podaję fieldy, względem których, wedle wyboru w url, będą wyświetlane rekordy. Np. jeśli w url napiszę ?ordering=title, to będą wyświetlone wszystkie rekordy alfabetycznie tytułami. Jeśli year - chronologicznie, itd.  
Można użyć dwóch filtrów, np. ?ordering=year,title - rekordy będą uporządkowane względem roku, ale jeśli będą z tego samego roku, to będą uporządkowane względem tytułu.  
Można też w url dodać minus: ?ordering=-title - wtedy będzie od Z do A.  
Można też ustawić ordering_fields na "__all__".  
Można też wybrać domyślne ordering: ordering = ["year"] - jeśli mam "__all__", mogę w url wpisać ordering=title, to będzie sortowało wg tytułu, ale jeśli nic nie wpiszę, będzie sortowało wg roku.   
  
  
# Paginacja  
Podzielenie response na strony (np. daj mi pierwsze 10 rekordów, jak będę potrzebowała więcej, to Ci powiem).  
  
W settings w słowniku REST_FRAMEWORK (gdzie znajdują się wszystkie ustwienia rest framework) trzeba dodać:  
```
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 3
```
PAGE_SIZE - ile domyślnie rekordów ma być zwracane.  
  
Teraz response nie będzie listą obiektów, tylko jednym obiektem (słownikiem), zawierającym informacje:  
- count - ile ogólnie mam rekordów,  
- next - link do kolejnego request (czyli po to, żeby pokazać kolejne 3 elementy),  
- previous - link do poprzedniego request,  
- results - tutaj znajduje się lista obiektów - tylu obiektów, ile podałam w PAGE_SIZE.  

W url przy next pokazują się też parametry "limit" oraz "offset" - ile rekordów ma wyświetlać oraz od którego zaczynając.  
  
## Paginacja przy każdym modelu  
Powyższe dotyczy wszystkich modeli. Jeśli chcę ustawić inną paginację dla poszczególnych modeli, muszę w views dodać:  
```
from rest_framework.pagination import PageNumberPagination 

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3
```
następnie w konkretnym ViewSet dodaję pagination_class, ustawiając na (w tym przykładzie) LargeResultsSetPagination (tę klasę mogę nazwać dowolnie).  
Teraz, przy wyświetleniu, zmieni się link do next - nie będzie offset, tylko page=2.
