a=[23,90,80,70,60,40]
b=filter(lambda x:x>50,list(map(lambda x:x+5,a)))
print(list(b))