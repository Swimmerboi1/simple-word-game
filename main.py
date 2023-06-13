import random
import os
words = ['abuse', 'adult', 'agent', 'anger', 'apple', 'award', 'Basis', 'Beach', 'Birth', 'Bingo', 'Block', 'Blood', 'Board', 'Brain', 'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class', 'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death', 'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event', 'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Frank', 'Front', 'Fruit', 'Glass', 'Grant', 'Grass', 'Green', 'Group', 'Guide', 'Heart', 'Henry', 'Horse', 'Hotel', 'House', 'Image', 'Index', 'Input', 'Issue', 'Japan', 'Jones', 'Judge', 'Knife', 'Layer', 'Level', 'Lewis', 'Light', 'Limit', 'Lunch', 'Major', 'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Motor', 'Mouth', 'Music', 'Night', 'Noise', 'North', 'Novel', 'Nurse', 'Offer', 'Order', 'Other', 'Owner', 'Panel', 'Paper', 'Party', 'Peace', 'Peter', 'Phase', 'Phone', 'Piece', 'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize', 'Proof', 'Queen', 'Radio', 'Range', 'Radio', 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 'Scale', 'Scene', 'Scope', 'Score', 'Sense', 'Shape', 'Share', 'Sheep', 'Sheet', 'Shift', 'Shirt', 'Shock', 'Sight', 'Simon', 'Skill', 'Sleep', 'Smile', 'Smith', 'Smoke', 'Sound', 'South', 'Space', 'Speed', 'Spite', 'Sport', 'Squad', 'Staff', 'Stage', 'Start', 'State', 'Steam', 'Steel', 'Stock', 'Stone', 'Store', 'Study', 'Stuff', 'Style', 'Sugar', 'Table', 'Taste', 'Terry', 'Theme', 'Thing', 'Title', 'Total', 'Touch', 'Tower', 'Track', 'Trade', 'Train', 'Trend', 'Trial', 'Trust', 'Truth', 'Uncle', 'Union', 'Unity', 'Value', 'Video', 'Visit', 'Voice', 'Waste', 'Watch', 'Water', 'While', 'White', 'Whole', 'Woman', 'World', 'Youth']
word = (random.choice(words))
word1 = word
word = (" ".join(word))
word.lower()
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
difficulty = str(input('What difficulty would you like to play on?\n 0 baby\n 1 easy\n 2 medium\n 3 hard\n 4 very hard\n 5 impossible\n'))
while difficulty.isdigit() is False:
  print('you must enter 0, 1, 2, 3, 4, or 5')
  difficulty = input()
difficulty = int(difficulty)
clearConsole()
def guesses():  
  guess1 = input('Next guess!\n')
  if len(guess1) != 5:
    print('word has to be 5 letters!')
    guess1 = input()
    guess1 = (' '.join(guess1))
    a,b,c,d,e = word.split()
    A1,B1,C1,D1,E1 = guess1.split()
    right_spot1 = 0
    wrong_spot1 = 0
    if(a == A1):
      right_spot1 += 1
    elif(a == B1 or a == C1 or a == D1 or a ==E1):
      wrong_spot1 +=  1
    if(b == B1):
      right_spot1 +=  1
    elif(b == A1 or b == C1 or b == D1 or b == E1):
      wrong_spot1 += 1
    if(c == C1):
      right_spot1 += 1
    elif(c == A1 or c == B1 or c == D1 or c == E1):
      wrong_spot1 += 1
    if(d == D1):
      right_spot1 += 1
    elif(d == A1 or d == B1 or d == C1 or d == E1):
      wrong_spot1 += 1
    if(e == E1):
      right_spot1 += 1
    elif(e == A1 or e == B1 or e == C1 or e == D1) :
      wrong_spot1 += 1
    if right_spot1 == 5:
      return('You win!') 
    else:
      print('letters in the right spot:')
      print(right_spot1)
      print('letters in the word but not in the right spot:')
      print(wrong_spot1)
  else:
    guess1 = (' '.join(guess1))
    a,b,c,d,e = word.split()
    A1,B1,C1,D1,E1 = guess1.split()
    right_spot1 = 0
    wrong_spot1 = 0
    if(a == A1):
      right_spot1 += 1
    elif(a == B1 or a == C1 or a == D1 or a ==E1):
      wrong_spot1 += 1
    if(b == B1):
      right_spot1 += 1
    elif(b == A1 or b == C1 or b == D1 or b == E1):
      wrong_spot1 += 1
    if(c == C1):
      right_spot1 += 1
    elif(c == A1 or c == B1 or c == D1 or c == E1):
      wrong_spot1 += 1
    if(d == D1):
      right_spot1 += 1
    elif(d == A1 or d == B1 or d == C1 or d == E1):
      wrong_spot1 += 1
    if(e == E1):
      right_spot1 += 1
    elif(e == A1 or e == B1 or e == C1 or e == D1) :
      wrong_spot1 += 1
    if right_spot1 == 5:
      return('You win!') 
    else:
      print('letters in the right spot:')
      print(right_spot1)
      print('letters in the word but not in the right spot:')
      print(wrong_spot1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



def first_guess():
  guess = input('Guess the five letter word!\n')
  if len(guess) != 5:
    print('word has to be 5 letters!')
    guess = input() 
    guess = (' '.join(guess))
    a,b,c,d,e = word.split()
    A,B,C,D,E = guess.split()
    right_spot = 0
    wrong_spot = 0
    if(a == A):
      right_spot += 1
    elif(a == B or a == C or a == D or a ==E):
      wrong_spot += 1
    if(b == B):
      right_spot += 1
    elif(b == A or b == C or b == D or b == E):
      wrong_spot += 1
    if(c == C):
      right_spot += 1
    elif(c == A or c == B or c == D or c == E):
      wrong_spot += 1
    if(d == D):
      right_spot += 1
    elif(d == A or d == B or d == C or d == E):
      wrong_spot += 1
    if(e == E):
      right_spot += 1
    elif(e == A or e == B or e == C or e == D) :
      wrong_spot += 1
    if (right_spot == 5):
      print('You won in 1 try! Wow!')
    else:
      print('letters in the right spot:')
      print(right_spot)
      print('letters in the word but not in the right spot:')
      print(wrong_spot)
    
  else:
    guess = (' '.join(guess))
    a,b,c,d,e = word.split()
    A,B,C,D,E = guess.split()
    right_spot = 0
    wrong_spot = 0
    if(a == A):
      right_spot += 1
    elif(a == B or a == C or a == D or a ==E):
      wrong_spot += 1
    if(b == B):
      right_spot += 1
    elif(b == A or b == C or b == D or b == E):
      wrong_spot += 1
    if(c == C):
      right_spot += 1
    elif(c == A or c == B or c == D or c == E):
      wrong_spot += 1
    if(d == D):
      right_spot += 1
    elif(d == A or d == B or d == C or d == E):
      wrong_spot += 1
    if(e == E):
      right_spot += 1
    elif(e == A or e == B or e == C or e == D) :
      wrong_spot += 1
    if (right_spot == 5):
      print('You won in 1 try! Wow!')
    else:
      print('letters in the right spot:')
      print(right_spot)
      print('letters in the word but not in the right spot:')
      print(wrong_spot)
  print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

first_guess()

while difficulty < 6:
  print('you have', int(-2 * difficulty + 12), 'guesses left')
  guesses()  
  difficulty = difficulty + 0.5
  print('you have', int(-2 * difficulty + 12), 'guesses left')
  guesses()
  difficulty = difficulty + 0.5
print('You lost! Word was:', word1)






