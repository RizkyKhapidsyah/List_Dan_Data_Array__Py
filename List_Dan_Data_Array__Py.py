# Source        : Kelas Terbuka
# Modified by   : Rizky Khapidsyah

# PENTING: Dimanapun, ARRAY DIMULAI DARI 0, sama seperti mbak-mbak SPBU yang mengisi belahan jiwa Anda yang DIMULAI DARI 0 
# *lol

Data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4069]    #Contoh Data dalam bentuk array, yang mencakup Integer
                                                        
# Array ke 
# 0  = 1
# 1  = 2
# 2  = 4
# 3  = 8
# 4  = 16
# 5  = 32
# 6  = 64
# 7  = 128
# 8  = 256
# 9  = 512
# 10 = 1024
# 11 = 2048
# 12 = 4069

print("Data =", Data, "\n\n")

# Mengakses Data dari Array dari Kiri
print("-----------------------------------------------------")
print("Mengakses Data dari Array dari Kiri")
print("-----------------------------------------------------")
BagianData1 = Data[0]
BagianData2 = Data[1]
BagianData3 = Data[2]
BagianData4 = Data[3]
BagianData5 = Data[4]
BagianData6 = Data[5]
BagianData7 = Data[6]
BagianData8 = Data[7]
BagianData9 = Data[8]
BagianData10 = Data[9]
BagianData11 = Data[10]
BagianData12 = Data[11]
BagianData13 = Data[12]
print(BagianData7, "\n\n")                                          # Contoh Menampilkan Data di array 6, lihat list, array 6 berisi nilai 64

# Mengakses Data dari Array dari Kanan
print("-----------------------------------------------------")
print("Mengakses Data dari Array dari Kanan")
print("-----------------------------------------------------")
BagianData14 = Data[-1]                                             # Mengakses data dari kanan menggunakan tanda minus '-' dan dimulai dari 1
BagianData15 = Data[-2]
print(BagianData14)                                                 # Menampilkan data paling kanan
print(BagianData15, "\n\n")                                         # Menampilkan data urutan ke-dua dari kanan

# Mengoperasikan Data Menggunakan Array
print("-----------------------------------------------------")
print("Mengoperasikan Data Menggunakan Array")
print("-----------------------------------------------------")
print(BagianData5 + BagianData10)                                   # Menampilkan hasil penghitungan pada Data dengan array ke 4 (16) ditambah dengan data dengan array ke 9 (512)
print(Data[0:6])                                                    # Menampilkan array yang berisi data yang dimulai dari array 0 sampai 
print(Data[-4:])                                                    # Menampilkan data yang dimulai dari array ke 3 dari kanan
print(Data[:-4])                                                    # Menampilkan data yang dimulai dari array ke 0 sampai ke 8 dari kiri
print(Data[4:])                                                     # Menampilkan data yang dimulai dari array ke 4 sampai array terakhir dari kiri
print(Data[:4], "\n\n")                                             # Menampilkan data yang dimulai dari array ke 0 sampai array ke 3 dari kiri

# Merubah konten isi list dengan menggunakan metode SLICING
print("---------------------------------------------------------")
print("Merubah konten isi list dengan menggunakan metode SLICING")
print("---------------------------------------------------------")
Data[3:5] = [11, 12]                                                # Merubah isi data pada array ke 3 dan 4 dengan nilai '11' dan '12' 
print(Data, "\n\n")

# Menambah isi data dengan data yang baru (Data1)
print("---------------------------------------------------------")
print("Menambah isi data dengan data yang baru (Data1)")
print("---------------------------------------------------------")
Data1 = [10, 20, 30, 40, 50, 60, 70]
print(Data + Data1, "\n\n")

# List di dalam List
print("---------------------------------------------------------")
print("List di dalam List")
print("---------------------------------------------------------")
R = [Data, Data1]
print(R, "\n\n")

# Mengakses list dalam multidimensional list
print("---------------------------------------------------------")
print("Mengakses list dalam multidimensional list")
print("---------------------------------------------------------")
Q = R[1][4]
print(R)
print(Q, "\n\n")

# Method untuk list
print("---------------------------------------------------------")
print("Method untuk list")
print("---------------------------------------------------------")
Data.append(44)                                                     # Menambahkan data ke dalam list, yang diletakkan di akhir
print(Data, "\n\n")

# Function yang bisa digunakan pada list, contoh:
print("---------------------------------------------------------")
print("Function yang bisa digunakan pada list")
print("---------------------------------------------------------")
Panjang_List = len(Data)
print("Data :", Data)
print("Jumlah =", Panjang_List, "data\n\n")

# Mengganti/Merubah isi Data
print("---------------------------------------------------------")
print("Mengganti/Merubah isi Data")
print("---------------------------------------------------------")
Data[5] = 12345678                                                  # Mengganti isi data pada array ke 5 (urutan 6) dengan nilai yang ingin diisi (contoh: 12345678)
print(Data, "\n\n")

# Mengcopy list ke variabel baru, yaitu variabel a 
print("---------------------------------------------------------")
print("Mengcopy list ke variabel baru, yaitu variabel a ")
print("---------------------------------------------------------")
a = Data[:]
a[5] = 1000
print(Data)
print(a, "\n\n")






