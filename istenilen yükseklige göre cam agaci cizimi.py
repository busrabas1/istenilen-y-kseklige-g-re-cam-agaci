a=int(input("ağacın yüksekliğini yazınız"))
b=a
for i in range (1,a+1):
    print(b*" ", (2*i-1)*"*")
    b-=1
