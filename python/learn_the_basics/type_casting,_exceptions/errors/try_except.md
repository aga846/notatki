# Do czego służy blok try/except  
Dzięki try/except możemy poradzić sobie z błędami - przewidywać, co może pójść źle i zapewniać, że wyświetli się to, co przewidzieliśmy, a nie wywali cały program.  
  
## Try i except  
```
def get(d, key):
    try:
        return[key]
    except KeyError:
        return None
```
W powyższym przykładzie, jeśli danego key nie będzie w słowniku d, zwróci None i program nie przestanie działać (co by się stało, gdybyśmy nie przewidzieli tego  błędu).    
  
## Try, except, else, finally  
Składnia:   
```
try:
    num = int(input("enter a number: "))
except ValueError:
    print("you were supposed to enter a number")
else:
    print("I'm in the else")
finally:
    print("Runs no matter what")
```
Najpierw program spróbuje tego, co jest w try.  
Jeśli wyskoczy ValueError - wyświetli to, co jest w except oraz to, co jest w finally.  
Jeśli nie wyskoczy ValueError - wyświetli else i finally.  
  
Po "else" można dać break (jeśli całość jest w pętli while).   
   
```
x = 0

while x < 3:
    x += 1
    try:
        num = int(input("enter a number: "))
    except ValueError:
        print("you were supposed to enter a number")
    else:
        print("I'm in the else")
        break
    finally:
        print("Runs no matter what")
```
W powyższym przykładzie pętla przejdzie maksymalnie 3 razy. Jeśli podamy liczbę, zatrzyma się (bo w else jest break), natomiast jeśli 3 razy podamy np. stringa, którego nie da zamienić się na integera, program po prostu się skończy.  
Jeśli chcemy pytać do skutku, trzeba po prostu zrobić pętlę while True, bez zmiennej x.  
  

Może być wiele "except", ale także w jednym "except" może być kilka błędów podanych jako krotka.
