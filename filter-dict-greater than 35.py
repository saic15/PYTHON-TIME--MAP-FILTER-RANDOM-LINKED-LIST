a={'st1':40,'st2':50,'st3':55,'st4':35}
b=filter(lambda x:(x[1]>35),a.items())
print(dict(b))