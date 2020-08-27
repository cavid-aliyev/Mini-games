#inputlarim help,start stop quit
#help yazanda(boyuk kicik ferq elemir) awagidakilar cixir
#diger birweyler yazanda komp bawa duwmur
#start edende deyirki oyun bawladi
#stop edende deyrki mawin dayandi
#quit edende proses dayanir(break)


command = ""
started = False #start duymesi 2 defe basilanda oyuncunu xeberdarliq etmek ucun
stopped = False #stop duymesi 2 defe basilanda oyuncunu xeberdarliq etmek ucun

while True:
    command = input(">").lower()
    if command == "start":
       if started:
           print("Car is already started")
       else:
           started = True
           print("Car started")
    elif command == "stop":
        if stopped:
            print("Car is already stopped")
        else:
            stopped = True
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand you ")