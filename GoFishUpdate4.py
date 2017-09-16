# ====================================================
# Final Project: Go Fish
# Authors: Hannah Gray, Katja McKiernan, Anna Ivanov
# Date: May, 6th , 2015

#=====================================================
# Import Statements

import random 

#=====================================================
# Global Variables 

#deck = ["Ah", "Ad", "Ac", "As","2h", "2d", "2c", "2s","3h", "3d", "3c", "3s","10h", "10d", "10c", "10s" ]
deck = ["Ah", "Ad", "Ac", "As", "2h", "2d", "2c", "2s", "3h", "3d", "3c", "3s", "4h", "4d", "4c", "4s", "5h", "5d", "5c", "5s", "6h", "6d", "6c", "6s", "7h", "7d", "7c", "7s", "8h", "8d", "8c", "8s", "9h", "9c", "9d", "9s", "10h", "10d", "10c", "10s", "Jh", "Jd", "Jc", "Js", "Qh", "Qd", "Qc", "Qs", "Kh", "Kd", "Kc", "Ks"]

CompHand = []
UserHand = []
CompWinningList=[]
UserWinningList =[]

#====================================================
# Function definitions


def GoFish(): 
   """ The main function that draws the cards for both players and makes sure
   that any beginning matches are taken out of their hand. It also calles the
   function to display directions and does most beginning things. """
   print(" ")
   print("---------------------------Go Fish---------------------------------")
   instructions()
   drawCard(CompHand,5)
   drawCard(UserHand, 5)
   print("User Hand:",UserHand)
   #print("Comp Hand:", CompHand)  #we didn't delete the comp hand printouts in case the tester wants to see what's going on with the comptuer 
   checkMatch(UserHand, UserWinningList) 
   checkMatch(CompHand, CompWinningList)
   print("User Pairs:", UserWinningList)
   #print("Comp Pairs:", CompWinningList)
   print("User Hand:", UserHand)
   #print("Comp hand:", CompHand) 
   gameTime()
   
   
def instructions():
   """Takes no inputs, displays the instructions for how to play the game."""
   print("""Welcome to Go Fish! 
      
The object of this game is to make matches between two cards of the same rank( 1, 4, 5, A etc.).
You will be dealt a hand and it will apear below. 
      
The numbers have an s, c, d, or h attached to them to signify their suit. 
      
To ask for a card please type the letter or number of the card in your hand. Face Cards are typed
using a capital letter. For example if you were to ask for a king you would type 'K'. 

If you make a match with a card in your opponent's hand, then you get to go again and guess another card. If not you go fish 
and draw a random card. 

If this card was the same rank as the card you asked for, then you make a match and you also get to go 
again. 

If the card you drew does not matched the card you asked for, but it does match another card in your hand then you make a 
match, but your turn is over. 

If you draw a card and it doesn't match any other cards in your hand then your turn is over as well.
      
The computer will let you know if your opponent has that card in its hand and whether you made a match or not. 
The object of the game is to make more matches than your opponent.
      
Good Luck!
""") 
   
   
def gameTime():
   """Takes no inputs, this function has a while loop running while the game
   is being played. It calls UserTurn whcih sets the rest of the game in
   motion Once either the CompHand, UserHand, or deck is empty then it
   finishes the game and tells the player whether they won/lost/tied and asks
   them if they want to play again."""
   while CompHand != [] and UserHand != [] and deck != []: 
      UserTurn() 
   Cpairs = len(CompWinningList)
   Upairs = len(UserWinningList)
   if Upairs > Cpairs:
      print(" ")
      print("Congratulations!!! You Won! You had", Upairs, "matches, and the Computer had", Cpairs, ".")
      resp = input("Would you like to Play Again?")
      resp1 = str(resp)
      resp2 = resp1.lower()
      resp3 = resp2.strip()
      if resp3 == "yes":
         resetGame()
         GoFish()
      else:
         print(" ")
         print("Goodbye!")
         return
   elif Cpairs > Upairs:
      print(" ")
      print("I'm sorry, you Lost! The computer had", Cpairs, "matches, and you had", Upairs, ".")
      resp =input("Would you like to play again?")
      resp1 = str(resp)
      resp2 = resp1.lower()
      resp3 = resp2.strip()      
      if resp3 == "yes":
         resetGame()
         GoFish() 
      else:
         print(" ") 
         print("Goodbye!")
         return
   else:
      print(" ")
      print("It's a tie!!! You both had", Cpairs, "matches.")
      resp = input("Would you like to play again?")
      resp1 = str(resp)
      resp2 = resp1.lower()
      resp3 = resp2.strip()      
      if resp3 == "yes":
         resetGame()
         GoFish() 
      else:
         print(" ") 
         print("Goodbye!")
         return 


