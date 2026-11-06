tabung = []
while True:
    uang = int(input("masukan jumlah uang: "))
    if uang == 0:
        break
    tabung.append(uang)
# fungsi
def hitung_total(tabung):
    total = sum(tabung)
    return total #kalau tidak di return hasil nya none

#prosedur
def cetak_rincian(tabung):
    print(f"=== Rincian Tabungan ===")
    print(f"riwayat nabung: {tabung}")
    print(f"total celengan: {hitung_total(tabung)}")
    
cetak_rincian(tabung)