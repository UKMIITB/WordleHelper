# WordleHelper
This script helps to solve wordle game in less than a minute, giving highly accurate suggestions

## How to use
1. On running the code it'll ask "Enter the number of character limit:"  
This is the word length of the game (Eg. For NYTimes Wordle it is 5)  

2. Then it'll ask "Enter the word number 1 : "  
This is the 1st word that you are expected to guess  
Preferably guess a word whose all characters are unique (Eg. horse)

3. Then it'll ask "Enter the color for word number 1 : "  
This you'll get when you actually enter the word guessed in actual game  
Assuming you guessed "horse" in the game & it returned the result as "black, yellow, yellow, black, green"  
Here "black" means wrong alphabet, "yellow" means correct alphabet but wrong position & "green" means correct alphabet and position  
So in this case for "Enter the color for word number 1 : ", the input should be byybg  

4. On entering color for word number 1, it'll give a list of words for next guess  
Pick any word from the list. Preferably pick word whose non green positions are distinct alphabets  
Also from the list, try to pick the word which is common

5. Enter the word picked in the game as well as input for "Enter the word number 2: "  
6. Enter the color combination obtained from the game on enter word 2 as input for "Enter the color for word number 2 :"
7. Code will again give out a list of word as suggestions. This time the list would be smaller than the one given out in Step 4  
8. Again repeat the steps, and you should be able to figureout the exact word
9. Just remember, from the suggested list of words given out by code always try to pick the most common word
