fruits = {'orange','apple','banana'}

#print(fruits)
#print(fruits[0]) bu sekilde indexlenemez 

for x in fruits:
    print(x)

fruits.add('chery')
fruits.update(['mango','grape','apple']) # zaten var olan eleman olursa tekrar tanımlanmaz    

print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)  # bu sekide direk yazdırma yapılır  
print(set(myList)) # set olarak cevrilirse tekrarlanan elemanlar yazdırılmaz listeden gider 

fruits.remove('mango')
fruits.discard('apple')
fruits.clear() # bu methodla bütün elemanlar silinir 

fruits.pop() # bu method setlerde kullanılmaz cunku indexe baglı olarak son elamanı siler
             # set lerde index olmadıgı icin ve sırlanmadığı icin rasgele silme islemi yapar   


