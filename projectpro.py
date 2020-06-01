#initializing the grid
def grid (n):
	arr=[]
	for i in range(n):
		row=[]
		for j in range(n):
			row.append(-1)	
		arr.append(row)
	
	return arr
#displaying the grid in the form of "" and then checking for each element if its equal to 1 we put X if its equal to 2 we put O
def display (arr,n):
	#we initialize a grid with ""s
	arrdisp=[]
	for i in range(n):
		row=[]
		for j in range(n):
			row.append("")	
		arrdisp.append(row)
	
	#we check if for each element if its equal to 1 we put X if its equal to 2 we put O
	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i][j]==-1 :
				arrdisp[i][j]="-"
				
			elif arr[i][j]==1 :
				arrdisp[i][j]="X"

			elif arr[i][j]==2 :
				arrdisp[i][j]="O"
	
	for i in range(len(arrdisp[0])):
		print(arrdisp[i])

#We check if there is a winner 
def winner(arr,disc,n):
	# the first loop is to check for horizontal lines
	for j in range(n):
		for i in range(n- 3):
			if arr[i][j] == disc and arr[i+1][j] == disc and arr[i+2][j] == disc and arr[i+3][j] == disc:
				return True
	 #the second one is to check for vertical lines
	for i in range(n):
		for j in range(n - 3):
			if arr[i][j] == disc and arr[i][j+1] == disc and arr[i][j+2] == disc and arr[i][j+3] == disc:
				return True
	#the third and the fourth are to check for the 2 diagonals
	for i in range(n - 3):
		for j in range(3, n):
			if arr[i][j] == disc and arr[i+1][j-1] == disc and arr[i+2][j-2] == disc and arr[i+3][j-3] == disc:
				return True

	for i in range(n- 3):
		for j in range(n - 3):
			if arr[i][j] == disc and arr[i+1][j+1] == disc and arr[i+2][j+2] == disc and arr[i+3][j+3] == disc:
				return True

	return False
#this function is to check for the first row, if there is no empty spots, we return a tie and we exit.( note: we didnt check if there a winner here because we checked for it in the turn function)
def tie(arr,n,col):
	cpt=0
	for i in range(0,n):
		if (arr[0][i] != -1):
		    cpt=cpt+1
		if( cpt==n):
			print("The complete slot is full,\n The game is a Tie.")
			arr=grid(n)
			exit()
# here we are checking if the column entered is valid or not
def play(col,n):
	if col <1 or col> n:	
		return -1
	else:
		return 0

def turn(play,player,disc,boole,n):
	arr=grid (n)
	display(arr,n)
	while boole==False  :#we here check it is the turn of which player
		if player % 2 !=0 :
			print("Player 1")
			disc= "X"
		elif player % 2 == 0:
			print("player2")
			disc ="O"
		if (disc =="x") or (disc== "X"):
			disc=1
		elif (disc =="O") or (disc =="o"):
			disc=2
		
		col = int(input("Choose which column to drop your disc \n"))
		check=play(col,n)
		while check ==-1 :
			#here is the case when the player enter a invalid spot
			print("Enter column in proper range")
			col = int(input("Choose which column to drop your disc \n"))
			check=play(col,n)
		#here is the case when the player enter a full column
		while (arr[0][(int(col)-1)] != -1):
			print("Column is full,cannot place disc")
			col = int(input("Choose which column to drop your disc \n"))	
		drop = col -1
		for row in range((len(arr) - 1), -1, -1):#this loop is to drop the disc
			if arr[row][drop] == -1:
				arr[row][drop] = disc
				break #we put a breakhere otherwise it will a full column of the user's disc and so the user win
		display(arr,n)
		boole=winner(arr,disc,n)
		tie(arr,n,col)
		#here we check if there is a winner or not, and which player is the winner
		if (boole == True) and (player  % 2 != 0):
			print("Player 1 wins !")
		elif (boole == True) and (player % 2 == 0):
			print("Player 2  wins ")
		player+=1 
