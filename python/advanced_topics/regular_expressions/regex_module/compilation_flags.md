# Compilation flags  
Można je dodać jako argument funkcji compile(), zaraz po regexie.  
Jeśli dodajemy kilka flag, nie można dać ich po przecinku ani w krotce; należy użyć znaku OR, czyli kreski |. Ale wbrew pozorom, nie oznacza to, że python przeczyta "ta flaga LUB ta flaga", ale zastosuje je obie.      
```
re.compile(r"[a-zA-Z]", re.VERBOSE)
re.compile(r"[a-zA-Z]", re.VERBOSE | re.IGNORECASE)
```
  
## Verbose  
Pozwala na napisanie regexa w sposób, który wygląda schludniej - pozwala robić entery i dodawać komenatrze, np. oba poniższe przykłady zrobią dokładnie to samo, tyle że ten drugi jest łatwiejszy do przeczytania:   
```
re.compile(r"^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$")

re.compile(r"""
  ^([a-z0-9_\.-]+)  # first part of email
  @                 # sigle @ sign
  ([0-9a-z\.-]+)    # email provider
  \.                # single dot
  ([a-z\.]{2,6})$   # com, org, net, etc.
""", re.VERBOSE)
```
Verbose nie robi nic z samym regexem, chodzi tu tylko o schludność.  
Bez dodania "re.VERBOSE" jako drugi argument, drugi przykład byłby odczytywany tak, że python oczekiwałby również enterów, tabów itd.  
  
Zamiast re.VERBOSE można napisać skrót - re.X (od extended).  
  
  
## Ignorecase  
Dzięki ignorecase regex będzie pasował do stringów bez względu na wielkość liter, tj. gdybym w powyższym przykładzie dodała flagę ignorecase, to również "ThomaS123@Yahoo.com" by pasowało. Bez dodania tej flagi nie zostałoby znalezione.  
  
Skrótem jest re.I.
