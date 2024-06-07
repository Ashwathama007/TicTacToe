def printBoard(xState,zState):
    # A function that will print the state of the board
    zero='X'if xState[0] else ('O' if zState[0] else 0)
    one='X'if xState[1] else ('O' if zState[1] else 1)
    two='X'if xState[2] else ('O' if zState[2] else 2)
    three='X'if xState[3] else ('O' if zState[3] else 3)
    four='X'if xState[4] else ('O' if zState[4] else 4)
    five='X'if xState[5] else ('O' if zState[5] else 5)
    six='X'if xState[6] else ('O' if zState[6] else 6)
    seven='X'if xState[7] else ('O' if zState[7] else 7)
    eight='X'if xState[8] else ('O' if zState[8] else 8)

    

    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")

def winner(xState,zState,check_val):
    #A function that will check if its a win for X or win for O or a draw..
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for x in wins:
        if xState[x[0]] + xState[x[1]] + xState[x[2]]==3 :
            print("Hurrah X Won !")
            return 1
        if zState[x[0]] + zState[x[1]] + zState[x[2]]==3 :
            print("Hurrah O Won !")
            return 0
        if(len(check_val)==9):
            print("Its a draw!!!")
            return 2
    return -1
def checking_validity(value,check_val):
    #It will check if the input values are valid or not
    if value in check_val:
        return -1
    elif value >8 or value<-1:
        return -1
    else:
        return 1

if __name__=="__main__":
    def start():
        xState=[0,0,0,0,0,0,0,0,0]
        zState=[0,0,0,0,0,0,0,0,0]
        check_val=[]
        turn =1 #1 for X and 0 for 0
        play_again=0
        print("Welcome to Tic Tac Toe")
        
        while(True):
            printBoard(xState,zState)
            if(turn==1):
                print("X's Turn")
                value=int(input("Please enter a value :"))
                ch=checking_validity(value,check_val)
                if(ch==1):

                    xState[value]=1
                    check_val.append(value)
                else:
                    while(ch!=1):
                        print("The value you selected has already been occupied or is out of range enter a different value ")
                        print("X's Turn")
                        value=int(input("Please enter a value :"))
                        ch=checking_validity(value,check_val)
                    if(ch==1):

                        xState[value]=1
                        check_val.append(value)


            else:
                print("O's Turn")
                value=int(input("Please enter a value :"))
                #TO check if the place has already been occupied or not
                ch=checking_validity(value,check_val)
                if(ch==1):

                    zState[value]=1
                    check_val.append(value)
                else:
                    while(ch!=1):
                        print("The value you selected has already been occupied or is out of range enter a different value ")
                        print("O's Turn")
                        value=int(input("Please enter a value :"))
                        ch=checking_validity(value,check_val)
                    if(ch==1):

                        zState[value]=1
                        check_val.append(value)
            check=winner(xState,zState,check_val)
            if(check!=-1 or check==2):
                print('Game Over')
                play_again=int(input("Do you want to play again?\nPress 1 for YES and any other number for NO :"))
                if play_again==1:
                    start()
                    
                else:
                    return None
                    

            #To switch turns between X and O
            turn=abs(turn-1)
    start()
        