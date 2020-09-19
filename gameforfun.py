# Hamımızın bildiyi rock paper scissors oyunu in Python!!!

import random

print(""""
    -----------------------------
       | Rock Paper Scissors |
    -----------------------------    
""")

commandList = ["R", "P", "S"]

userScore = 0
computerScore = 0
i = 1

chance = int(input("Neçə dəfə oynamaq fikrin var?) (bax dostum, sonra dəyişmək yoxdur ha)"))

while i <= chance:
    computerCh = str(random.choice(commandList))

    userCh = input("Enter Rock, Paper, Scissors (key to press: R,P,S): ").upper()

    if userCh == computerCh:
        print("Oha.. ikivizdə eyni şey seçdiz")

    elif userCh == "R":
        print("Computer Enter: ", computerCh)
        if computerCh == "P":
            print("👉 Uduzdun:( Kağız daşı bağlıyır")
            computerScore += 1
        else:
            print("👉 Uddun! Daş qayçını əzir")
            userScore += 1
    elif userCh == "P":
        print("Computer Enter: ", computerCh)
        if computerCh == "S":
            print("👉 Uduzdun:( Qayçı kağızı kəsir")
            computerScore += 1
        else:
            print("👉 Uddun! Kağız daşı bağlıyır")
            userScore += 1

    elif userCh == "S":
        print("Computer Enter: ", computerCh)
        if computerCh == "R":
            print("👉 Uduzdun:( Daş qayçını əzir")
            computerScore += 1
        else:
            print("👉 Uddun! Qayçı kağızı kəsir")
            userScore += 1
    else:
        print(":(")

    print("\n\t******Qələbə lövhəsi******")
    print(f"\t Sən: {userScore} | Computer: {computerScore}")
    print("\t**********************")
    print(f"Oyun nömrə:[{i}]")
    print("========================================================")

    i += 1

print("\n\n##### Game Over #####")
print("*******************************************")
if userScore < computerScore:
    print(
        f"😭 Bağışla amma sən uduzdun 😭\n Compüter bu oyunu {computerScore} ilə qalib gəldi"
    )
elif userScore == computerScore:
    print("😅 Oyunda bərabərlik var.Bir daha oyna:D 😅")
else:
    print(f"😄 Sən qalib gəldin!! Sən {userScore} xal ilə qalib gəldin vouvv 😄")
