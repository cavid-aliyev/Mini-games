import random

tries = 0

number = random.randint(1, 50)
print("Ahaa... Mənim 1 50 arası fikirləşdiyim rəqəmi tapa bilərsənmi? ;)")

while tries < 6:
    guess = int(input("Rəqəm yaz: "))

    tries += 1

    if guess < number:
        print("Yazdığın rəqəm çox aşağıdı")
        print(f"Cəhd sayı:{tries}")

    if guess > number:
        print("Yazdığı rəqəm çox yuxarıdı")
        print(f"Cəhd sayı:{tries}")

    if guess == number:
        print(f"Vauu.. sən mənim rəqəmimi {tries} cəhdə tapdın təbriklər!")

    if guess != number and tries == 6:
        print(f"Çox təəssüflər, lakin mənim rəqəmim {number} idi")
        break


