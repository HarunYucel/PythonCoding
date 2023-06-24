# key - value 
# 41 kocaeli => kocaeli 34 => istanbul  

sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])

#print(plakalar['kocaeli'])=> 41 
#print(plakalar['istanbul'])=> 34   yapmak istediğimiz böyle bir sonuc almak 
    
'''plakalar = {'key':'value'}
plakalar = {'kocaeli': 41, 'istanbul': 34}

print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara']=6     # listede olmayan bir eleman yazılırsa listeye 
                         # key-value olarak ekleme yapar  
                           
plakalar['kocaeli']='new value' # var olan elemana karsılık olarak da 
                                # güncelleme yapılabilir 

print(plakalar)'''

users ={'harunyucel': {
            'age':32,
            'email':'harun@gmail.com',
            'address': 'kocaeli',
            'phone' : '1231321'
},
        'cinarturan': {
            'age':2,
            'roles': ['admin','user'],
            'email':'cinar@gmail.com',
            'address': 'kocaeli',
            'phone' : '1231321'
        }
         }

print(users['cinarturan'])
print(users['cinarturan']['age'])
print(users['cinarturan']['email'])
print(users['cinarturan']['address'])
print(users['cinarturan']['roles'])
print(users['cinarturan']['roles'][0])