def drawCard(hand, num):
   """Takes a hand and a number as inputs. It randomly chooses a card from
   the deck's list and appends that card to the hand and removes it from the
   deck. It does this for however many times are indicated by the number."""
   for i in range(num):
      card = random.choice(deck)
      deck.remove(card) 
      hand.append(card)  
   return card 


def checkMatch(hand, winlist):
   """takes a hand and a winlist. This function checks existing cards in the
   hand for a match. It is only used initially when drawing the first hand.
   We compare every card in the hand to the card next to it recursively and
   take out any matches. """
   for card in hand:
      pos = hand.index(card)
      for card1 in hand[pos+1:]: #make sure we don't loop over the same card at the same time 
         if card[0] == card1[0]:
            match = (card, card1)
            winlist.append(match)
            hand.remove(card)
            hand.remove(card1)
            return checkMatch(hand, winlist)
   return winlist


def userInput():
   """This function asks the user for a card to ask for and makes sure that
   the number/face card that they asks for is valid, that they have it in
   their hand, it is the right kind of string, etc. This is to safeguard
   against user error."""
   print(" ")
   userinput = input("Choose a card to ask for from the other player:") 
   strInput = str(userinput)
   strInput1 = strInput.strip()
   UserHand1 = UserHand + ["T"]
   UHand = str(UserHand1) #we did this to turn the hand into a string so that we could search the userhand for matches
   if strInput1 in "abcdefghijklmnopqrstuvwxyzBCDEFGHILMNOPRSTUVWXYZ":
      print("Please type a valid character") 
      return userInput() 
   elif strInput1 in UHand: #here we search the newhand for the matched and if we find it than we know they typed it correctly
      return strInput1
   else:
      print("Please choose a card IN your hand.") 
      return userInput()


def UserTurn():
   """This function takes no inputs, and completes the main actions of the
   User's turn. It compares the user's input and decides if it matches a card
   in the comp hand, if it doesn't have a match, then it draws a card for the
   player and assesses whether or not that card matches the users hand at
   all. """
   checkMatch(UserHand, UserWinningList) #jsut to make sre all matches are already out
   try1 = compareUMatch() #compares the cards and figures out if they match 
   if len(try1) == 2:  #match was a tuple
      print ("Good Guess, You made a match!")
      if UserHand!= [] and CompHand!=[]:
         print("You get to go again")
         print("User Hand:", UserHand) 
         #print("Comp Hand:", CompHand) 
         print(" ")
         UserTurn()
   else:
      print(" ") 
      print("I'm sorry, Go fish!")
      dCard = drawCard(UserHand, 1)      
      print("Drawn Card:", dCard) 
      if dCard[0] == try1[0]: #try1 here will equal the value that the user inputted b/c it's lenght is !=2 and thus the user input is returned
         makeMatch(dCard, UserHand, UserWinningList)
         print("It matched the one you fished for") 
         if UserHand!= [] and CompHand!=[]:
            print("so you get to go again!") 
            print("User Hand:", UserHand)
            #print("CompHand:", CompHand) 
            print(" ")
            UserTurn() #user gets to go again
      else:
         elseMakeMatch(dCard,UserHand, UserWinningList) #checks the rest of the cards to see if they match the draw card
         print("Now it's the computer's turn")
         print("User Hand:", UserHand) 
         #print("Comp Hand:", CompHand)  
         print(" ") 
         CompTurn()  #user doesn't get to go again. 
   return UserWinningList


def CompTurn(): 
   """Takes no inputs. This function is very similar to UserTurn, but the
   print statements are different, and it also relies on helper functions
   that are defined for only the CompHand and wont work for UserTurn."""
   checkMatch(CompHand, CompWinningList)
   try2 = compareCMatch()
   if len(try2) == 2:
      print ("The Computer made a match!")
      if UserHand != [] and CompHand!=[]:
         print("Computer goes again") 
         #print("User Hand:", UserHand) 
         #print("Comp Hand:", CompHand) 
         print(" ")
         CompTurn()
   else:
      print("Computer guess was not a match, it goes fish!") 
      dCard = drawCard(CompHand, 1)
      #print("Drawn Card:", dCard) 
      if dCard[0] == try2[0]: 
         makeMatch(dCard, CompHand, CompWinningList)
         print("The Computer drew the card it asked for") 
         if UserHand != [] and CompHand!=[]:
            print("It goes again!") 
            #print("Comp Hand:", CompHand)
            #print("User Hand:", UserHand) 
            print(" ")
            CompTurn()
      else:
         elseMakeMatch(dCard, CompHand, CompWinningList)
         print("Now it's your turn again")
         print("User Hand:", UserHand) 
         #print("Comp Hand:", CompHand) 
         print(" ") 
         UserTurn()
   return CompWinningList   


