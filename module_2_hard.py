n = int(input("Введите число от 3 до 20: "))
def shifr (n):
    parol = ''
    for i in range (1,n):
        for j in range (2,n):
         if j<=i:
               continue
         if n% (i+j)==0:
            parol += str(i)+str(j)
    return parol


result = shifr (n)
print ('Пароль: ', result)



