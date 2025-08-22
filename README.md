# RD's Remixes of "The Big Book of Small Python Projects" by Al Sweigart
[Project Tiers and Descriptions](\PROJECT_DESCRIPTIONS.md)
[Project Descriptions](https://inventwithpython.com/bigbookpython/)
[Tiers](https://chatgpt.com/s/t_68a8b84d16448191afc4eb0c6e2bf043)
[Pathways](https://chatgpt.com/s/t_68a8b86cbc748191bee9bd4fd720445e)
## Tier 1: Beginner
### :bagel: [Bagels](/bagels.py)
<details>
  <summary>Reflections</summary>
  
  * 08/17
    * Created a function set_secret_number() to create the random n-digit mystery number.
    * Created a function get_user_input to validate the type of input -- should be an n-digit number. Formats it as a list of individual numbers of n length upon validation.

  * 08/18
    * Realized I could more closely align to the single responsibility principle with the get_user_input function. I should make another function just to format the input. Made the function format_user_input(user_input).
    * Made a very simple version of comparing the user guess with the mystery number - it checks each item by index and constructs a list of strings. I will later convert this to a straight up string.
    * Created a helper function to determine whether the number was guessed based on contents of the hint string.
    * Created a helper function at the end to give user option to replay.
    * I asked [chat](https://chatgpt.com/share/68a38ee0-db8c-800b-925d-a7919dcad523) to review, gave following suggestions:
      * Change set_secret_number() so duplicate digits are not allowed
      * Randomizes the hint list every time
      * Refactors compare_guess_to_secret_number() to just produce final clue string, which in turn updates how to change still_playing helper function
  
  * 08/19
    * Wrote a helper function ask_replay to allow user to replay game.
    * Incorporated a way to check number of guesses left in a game
    * Put some new lines in displayed lines to enhance readability
</details>

### :birthday: [Birthday Paradox](/birthday_paradox.py)
<details>
  <summary>Reflections</summary>

  - 08/22
    - Started the file with the docstring
</details>

### :closed_lock_with_key: [Caesar Cipher](/ccipher.py)
<details>
  <summary>Reflections</summary>
  * 08/19
    * Added docstring description of problem from chat
</details>

### :game_die: [Cho Han](/cho_han.py)
<details>
  <summary>Reflections</summary>

  - 08/21
    - Inserted docstring to explain the game
    - Made helper functions to:
      - receive user bet
      - validate user bet
      - receive user prediction
      - validate user prediction
      - roll die
      - check sum of die
      - match die rolls with Japanese word
    - [Chat](https://chatgpt.com/share/68a744c0-4f54-800b-b794-c80749d6cb4b)
  - 08/22
    - Helper functions created:
      - check outcome against prediction
      - adjust purse based on outcome vs logic (T/F)
      - replay loop
      - game dialogue throughout
    - [Further polishing guidelines](https://chatgpt.com/s/t_68a89432a85081919bc5af2ea4114ba2)

</details>

### :1234: [Collatz Sequence](/collatz_sequence.py)
<details>
  <summary>Reflections</summary>

  * 08/19
    * Created two helper functions - one to get user input for starting number, another to validate that user input is a positive number.
    * I have the very basic version of the sequence creator done. I want to focus next on making helper functions to better align with the single responsibility principle. 
    * I made a ton of helper functions to make the run_collatz() function look like a recipe. This will help once I start getting some matplotlib into this to show the dotplot of steps (x) vs terms (y)
    * Helpful conversation with [chat](https://chatgpt.com/share/68a4a661-23a4-800b-9c43-f2590ee2215f) for guidance
  
  * 08/20
    * Made a virtual environment to install matplotlib for this project
    * Starting to make a dot plot to show step number (x) vs value of term (y)
    * Helper function made to set x and y axis -- list of indicies, list of terms
    * Makes a very simple dot plot! How cool is that?!?!
      * The axes depend on the length and max value of the sequence

</details>

### :mag_right: [Factor Finder](/factor_finder.py)
<details>
  <summary>Reflections</summary>
  
  - 08/22
    - Started file, added docstring to explain purpose.
    - helper functions for the following:
      - get user input
      - validate input
      - find factors, put into a list
      - format the list into a string
  
</details>

### :pig: [Pig Latin](/pig_latin.py)
<details>
  <summary>Reflections</summary>
  
  - 08/22
    - Added docstring to explain purpose
    - 
</details>