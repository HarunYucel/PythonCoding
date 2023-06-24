website= "http://www.sadikturan.com"
course = "Pyton Kursu: bastan Sona Python Programlama Rehberiniz (40 saat)"

# 'course' karakter dizisinde kac karakter bulunmaktadır
result = len(course)

# 'website' icinden ww karakterlerini alın 

result = website[7:10] 

# website icinden com karakterlerini alım 
lengt = len(website)
result = website[lengt-3:lengt]

# 'course' icinden ilk 15 ve son 15 karakterlerini alın 

result = course[:15]
result = course[-15:]

# 'course' ifadesindeki karakterleri tersten yazdırın 
result = course[::-1] # bu şekide sondan basa dogru birer birer index gelir 

s = '12345'*5
print(s)
print(s[::5]) # bu sekilde 5. indexte bir alır yani '1' i 5 kere almıs olur

name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis'

# Yukarıda verilen değiskenler ile ekrana asagıdaki ifadeyi yazdırın 
# 'Benim adım Bora Yılmaz, Yasım 32 ve mesleyim mühendis.'

result= "Benim adım " + name + " "+surname+ ", Yaşım "+ str(age) +" ve mesleğim"+job  
result = 'Benim adım {0} {1}, Yasım {2} ve mesleyim {3}.'.format(name,surname,age,job)
result = f'Benim adım {name} {surname}, Yasım {age} ve mesleyim {job}.'

# ' Hello world' ifadesimdeki w harfini 'W' ile degistirin 

s= 'Hello world'
s= s[0:6]+ 'W'+s[-4:]
print(s)

# 'abc ifadesini yanyana 3 defa yazdırın'
  
result= 'abc '*3
print(result)




print(result)