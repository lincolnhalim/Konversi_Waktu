# HH : Hours, 2 digits, range: 00 - 99

# MM : Minutes, 2 digits, range: 00 - 59

# SS : Seconds, 2 digits, range: 00 - 59

# Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

# def timeConverter(seconds):
#       .....
 
# Masukkan detik : 3600
# Konversi : 01:00:00

# Masukkan detik : 3665
# Konversi : 01:01:05

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





# # Function Initialization
#  def counterClockwise(...):
#      .....
     
# # Use the Function
# print(counterClockwise(List_awal))

# X = [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]


# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

# for r in result:
#    print(r)


# Mengurai dan Merajut Kata


# def urai(y):
#     for i in range(len(y)):
#         for j in range(i+1):
#             k += y[j]
#             k += ""
#         k += ""
#         return k
# def rajut(y):
#     a = [1]
#     b = 1
#     for i in range(2, len(y)):
#         b += i
#         a.append(b)
#     c = a.index(len(y))+1
#     c *= -1
#     l = y[c: len(y)]
#     return l 

# urai("saaaa")


# limit = "code"
# for baris in range(1, len(limit)+1):
#     for angka in range(baris+1):
#         print(angka, end = '')
    