Labels to etykiety do okienek na input (podpowiedzi, co mamy wpisać w danym okienku). Labels muszą być powiązane z konkretnym inputem, dlatego w inpucie, z którym wiążę dany label, dodaję atrybut id, którego wartość potem wpisuję jako wartość dla atrybutu for, który tworzę dla label:  
  
```
<form action="/tacos">
  <label for="username">Enter your username</label>
  <input id="username" type="text" placeholder="username">
```
  
Samo klinkięcie na label przekierowuje kursor (nie kursor myszki, tylko kursor pisania) do inputu, z którym jest powiązany.  
  
Możliwe jest też zagnieżdżenie inputu w labelu, ale jest to mniej powszechne podejście:  
```
<label>
  Enter a Username:
  <input type="text" placeholder="username">
</label>
```
