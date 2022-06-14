def CheckingAns(ans,trial):
    Char = 0
    Position = 0 
    for i in range (0, int(len(ans))):
        if trial[i] == ans[i]:
            Position = Position + 1
        for j in range (0, int(len(ans))):
                if trial[i] == ans[j]:
                    Char = Char + 1
    if(Char == len(ans) and Position == len(ans)):
        print("Correct")
        print("Char = " + str(Char))
        print("Position = " + str(Position))
        return True
    else:
        print("Wrong")
        print("Char = " + str(Char))
        print("Position = " + str(Position))
        return False

ans = "routes"
result = False
while(True):
    trial = input("Type word and check answer: ")
    if (len(ans)!= len(trial)):
        print("error: wrong length word")          
    else:
        result = CheckingAns(ans,trial)
    if result:
        break;
