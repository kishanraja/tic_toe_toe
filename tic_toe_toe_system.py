import random
def display_board( state ):
	print ("-------------")
	print ("| %i | %i | %i |" % (state[0], state[1], state[2]))
	print ("-------------")
	print ("| %i | %i | %i |" % (state[3], state[4], state[5]))
	print ("-------------")
	print ("| %i | %i | %i |" % (state[6], state[7], state[8]))
	print ("-------------")

def checkPos(state,vv):
        y=random.randint(0,8)
        print("------%i"%y)
        if y not in vv:
                if((state[0]==1 and state[1]==1) or (state[3]==1 and state[4]==1) or (state[6]==1 and state[7]==1) or (state[0]==1 and state[4]==1) or (state[2]==1 and state[4]==1) or (state[0]==1 and state[3]==1) or (state[1]==1 and state[4]==1) or (state[2]==1 and state[5]==1)or (state[6]==1 and state[3]==1)or (state[7]==1 and state[4]==1) or (state[8]==1 and state[5]==1) or (state[1]==1 and state[2]==1) or (state[4]==1 and state[5]==1) or (state[7]==1 and state[8]==1) or (state[8]==1 and state[4]==1) or (state[6]==1 and state[4]==1) or (state[0]==1 and state[6]==1) or (state[6]==1 and state[8]==1) or (state[2]==1 and state[8]==1) or (state[0]==1 and state[2]==1) or (state[8]==1 and state[0]==1) or (state[2]==1 and state[6]==1) or (state[3]==1 and state[5]==1)):
                        #print("%i"%y)
                        
                        if((state[0]==1 and state[1]==1) or (state[8]==1 and state[5]==1) or (state[6]==1 and state[4]==1)):
                                if(state[2]==2):
                                        return 2
                        if((state[3]==1 and state[4]==1) or (state[2]==1 and state[8]==1)):
                                if(state[5]==2):
                                        return 5
                        if((state[6]==1 and state[7]==1) or (state[0]==1 and state[4]==1) or (state[2]==1 and state[5]==1)):
                                if(state[8]==2):
                                        return 8
                        if((state[2]==1 and state[4]==1) or (state[0]==1 and state[3]==1) or (state[8]==1 and state[7]==1)):
                                if(state[6]==2):
                                        return 6
                        if((state[1]==1 and state[4]==1) or (state[8]==1 and state[6]==1)):
                                if(state[7]==2):
                                        return 7
                        if((state[2]==1 and state[1]==1) or (state[6]==1 and state[3]==1)):
                                if(state[0]==2):
                                        return 0
                        if((state[5]==1 and state[4]==1) or (state[0]==1 and state[6]==1)):
                                if(state[3]==2):
                                        return 3
                        if((state[7]==1 and state[4]==1) or (state[0]==1 and state[2]==1)):
                                if(state[1]==2):
                                        return 1
                        if((state[0]==1 and state[8]==1) or (state[6]==1 and state[2]==1) or (state[3]==1 and state[5]==1)):
                                if(state[4]==2):
                                        return 4
                        return True
                if((state[0]==0 and state[1]==0) or (state[3]==0 and state[4]==0) or (state[6]==0 and state[7]==0) or (state[0]==0 and state[4]==0) or (state[2]==0 and state[4]==0) or (state[0]==0 and state[3]==0) or (state[1]==0 and state[4]==0) or (state[2]==0 and state[5]==0)or (state[6]==0 and state[3]==0)or (state[7]==0 and state[4]==0) or (state[8]==0 and state[5]==0) or (state[1]==0 and state[2]==0) or (state[4]==0 and state[5]==0) or (state[7]==0 and state[8]==0) or (state[8]==0 and state[4]==0) or (state[6]==0 and state[4]==0) or (state[0]==0 and state[6]==0) or (state[6]==0 and state[8]==0) or (state[2]==0 and state[8]==0) or (state[0]==0 and state[2]==0) or (state[8]==0 and state[0]==0) or (state[2]==0 and state[6]==0) or (state[3]==0 and state[5]==0)):
                        print("%i"%y)
                        
                        if((state[0]==0 and state[1]==0) or (state[8]==0 and state[5]==0) or (state[6]==0 and state[4]==0)):
                                if(state[2]==2):
                                        return 2
                        if((state[3]==0 and state[4]==0) or (state[2]==0 and state[8]==0)):
                                if(state[5]==2):
                                        return 5
                        if((state[6]==0 and state[7]==0) or (state[0]==0 and state[4]==0) or (state[2]==0 and state[5]==0)):
                                if(state[8]==2):
                                        return 8
                        if((state[2]==0 and state[4]==0) or (state[0]==0 and state[3]==0) or (state[8]==0 and state[7]==0)):
                                if(state[6]==2):
                                        return 6
                        if((state[1]==0 and state[4]==0) or (state[6]==0 and state[8]==0)):
                                if(state[7]==2):
                                        return 7
                        if((state[2]==0 and state[1]==0) or (state[6]==0 and state[3]==0)):
                                if(state[0]==2):
                                        return 0
                        if((state[5]==0 and state[4]==0) or (state[0]==0 and state[6]==0)):
                                if(state[3]==2):
                                        return 3
                        if((state[7]==0 and state[4]==0) or (state[0]==0 and state[2]==0)):
                                if(state[1]==2):
                                        return 1
                        if((state[0]==0 and state[8]==0) or (state[6]==0 and state[2]==0) or (state[3]==0 and state[5]==0)):
                                if(state[4]==2):
                                        return 4
                        return True
                else:
                        return y
                return True
        else:
                ans = checkPos(state,vv)
                return ans
                
def tic_toe_toe_sys(state):
        player1=True
        player2=False
        i=9
        v=0
        vv=[]
        while(i>0):
                if((state[0]==1 and state[1]==1 and state[2]==1) or (state[3]==1 and state[4]==1 and state[5]==1) or (state[6]==1 and state[7]==1 and state[8]==1) or (state[0]==1 and state[4]==1 and state[8]==1) or (state[2]==1 and state[4]==1 and state[6]==1) or (state[0]==1 and state[3]==1 and state[6]==1) or (state[1]==1 and state[4]==1 and state[7]==1) or (state[2]==1 and state[5]==1 and state[8]==1)):
                        print("player 1 win")
                        return False
                if((state[0]==0 and state[1]==0 and state[2]==0) or (state[3]==0 and state[4]==0 and state[5]==0) or (state[6]==0 and state[7]==0 and state[8]==0) or (state[0]==0 and state[4]==0 and state[8]==0) or (state[2]==0 and state[4]==0 and state[6]==0) or (state[0]==0 and state[3]==0 and state[6]==0) or (state[1]==0 and state[4]==0 and state[7]==0) or (state[2]==0 and state[5]==0 and state[8]==0)):
                        print("System win")
                        return False
                if player1==True:
                        v=int(input("Enter player 1 position "))
                        state[v-1]=1
                        player1=False
                        vv.append(v-1)
                        if(player1==False):
                                v=checkPos(state,vv)
                                #print("%i---"%v)
                                state[v]=0
                                vv.append(v)
                                player1=True
                i=i-1
                display_board(state)
        return True

starting_state=[2,2,2,2,2,2,2,2,2]
print("start state:")
display_board(starting_state)
tic_toe_toe_sys( starting_state )
