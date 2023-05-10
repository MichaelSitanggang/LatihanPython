# A
kata = input("")
huruf = ''
for i in range(len(kata)):
    if kata[i] not in kata[i+1:] and kata[i] not in kata[:i]:
        huruf = kata[i]
        break
if huruf == '':
    print("-1")
else:
    print(f"{kata.index(huruf)+1}")
print()
#Kompleksitas waktu = O(n)
#Algoritama
'''
1. Mulai
2. Input kata 
3. 
4. Ulangi i didalam kata
     jika kata i tidak didalam kata [i+ 1:] dan kata[i] tidak didalam kata[:i]
        huruf = kata ke [i]
         berhenti
5. Jika huruf == ''
    cetak -1
6. jika yang lain :
     cetak format string kata.index{huruf)+1}
7. Selesai
'''

# B
pattern = input()
text = input()

if pattern in text:
    print("Ketemu")
else:
    print("Tidak Ketemu")
print()
#kompleksitas waktu = O(n)
#Algoritma
'''
1. Mulai
2. input pattern
3. input text
4. jika pattern didalam text
     maka cetak ketemu
5. jika kondisi lain
      maka cetak tidak ketemu
6. Selesai
'''

# C
n = input()
n = list(map(int, n.split()))
prima = 0
for i in n:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            prima += 1
print(prima)

#kompleksitas waktu = O(n)
#Algoritma
'''
1. Mulai
2. Input n
3. Input n list(map(int,n.split()))
4. prima = 0 --> menyatakan bahwa prima nya bernilai 0
5. ulangi i didalam n
      jika i > 1
         ulangi j in range(2,i)
            jika i % j == 0 --> % = modulus
                berhenti
         jika kodisi lain :
            prima += 1
6. Cetak prima
7. Selesai
'''
