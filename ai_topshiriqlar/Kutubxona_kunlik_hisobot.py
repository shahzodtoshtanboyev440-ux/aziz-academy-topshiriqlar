# Kutubxona: kunlik hisobot
# Kurs: Dasturlash / IT
# Mavzu: O'rnatish va muhit — Python, interpreter, IDE sozlash
# Ball: 100
# Aziz Academy — AI Topshiriq

t = s = 0 
k = ""
max_d = -1
for _ in range(int(input())):
    n, p, q = input().split()
    d = int(p) * int(q)
    t += d 
    s += int(q)
    if d > max_d:
        max_d = d
        k = n 
print(t)
print(k)
print(s)