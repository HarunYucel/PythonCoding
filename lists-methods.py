numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val=min(numbers)
val=max(numbers)
val=max(letters)
val=min(letters)

val=numbers[3:6]
val=numbers[:3]
val=numbers[4:]

numbers[4]=40

numbers.append('49')   # bu method sona eleman ekleme yapar 
numbers.append(59)

numbers.insert(3,78)     # bu method istedğimiz konuma eleman ekler       
numbers.insert(-1,52)    # bulunduğu konumda bulunan elemanı sağa kaydırır.   


numbers.pop()       # bu şekide sonda bulunan elamanı siler 
numbers.pop(0)      # bu şekilde de isteğimiz elemanı siler  
numbers.pop(-1)
numbers.remove(59)  # bu method belirttiğimiz elemanı bulur ve siler  

numbers.sort() # listeler sayısal ve alfabetik olarak sıralanır 
letters.sort()

numbers.reverse() # bu şekilde liste tam tersi olarak sıralanır


print(numbers.count(10))   # bu methodda bu elemandan listede kaç tane olduğu
print(letters.count('a'))  # saydırılır

print(numbers.clear) # bu şekilde liste tamamen silinir 

print(numbers)
print(val)

