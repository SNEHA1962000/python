play1=input("enter the player1")
play2=input("enter the player2")
if(play1=="rock" and play2=="scissor"):
  print("play1 wins")
elif(play1=="rock" and play2=="paper"):
  print("play2 wins")
elif(play1=="paper" and play2=="scissor"):
  print("play2 wins") 
elif(play1=="paper" and play2=="rock"):
  print("play1 wins")
elif(play1=="scissor" and play2=="paper"):
  print("play1 wins")
elif(play1=="scissor" and play2=="rock"):
  print("play2 wins")
elif(play1==play2):
  print("play1 wins") 
else :
    print("invalid")
