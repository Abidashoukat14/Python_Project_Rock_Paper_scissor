# Python_Project_Rock_Paper_scissor

# Introduction
This is a Python implementation of the classic **Rock-Paper-Scissors game**. The player competes against the computer, which makes random moves. The project is designed to be simple and fun, with an interactive and user-friendly interface.

# How the Game Works

The game follows the standard rules of **Rock-Paper-Scissors**:

**Rock** (0) beats **Scissors** (2).<br>

**Paper** (1) beats **Rock** (0).<br>

**Scissors** (2) beats **Paper** (1).<br>

# Features

**1. Interactive Gameplay**: The player inputs their choice of Rock, Paper, or Scissors, while the computer randomly selects its move.<br>

**2. Game Rules Display**: If the player is unfamiliar with the rules, they are provided before starting the game.<br>

**3. Continue or Quit**: After each round, the player can choose to keep playing or quit the game.<br>

**4. Error Handling**: The program ensures valid input from the player and handles errors appropriately.<br>

# How to Play

**1.** When the game starts, you'll be asked if you know the rules. If you answer "no," the rules will be displayed.<br>

**2.** Choose your move by entering: <br>
          `0` for **rock**<br>
          `1` for **Paper**<br>
          `2` for **Scissors**<br>
          
**3.** The computer will also select a move, and the result of the round will be displayed.<br>

**4.** After each round, you can either continue playing or quit the game.<br>

# Code Breakdown 

 **1. random.randint(0,2)**: Generates a random number between 0 and 2 for the computer's choice.<br>

**2. Game Rules Check**: Based on the player's and the computer's choices, the game determines who wins or if the match is a draw.<br>

**3. Quit or Continue**: Players are prompted after each round to either quit the game or keep playing.<br>

# Requirements

   `Python 3.x`

# Running the Game

**1. Clone this repository or download the code.**

**2. Run the script using Python:**


    `python rock_paper_scissors.py`

**3. Follow the on-screen prompts to play the game.**

# Example:

`
--------------------------------Welcome To the Game:---------------------------------

Do you know the rules of the game..?If Yes write 'yes' if No write 'no' : yes

---------------------------------Okay! Thats cool. You are incredible... Let's start the game.---------------------------------

                      Enter your Element.. '0' for Rock, '1' for Paper, '2' for Scissor: 0

         If you don't want to play, feel free to quit the Game by entering 'quit'. If not, enter 'not quit': not quit

This match is a draw.<br>

Computer choice: 0, You choice: 0.`

# Author

**Created by Abida.**

**Check out my GitHub for more projects: https://github.com/Abidashoukat14.**
