
def convert(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60
   return "%02d:%02d:%02d" % (hour, min, sec) 


try:

    detik = int(input("masukkan detik: "))
    if detik > 359999:
        print("angka diluar jangkauan")
    elif detik < 0:
        print("hanya menerima angka bulat")
    else:
        print("Konversi:", convert(detik))

except:
    print("input yang anda masukkan salah")
    
