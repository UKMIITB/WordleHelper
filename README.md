# WordleHelper

This script provides api endpoints for getting highly accurate guesses for wordle game

## How to use

1. The base url for the api endpoint is `https://wordle-helper-app.herokuapp.com/`  
   On hitting this url, it'll just return text `Welcome to Wordle Helper API`

2. The main url for getting predictions results is `https://wordle-helper-app.herokuapp.com/suggestion`  
   Following points needs to be considered while accessing this endpoint  
   Request Type: POST  
   Header -> Content-Type: application/json  
   Body: {  
   "guess_word": "beast",  
   "guess_word_result": "yyggb",  
   "iteration": 2,  
   "word_list": ["abc", "def", "ghi"]  
   }  
   `guess_word`: Is the word that was actually guessed in wordle game  
   `guess_word_result`: Is the result of the guess word from wordle game. b is for black, y for yellow & g for green  
   `iteration`: The current iteration going on. Make sure it starts with 1  
   `word_list`: For each request sent, server would send back list of possible result words. Pass this list as word_list for next guess  
   For `iteration`= 1, `word_list` should be an empty list

3. Response from API: {  
   "status": 200,  
   "suggestion_result": [
   "boral",
   "coral",
   "goral"
   ]  
   }

   User should pick one word from `suggestion_result`, preferably word which is a common word & with distinct characters.  
   For next guess, while making API call, result of `suggestion_result` should be sent as `word_list`

4. If the 1st request is sent with `x` as word length then its upto frontend user to ensure all subsequent request are for same word length & that `guess_word_result` is also of same length as `x`. If this is not followed, API might return error response

5. A sample web UI is added in this project in the folder frontend. To run this, you can clone this project, go to `frontend/src/App.js` in terminal and run `npm start`

6. On running the code it'll have 2 input field. Enter the guess & Enter the response from wordle  
   The 1st guess should come from user, then enter that word in `guess` field & that same word in wordle game and the output from wordle game should be added in `Enter the response from wordle` field and press `Submit`

7. It'll return list of possible words for next guess. Pick any one word from this list, preferably word which is common & has distinct characters and enter the same as next guess word in UI as well in wordle game & the result of wordle in `response` field. The next set of suggestions would keep on shrinking and quickly reaching to exact word in few iterations

8. Just remember, from the suggested list of words given out by code always try to pick the most common word
