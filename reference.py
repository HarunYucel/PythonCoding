
# value types => string, number
# value type da bu sekide y de yapılan değisiklik x degerini etkilemez
x = 5 

y = 25

x = y 

y = 10

print(x,y)

# reference types => list 

a = ["apple","banana"]
b = ["apple","banana"]

a=b

b[0] = "grape"

print(a,b)

# reference typelarda liste uzerinde yapılan değişiklik aynı adresi gösteren 
# iki objede de otomatik olarak değişir 

