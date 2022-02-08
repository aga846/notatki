Kolejność podawania argumentów jest ważna.

```
def full_name(first, last)
full_name("Damian", "Jaskolski") != full_name("Jaskolski", "Damian")
```

Można podawać w innej kolejności, jeśli podaje się nazwę parametru:  

```
def full_name(first, last)
full_name("Damian", "Jaskolski") = full_name(last="Jaskolski", first="Damian")
```
