#---------------------dictionary-------------------------

"""def times_ten(start_index:int,end_index:int):
    dictionary={}
    for i in range(start_index,end_index+1):
        dictionary[i]=i*10
    return dictionary
d = times_ten(3, 6)
print(d)"""

#--------------------------------------------------
"""
def factorials(n:int):
    dictionary={}
    faktor=1
    for i in range(1,n+1):
        faktor *=i
        dictionary[i]=faktor
    return dictionary
k = factorials(5)
print(k[1])
print(k[3])
print(k[5])"""

#-----------------------------------------------------


"""def histogram(strings:str):
    dictionary={}
    for harf in strings:
        if harf   in dictionary:# eğer harf sözlükte varsa sayısını bir artırıyoruz 
            dictionary[harf]+=1
        else:
            dictionary[harf]=1 # sözlükte yoksa sayısı 1 olarak kalıyor 
        
        
    for harf in dictionary.keys():# harf sayısıs kdr yıldız koyma
        print(f"{harf} {'*'* dictionary[harf]}")


#histogram("abba")
histogram("statistically")"""

#---------------------------------------------------------

def invert(dictionary:dict):
    sozluk={}
    for key,value in dictionary.items():
        sozluk[value]=key
    dictionary.clear()
    dictionary.update(sozluk)
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)

