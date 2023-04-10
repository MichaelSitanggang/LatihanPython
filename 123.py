# Nomor 1
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
# nomor 2
pattern = input()
text = input()

if pattern in text:
    print("Ketemu")
else:
    print("Tidak Ketemu")
print()

# Nomor 3
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
