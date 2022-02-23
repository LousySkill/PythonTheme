n=int(input("Сколько необходимо билетов?"))
L=[]
x=1
for c in range(1, n+1):
    age=int(input(f"Введите возраст посетителя {x}:"))
    x+=1
    if age<18:
        price=0
    elif 18<age<25:
        price=990
    elif age>25:
        price=1390
    L.append(price)
print(L)
if n>3:
    a=int(sum(L)-sum(L)/10)
    print("Покупка на сумму",a)
else:
    a=sum(L)
    print("Покупка на сумму",a)
print(L)
