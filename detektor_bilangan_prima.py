print ("\n\n==========PRIMA CHECKER==========")
print ("^^detektor bilangan prima^^")
x = int(input("\nMasukkan bilangan yang mau diteliti  :  "))
start_time = float(time.time())
tampung = 0
for i in range (1,x + 1):
    operasi = x % i
    if operasi == 0 :
        tampung += 1

faktor_prima = 2

if tampung == faktor_prima :
    print("\n===Bilangan tersebut adalah bilangan prima===")
else :
    print("\n++Bilangan tersebut bukan bilangan prima++")
print ("\n\nLamanya komputer kamu merespon : ", float(time.time() - start_time) ," detik " )
