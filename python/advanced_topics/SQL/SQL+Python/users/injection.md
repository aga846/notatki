Podejście w pliku "password.py" jest bardzo złe, bo można łatwo to oszukać (obejść):  
w password wpisując ' OR 1=1--  
Co to zrobi - query da mi pierwszego użytkownika, dlatego że dzięki powyższemu query będzie brzmiało:  
SELECT * FROM users WHERE username='cos' AND password='' OR 1=1  
co oznacza, że to zawsze będzie prawdziwe, czyli da mi wszystkich users.  
Żeby to tak zadziałało, potrzebne mi były dwie kreski - komentarz, bo bez nich byłby problem z ostatnim cudzysłowem (dzięki komentarzowi pierwszy napisany cudzysłów kończy cudzysłów przy password=).  
  
Lepsze podejście jest w pliku "password2.py".  
