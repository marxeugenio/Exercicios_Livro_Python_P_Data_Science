count = 0

for x in range(2000, 5001):
    if x % 2 == 0 and x % 4 == 0 and x % 3 == 0:
        count += 1
    
print(f"Existem {count} números pares divisiveis por 4 e 3 entre 2000 e 5000")
