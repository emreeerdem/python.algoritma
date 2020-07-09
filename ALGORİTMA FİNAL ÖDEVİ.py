#soru1
#Benım öğrenici numaram 03 olduğu için çalıştırırken kodu hata aldım ben de o yüzden 2 ve 50 arasında ki asal sayıları gösterdim
for i in range(2,50):
    emre = False
    for j in range(2, i):
            if (i % j) is 0:
                emre=True
    if emre is False:
        print (i)




#Soru 3
isim=[[5,13,18],
   [5,5,18],
   [4,5,13]]

for i in range(3):
   print(isim[i])
A=[[1,2,-1],
    [2,5,2],
    [-1,-2,2]]
print()
for i in range(3):
   print(A[i])
print()



# 3x1 matrix
E = [[5,13 ,18]]
M = [[5,5,18]]
R = [[4 ,5,13]]

# 3x3 matrix
A= [[1,2,-1],
    [2,5,2],
    [-1,-2 ,2,]]


result1 = [[sum(a*b for a,b in zip(E_row,A_col)) for A_col in zip(*A)] for E_row in E]
result2 = [[sum(a*b for a,b in zip(M_row,A_col)) for A_col in zip(*A)] for M_row in M]
result3 = [[sum(a*b for a,b in zip(R_row,A_col)) for A_col in zip(*A)] for R_row in R]

for r in result1:
   print(r)
for r in result2:
   print(r)
for r in result3:
   print(r)



#Soru 4
from datetime import datetime

e = gün = int(input('Günü giriniz : '))
m = ay = input('Ayı giriniz : ')
r = yıl = int(input('Yılı giriniz : '))
e = date1 = datetime.date(gün , ay , yıl)
print("datetime.date(gün, ay, yıl)")



