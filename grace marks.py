a={'x':55,'y':60}
b=dict(map(lambda x:(x[0],(x[1]//10)+x[1]),a.items()))
print(b)