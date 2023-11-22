#def powitanie(imie):
 #   return print("Witaj w świecie",imie,"!")

#powitanie("test")

#def MinMax(a, b, c):
   # return max(a, b ,c), min(a, b, c)

#print(MinMax(1, 5, 30))

#def dlugasc_ciagu(ciag):
    #return len(ciag)

#print(dlugasc_ciagu("Python"))#


#def silnia(n):
  #  if n==0:
     #   return 1
  #  else:
     #   return n * silnia(n-1)
#t = silnia(5)
#print(t)

#def dodawanie(a:int, b:int) -> int:
        #return a + b

#print(dodawanie(3,6))

#import requests

#response = requests.get('https://www.google.com')
#print(response.text)

#walidaja adresu email



#def walidacja(email):
 #  if email.count('@')!=1:
  #    raise ValueError("to nie jest adres mailowy,!")
      #podział na username i domene
 #  param = email.split('@')
  # if param[1] == 'pw.edu.pl':
    #  True
   #else:
     # raise ValueError("to nie jest adres mailowy,!")

   #return True

#try:
   #walidacja('wiktor.bilinski@pw.edu.pl')
#except ValueError as e:
     #print(f"komunikat błędu: {e}")

#def walidacja_hasla(haslo):

   #cyfra = any(char.isdigit() for char in haslo)
  # duza_litera = any(char.issuper() for char in haslo)
  # zasieg = len(haslo)>=8
 #  return cyfra and duza_litera and zasieg
#haslo=input("wprowadz haslo: ")

#if walidacja_hasla(haslo):
 #  print("mam silme haslo")



# def valdiate_username(username):
#    zasieg = len(username)> 2 and len(username)<17
#    czy_cyfra = any(char.isdigit() for char in username)
#    czy_litera = any(char.isalpha() for char in username)
#    return zasieg and czy_cyfra and czy_litera

# if valdiate_username("kais231"):
#    print("take")
# else:
#    print("ni ma huhu")





# def validate_ip(ip):
#    param = ip.split('.')
#    pierwszy_oktet = param[0].isnumeric()
#    if len(param[0])!=3:
#       return False
#    drugi_oktet = param[1].isnumeric()
#    if len(param[1])!=3:
#       return False
#    trzeci_oktet = param[2].isnumeric()
#    if len(param[2])!=3:
#       return False
#    czwarty_oktet = param[3].isnumeric()
#    if len(param[3])!=3:
#       return False
#    return pierwszy_oktet and drugi_oktet and trzeci_oktet and czwarty_oktet

# if validate_ip("192.111.123.421"):
#    print('T')
# else:
#    print('N')
# nip="12307705"
# weights = [1, 2, 4, 5, 7, 9, 3, 6, 8]

# if len(nip)!= 10:
#    return False
# if not nip.isdigit():
# return False
# suma = 0
# for i in range(9):
#    suma += int(nipt[i]) * weights[i]

#    if suma%11 != nip[9]
#       return False
#    return True

# if validate_nip('6436123432'):
#    print("nip jest ok")
# else:
#    print("nip jest nieok")
# def validate_nip(nip):
#    weights  = [6,5,7,2,3,4,5,6,7]
# if len(nip) != 10:
#       False
# if nip.isdigit():
#       False
# suma = 0
# for i in range(9):
#    suma += int(nip[i])*weights[i]
# if suma%11 == 10 amd suma %11 != nip[9]:
#       return False
#    return True
# nip ="123456789"
# t=validate_nip(nip)
# print(t)
