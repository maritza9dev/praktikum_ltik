#Maritza Rievani Wibowo - 2602736 
#latihan 1 no 1 - fibonaci
def fibonacci(n):
    deret = [1, 1]
    while len(deret) < n:
        deret.append(deret[-1] + deret[-2])
    return deret[:n]
print(fibonacci(7))    
        
# #latihan 1 no 2 - tabung
def tabung(phi, r, t):
    volume = phi*(r**2)*t
    return volume
print(tabung(3.14,7,10))

#latihan 1 no 3 
def total_rata(*angka):
    total = sum(angka)
    rata = total/len(angka)
    return total, rata
data = input("Masukkan angka (pisahkan dgn spasi): ").split()
angka = [int(x) for x in data]
total, rata = total_rata(*angka)
print(f"total: {total}")
print(f"rata: {rata}")

#latihan 2
def login (password="Latihan", kesempatan=3):
    for i in range(1, kesempatan + 1):
        pw = input(f"Password: ")
        if pw == password:
            print("Login berhasil! Selamat datang, Admin.")
            return
        print("Password salah.")
    print("Kesempatan habis. Keluar dari menu login.")
login()
  
#latihan 3 
def selisih(j1, m1, d1, j2, m2, d2):
    mulai = j1 * 3600 + m1 * 60 + d1
    selesai = j2 * 3600 + m2 * 60 + d2
    s = selesai - mulai
    return s // 3600, (s % 3600) // 60, s % 60

j1 = int(input("Jam Mulai: "))
m1 = int(input("Menit Mulai: "))
d1 = int(input("Detik Mulai: "))
j2 = int(input("Jam Selesai: "))
m2 = int(input("Menit Selesai: "))
d2 = int(input("Detik Selesai: "))

jam, menit, detik = selisih(j1, m1, d1, j2, m2, d2)
print(f"Output: {jam} jam - {menit} menit - {detik} detik")
    
    