<!DOCTYPE html>
<html lang="en">

<div class="top">
    <a href="https://github.com/RealMaskedTitan/python-projects/tree/master">Home   </a>
    <a href="https://github.com/RealMaskedTitan/python-projects/tree/master/music%20trivia">Music Trivia    </a>
    <a href="https://github.com/RealMaskedTitan/python-projects/tree/master/house-inventory">House Inventory    </a>
    <a href="https://github.com/RealMaskedTitan/python-projects/tree/master/menu-maker">Menu Maker  </a>
    <a href="https://github.com/RealMaskedTitan/python-projects/tree/master/bio">About Me   </a>
  </div>
      <div>

<h1>MaskedTitan's Python projects!</h1>
<p1>Welcome to my Github repo about my python projects, where as you can tell I store my python projects</p1>
<br>
<h2>house inventory</h2>
<div>
    This python program is made to keep track of items with features such as: the date of the item being registered into the                                database any notes for the items are saved the location of the item is recorded
    This program uses the python datetime module to record the date it also uses the json module to interact with the json database file
</div>
<br>
<h2>Music Trivia</h2>
<div>
    music trivia This python program is designed to test a person's knowledge about music names.

login details: Username : MaskedTitan Password : 1234

The game rules:

A random song name and artist are chosen.
The artist and the fi rst letter of each word in the song title are displayed.
The user has two chances to guess the name of the song.
If the user guesses the answer correctly the fi rst time, they score 3 points. If the user guesses the answer correctly the second time they score 1 point. The game repeats.
The game ends when a player guesses the song name incorrectly the second time
This program is designed to:

Allows a player to enter their details, which are then authenticated to ensure that they are an authorised player.
Stores a list of song names and artists in an external file.
Selects a song from the file, displaying the artist and the first letter of each word of the song title.
Allows the user up to two chances to guess the name of the song, stopping the game if they guess a song incorrectly on the second chance.
If the guess is correct, add the points to the player’s score depending on the number of guesses.
Displays the number of points the player has when the game ends.
Stores the name of the player and their score in an external file.
Displays the score and player name of the top 5 winning scores from the external file.
</div>

<h2>Menu Maker</h2>

    a python module to output menus
    example of this output is:
    ------------
    | thanks   |
    | for      |
    | using    |
    | this     |
    ------------
    this can be achieved by running this command:
    make_menu(['thanks', 'for', 'using', 'this'])
