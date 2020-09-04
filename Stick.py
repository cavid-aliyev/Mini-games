sticks = 10
player_turn = 1

while sticks > 0:
    print(f"Neçə dənə çubuq göturduz? , Qalan çubuqların sayı {sticks}")
    taken = int(input())

    if taken < 1 or taken > 3:
        print(f"Siz {taken} dənə çubuq götürmək istədiz. Götürə biləcəyiniz çubuq sayı 1,2,3 ")
        continue

    sticks -= taken
    print(f"Götürdüyünüz çubuqların sayı: {taken}\n")

    if sticks <= 0:
        print(f"Oyunda çubuq qalmadı. \nPlayer {player_turn} uduzdu(")

    



