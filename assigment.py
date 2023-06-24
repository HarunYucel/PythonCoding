#x= 5 
#y= 10 
#z= 20 

x, y, z = 5, 10, 20 

#x, y = y, x

x+= 5   # x = x+5
x-= 5   # x = x-5   
x*= 5   # x = x*5   
x/= 5   # x = x/5
x%= 5   # x = x%5 bölümden kalan  
y//= 5  # y = y//5 bölümden kalan tamsayi kısmını alır 
y**= 5  # y = y**5 y nin degerini 5 defa yanyana carpar



values = 1, 2, 3
#values = 1, 2  #  fakat bu sekilde atama yapamayız 2 deger 3 degere atanamaz 
#values = 1, 2, 3, 4, 5 b usekilde de fazla olduğu hatası verir  

x, y, *z = values # bu sekilde x=1 y=2 z=[3,4,5] seklinde atama olur 
                  # yani 1 2[3,4,5] ekrana boyle yazdırır   

x, y, z = values  # bu sekilde atama yapabiliriz 

print(x,y,z)
print(x, y, z)
print(x, y, z[0]) # z nin indexlerini özel olarak yazdırırız 

print(values)
print(type(values)) # typenı yazdırıyoruz ve tuple listesi tipinde oldugunu görürüz


 








