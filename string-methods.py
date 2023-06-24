message= 'Hello There. My name is Sadık Turan'

#message= message.upper()
#message= message.lower()
#message= message.title()
#message= message.capitalize()

#message = message.strip()  
#message= message.split()
# message = message.split('.')
# message = ' '.join(message) 
# message = ''.join(message)
# message = '---'.join(message)
# message = '*'.join(message) 
 

index = message.find('Sadık')
isFound = message.startswith('H')
isFound=message.endswith('H')

message = message.replace('Sadık','Çınar')
message= message.replace(' ','*')
message = message.replace('ç','c').replace('ö','o').replace(' ','-')

message = message.center(100)
message = message.center(50,'*')


#print(message[2])
print(message)
print(isFound)