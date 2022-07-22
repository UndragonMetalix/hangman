def handman(word):
    wrong = 0
    stages = ["",
             "____________        ",
             "|           |       ",
             "|           0       ",
             "|          /|\      ",
             "|          / \      ",
             "|                   ",
             "|                   "
             ]
    rlettrs = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to execution!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rlettrs:
            cind = rlettrs.index(char)
            board[cind] = char
            rlettrs[cind] = '$'
        else:
            wrong +=1 
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You Win! The word was:  ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You Lose! word:{}.".format(word))
    

handman("oil")
        
   