def makeMatch(card, hand, winlist):
   """Checks that a card just 'fished for' is a match with the card you asked
   for. If they match then it gets moved to the approppiate winlist. This is
   used throughout the game to check the cards both the user and comp draw.
   """
   for card1 in hand:
      if card1[0] == card[0]: #compares drawn card to all the cards in the hand
         match = ((card1, card))
         winlist.append(match)
         hand.remove(card1)
         hand.remove(card)
         if hand == UserHand:
            print ("Match:", match)
         return hand 
   print("The card drawn doesn't match the one that was fished for") 
   return winlist



def elseMakeMatch(card, hand, winlist):
   """Checks that a card just drawn is a match with any of the other cards in
   your hand (which you did not ask for). If in the hand it gets moved to the
   approppiate winlist. THe different between this and the function before is
   taht the print statements are a bit different. makeMatch tells the user if
   the card they ASKED FOR matched the FISHED for card, while elseMakeMatch
   just telss the user if the FISHED card matches ANY card in your hand."""
   hand.remove(card) #first removes the fished for card from your hand to compare it. 
   for card1 in hand:
      if card1[0] == card[0]:
         match = ((card1, card))
         winlist.append(match)
         hand.remove(card1)
         if hand == UserHand:
            print("Yay! The card matched another card in your hand")
            print ("Match:", match)
            return hand 
         else:
            print("The computer made a  match")
            return hand 
   print("The card drawn was not a match") 
   hand.append(card) #re-appends it if no match was found. 
   return winlist   


   
def compareUMatch():
   """Takes no inputs, this function compares the Userinput and checks to see
   if it matches a card in the comp hand, if it does then it removes the card
   from both the CompHand and the UserHand and creates a tuple called 'Match'
   which it adds to the UserWinningList. If they don't match, the function
   returns the original user input so that UserTurn can asses that input and
   see if it matches the card that will be fished for. This function only
   works for the Userturn"""
   card = userInput() 
   val = str(card)
   for i in UserHand:
      if val[0] in i:
         matchedCard = i
         for i in CompHand:
            if val[0] in i:
               otherCard = i
               match = (matchedCard, otherCard)   
               UserHand.remove(matchedCard)
               CompHand.remove(otherCard)
               UserWinningList.append(match)
               print(" ") 
               print("Match:",  match)
               return match
   match = (val[0]) #safeguard against users who type 10
   return match 



def compareCMatch():
   """Takes no inputs, this funciton is like compareUMatch, but it is set up
   specifically for the computer because instead of relying on the userinput
   to choose what card to ask for and thus subsequently analyze, this
   funciton randomly draws a card from the CompHand and then uses that. It
   also take the match and returns it to the CompWinningList."""
   gCard = random.choice(CompHand)
   val = gCard[0]
   if val == "1":
      print("Computer asked you for: 10")
   else:
      print("Computer asked you for:", val)   
   for i in CompHand:
      if val in i:
         matchedCard = i
         for i in UserHand:
            if val in i:
               otherCard = i
               match = (matchedCard, otherCard)   
               UserHand.remove(otherCard)
               CompHand.remove(matchedCard)
               CompWinningList.append(match) 
               #print(" ")
               #print("Match:",  match) #toggle blocked out for the actual game, undo this if you wnat to see things from the computer's side. 
               return match
   match = (val) 
   return match    
   
   
def resetGame():
   """This function resets the game by deleting any cards left in all of the
   hands/lists/deck and then re-appending the cards to the deck."""
   del CompHand[:] 
   del UserHand[:]
   del CompWinningList[:]
   del UserWinningList[:]
   del deck[:]
   deck.append("Ah")
   deck.append("Ad")
   deck.append("Ac")
   deck.append("As")
   deck.append("2h")
   deck.append("2d")
   deck.append("2c")
   deck.append("2s")
   deck.append("3h")
   deck.append("3d")
   deck.append("3k")
   deck.append("3s")
   deck.append("4h")
   deck.append("4d")
   deck.append("4c")
   deck.append("4s")
   deck.append("5h")
   deck.append("5d")
   deck.append("5c")
   deck.append("5s")
   deck.append("6h")
   deck.append("6d")
   deck.append("6c")
   deck.append("6s")
   deck.append("7h")
   deck.append("7d")
   deck.append("7c")
   deck.append("7s")
   deck.append("8h")
   deck.append("8d")
   deck.append("8c")
   deck.append("8s")
   deck.append("9h")
   deck.append("9c")
   deck.append("9d")
   deck.append("9s")
   deck.append("10h")
   deck.append("10d")
   deck.append("10c")
   deck.append("10s")
   deck.append("Jh")
   deck.append("Jd")
   deck.append("Jc")
   deck.append("Js")
   deck.append("Qh")
   deck.append("Qd")
   deck.append("Qc")
   deck.append("Qs")
   deck.append("Kh")
   deck.append("Kd")
   deck.append("Kc")
   deck.append("Ks")   
   return deck


if __name__ == 'main':
   GoFish()