"----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
def rotatechoice(play,player,disc,boole,n):
	arr=grid(n)
	display(arr,n)
	while boole==False  :
		#in this part we are aassigning x or o for each player  
		if player % 2 !=0 :
			print("Player 1's turn(X)")
			disc= "X"
		elif player % 2 == 0:
			print("player2's turn(O)")
			disc ="O"
		if (disc =="x") or (disc== "X"):
			disc=1
		elif (disc =="O") or (disc =="o"):
			disc=2
		
		check=-1
		while check ==-1:
			try:
				#here is the case when the player enter a invalid spot
				col = int(input("Choose which column to drop your piece \n"))
				check=play(col,n)
				while check ==-1 :
					print("Enter column in proper range")
					col = int(input("Choose which column to drop your piece \n"))
					check=play(col,n)
				#here is the case when the column is full
				while (arr[0][(int(col)-1)] != -1):
					print("Column is full,cannot place piece")
					col = int(input("Choose which column to drop your piece \n"))
					check=play(col,n)
					while check ==-1 :
						print("Enter column in proper range")
						col = int(input("Choose which column to drop your piece \n"))
						check=play(col,n)
				check=0
			except ValueError :
				print("Invalid input ")
				check=-1
		#this loop is to drop the disc
		drop = int(col) - 1
		for row in range((len(arr) - 1), -1, -1):#this loop is to drop the disc
			if arr[row][drop] == -1:
				arr[row][drop] = disc
				break #we put a breakhere otherwise it will a full column of the user's disc and so the user win
			else:
				continue
		check=-1
		while check==-1:
			try:# here we ask the user for the number of rotations he want the grid to do
				print("How many rotations do you want the grid to rotate? ")
				k = int(input())
				if k >=0 :
					rotate(k,arr,n)
					check=0
			except ValueError:
				print("Not a valid number Of Rotations")
				check=-1
		
		display(arr,n)
		boole=winner(arr,disc,n)
		tie(arr,n,col)
		if (boole == True) and (player  % 2 != 0):
			print("Player 1 won")
		elif (boole == True) and (player % 2 == 0):
			print("Player 2  win ")
		player+=1   
#here is our function to drop the disc
def drop(arr,n):
	for i in range(n-1):
		for j in range(n):
			if arr[i+1][j]== -1 :
				arr[i+1][j]=arr[i][j]
				arr[i][j]=-1
#here is the function to do the rotations
def rotate(k,arr,n):#k is the no of rotations
	for l in range(0,k):
		m = len(arr[0])
		for i in range(m // 2):
			for j in range(i, m - i - 1):
				temp = arr[i][j]
				arr[i][j] = arr[m - 1 - j][i]
				arr[m - 1 - j][i] = arr[m - 1 - i][m - 1 - j]
				arr[m - 1 - i][m - 1 - j] = arr[j][m - 1 - i]
				arr[j][m - 1 - i] = temp
		    
			for i in range(n):#here is the loop responsible for the number of rotations
				drop(arr,n) 

print("    Let's play Connect FOUR ") # 4 print to initialize a kind of an interface
print("________________________________________\n")#to return to a the next line
print("1.  Play classic connect 4? ")
print("2.  Play connect 4 with rotations? ")
print("\n________________________________________")
# So as long as the player don't put valid input (1 or 2) we are ask to input again
playe=int(input("Press 1 to choose the first option or 2 for the second option\n"))
while playe<1 or playe>2:
    playe=int(input("Press 1 to choose the first gamemode or 2 for the second one \n"))
    print("Enter a correct choice (1 or 2)")
if playe == 1 or playe ==2: # If the input are valid the variable changes and we can get to the following command
    disc=" "
    boole = False
    check=0
    player=1

    n=int(input("Enter dimensions of your N x N game grid \n")) # To get the input of the grid from the user
    while n < 4: # A loop to ask again a size if the one given is to small
        print("Your grid is too small to play connect 4, you need at least a 4x4 grid ")
        n=int(input("Enter dimensions of your N x N game boagridrd \n"))
    if n>=4 : # Once the grid has good dimensions, the variable changes 
        check=0


if playe == 1 :    # If the player choosed the gamemode without rotate
    turn(play,player,disc,boole,n)
elif playe == 2 :# If the player choosed the gamemode with rotate
    rotatechoice(play,player,disc,boole,n) 
t=int(input(""))

