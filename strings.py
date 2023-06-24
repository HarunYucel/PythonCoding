name = 'Sadik'
surname='Turan'

age=36

print('My name is '+ name+' '+surname+ ' and \n I am'+ str(age) + ' years old. ' )

greeting= 'My name is '+ name+' '+surname+ ' and \n I am'+ str(age) + ' years old. '

length = len(greeting)      # str lerde index olarak bakılır 
print(greeting)             # son index len olarak alınır 
print(greeting[0])
print(greeting[3])
print(greeting[length-1])
# print(greeting[-1]) direk sekilde son indexe ulasabilirim  

print(greeting[3:7])
print(greeting[3:])
print(greeting[:16])
print(greeting[2:40:2]) # bu sekide baslangıctan bitise dogru ikiser olarak gider

