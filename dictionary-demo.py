'''
ogrenciler = {
'120':{
'ad':'Ali',
'soyad':'Yılmaz',
'telefon': '0532 000 00 01'

},
'125':{
'ad':'Ali',
'soyad':'Yılmaz',
'telefon': '0532 000 00 02'

},
'128':{
'ad':'Ali',
'soyad':'Yılmaz',
'telefon': '0532 000 00 03'

},


}

1- bilgileri verilen ogrencileri kullanıcıdan aldıgınız bilgilerle 
dictionary icinde saklayınız

2-ogrenci numarasını kullanıcıdan alıp ilgili ogrenci bilgisini gösterin
'''

ogrenciler  = {}

number  = input("öğrenci no: ")
name    = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone   = input("öğrenci telefon: ")

'''ogrenciler[number]= {
    'ad': name,
    'soyad':surname,
    'telefon': phone
} '''

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone

    }

})


number  = input("öğrenci no: ")
name    = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone   = input("öğrenci telefon: ")

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone

    }

})



number  = input("öğrenci no: ")
name    = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone   = input("öğrenci telefon: ")

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone

    }

})



number  = input("öğrenci no: ")
name    = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone   = input("öğrenci telefon: ")

ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone

    }

})

#print(ogrenciler)
print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]

#print(ogrenci)

print(f'Aradığınız {ogrNo} nolu öğrencinin adı:{ogrenci["ad"]} soyadı : {ogrenci["soyad"]} ve telefonu ise {ogrenci["telefon"]}   ')