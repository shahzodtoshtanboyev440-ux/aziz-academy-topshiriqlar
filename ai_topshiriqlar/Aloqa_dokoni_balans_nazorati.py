# Aloqa do'koni: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: O'rnatish va muhit — Python, interpreter, IDE sozlash
# Ball: 100
# Aziz Academy — AI Topshiriq

b = 500000 
m = b 
c = 0 
for _ in range(int(input())):
    s = input()
    v = int(s[1:])
    if s[0] == '+':
        b += v
    else:
        b -= v
        c += 1 
    if b < m:
        m = b 
print(b)
print(m)
print(c)