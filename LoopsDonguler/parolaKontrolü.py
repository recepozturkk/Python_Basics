while True:
    password = input("Lütfen parola giriniz: ")
    if(len(password)<3 or len(password) > 8 or len(password) == None):
        print("Parolanız 8 karakterden uzun ve 3 karakterden kısa olmamalı!")
    else:
        print("Parolanız başarıyla oluşturuldu.")
        break