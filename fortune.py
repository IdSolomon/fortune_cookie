# Fortune Cookie Program

import random

name = "Xerxes"
fortune = ""
randomNumber = random.randint(0, 10)

if randomNumber == 0:
  fortune = "May you one day be carbon neutral."
elif randomNumber == 1:  
  fortune = "You have rice in your teeth."
elif randomNumber == 2:  
  fortune = "No snowflake feels responsible for an avalanche."
elif randomNumber == 3:  
  fortune ="You can only connect the dots looking backwards."
elif randomNumber == 4:  
  fortune ="The fortune you seek is in another cookie."
elif randomNumber == 5:  
  fortune ="Damned if you do. Damned if you don't."
elif randomNumber == 6:  
  fortune ="Today you're an adult. Tomorrow you're screwed."
elif randomNumber == 7:  
  fortune ="Fortune favors the bold. Depending on the fortune."
elif randomNumber == 8:  
  fortune ="You will find a way. That is, if life finds it first."
elif randomNumber == 9:  
  fortune ="Do or do not. There is no try."
elif randomNumber == 10:  
  fortune ="No cookie. No cry."

print(name + " opens fortune cookie to reveal: " + fortune)
