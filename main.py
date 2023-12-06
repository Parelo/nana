
import random

print("pasirinkite spejimo skaiciaus ribas")
nuo = int(input("Nuo:"))
iki = int(input("iki"))

sugeneruotas = random.randint (nuo, iki)

counter = 0



print(sugeneruotas)


while True:
    spejemas = int(input("spejemas skaicius"))
    if spejemas > sugeneruotas:
        counter += 1
        print("maziau")

    if spejemas < sugeneruotas:
        print("daugiau")
    if spejemas == sugeneruotas:
        print(f"Valio spejimu skaicius {counter}")

        break
