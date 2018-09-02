def display_board( state ):
	print ("-------------")
	print ("| %i | %i | %i |" % (state[0], state[1], state[2]))
	print ("-------------")
	print ("| %i | %i | %i |" % (state[3], state[4], state[5]))
	print ("-------------")
	print ("| %i | %i | %i |" % (state[6], state[7], state[8]))
	print ("-------------")


def tic_toe_toe(state):
        player1=True
        player2=False
        i=9
        while(i>0):
                if((state[0]==1 and state[1]==1 and state[2]==1) or (state[3]==1 and state[4]==1 and state[5]==1) or (state[6]==1 and state[7]==1 and state[8]==1) or (state[0]==1 and state[4]==1 and state[8]==1) or (state[2]==1 and state[4]==1 and state[6]==1) or (state[0]==1 and state[3]==1 and state[6]==1) or (state[1]==1 and state[4]==1 and state[7]==1) or (state[2]==1 and state[5]==1 and state[8]==1)):
                        print("player 1 win")
                        return False
                if((state[0]==0 and state[1]==0 and state[2]==0) or (state[3]==0 and state[4]==0 and state[5]==0) or (state[6]==0 and state[7]==0 and state[8]==0) or (state[0]==0 and state[4]==0 and state[8]==0) or (state[2]==0 and state[4]==0 and state[6]==0) or (state[0]==0 and state[3]==0 and state[6]==0) or (state[1]==0 and state[4]==0 and state[7]==0) or (state[2]==0 and state[5]==0 and state[8]==0)):
                        print("player 2 win")
                        return False
                if player1==True:
                        state[int(input("Enter player 1 position "))-1]=1
                        player1=False
                else:
                        state[int(input("Enter player 2 position "))-1]=0
                        player1=True
                i=i-1
                display_board(state)
        return True

starting_state=[1,2,3,4,5,6,7,8,9]
print("start state:")
display_board(starting_state)
tic_toe_toe( starting_state )
