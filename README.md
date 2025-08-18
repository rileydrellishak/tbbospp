# RD's Remixes of "The Big Book of Small Python Projects" by Al Sweigart
[Project Descriptions](https://inventwithpython.com/bigbookpython/)
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
    * Updating the comparison for hints - must account for repeated digits.
      * if secret is 300 and guess is 333, I want it to say Fermi; not Fermi Pico Pico
</details>

### :birthday: [Birthday Paradox](/birthday_paradox.py)
### :closed_lock_with_key: [Caesar Cipher](/ccipher.py)
### :lock: [Caesar Hacker](/chacker.py)
### :game_die: [Cho Han](/cho_han.py)
### :newspaper: [Clickbait Headline Generator](/clickbait_headline_generator.py)
### :1234: [Collatz Sequence](/collatz_sequence.py)
### :mag_right: [Factor Finder](/factor_finder.py)

## Tier 2: Intermediate

## Tier 3: Advanced
