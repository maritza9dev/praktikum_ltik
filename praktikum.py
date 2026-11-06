# arbitary argument dipakai ketika tidak mengetahui ada berapa argumen pakai *
def funcArgs(*angka):
    print(f"angka terakhir yang dimasukkan yaitu: {angka}") #bisa pakai slicing misal [:]
funcArgs(1) #akan menjadi tuple

# arbitary keyword argument pakai **
def pengurangan(**angka):
    print(f"nilai yang diinputkan adalah {angka["pertama"]}")
pengurangan