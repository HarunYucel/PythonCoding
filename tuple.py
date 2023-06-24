
list=[1,2,3]
tuple=(1,'iki',3)
print(type(list))
print(type(tuple))

'''print (list[2])
print(tuple[2])

print(len(tuple))
print(len(list))'''

list = ['ali','veli']
tuple=('damla','ayşe','ayşe')


list[0] = 'ahmet'
# tuple[0]= 'deniz'   # eleman atandıktan sonra tek bir atama yapılamaz 


print(tuple.count('ayşe'))
print(tuple.index('ayşe')) #ilk bulunduğu indexi döndürür

names = ('demet','emel','ayşe') + tuple

print(names)



print(list)
print(tuple)

# list ve tuple arasındaki fark tuple da herhangi bir eleman işlemi uzerinde  
# güncelleme silme ekleme işlemi yapılamaz fakat liste olarak birlestirme 
# yapılabilir 

