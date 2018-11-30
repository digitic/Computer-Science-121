Game: Danganronpa - Darkshift
Creators: Zhengyao Gu, Casey Harris

Play: A murder mystery game, featuring three modes of play. First is Free Time, where your character can explore the school, find coins, and talk to the other students. After talking to two people (or waiting twice), the game shifts into the investigation of a dead body. This is similar to Free Time, except that the player can now gather and investigate evidence. Once all evidence is collected, the game moves to the trial, which is a series of logic puzzles using the evidence you had collected to figure out the killer.

Features (Points):
Me command 2 - Players can inspect their credibility score and missing pieces of evidence.
Bigger world 2 - Rooms with unique names, and a bigger overworld.
Inspect command 2 - Able to review a piece of evidence to remember what its description is.
player attributes 3 - Player has “credibility” in place of health, and also tracks amount of money carried. Also has a penalty stat that impacts credibility lost for repeated failures.
regeneration 2 - When getting a question right in trial, the player regenerates 4% credibility if that wouldn’t set them over 100%.
Healing items 2 - Healing potions available in the shop to restore credibility.
Wait 2 - Wait in Free Time to pass time.
Victory condition 3 - Get to the end of the trial to win. Lose all your credibility to lose.
Loot 3 - Coins from events around the school in Free Time.
characters 4 - Other students to interact with, a cast of six other characters!
Special rooms(shop) 3 - A shop room where you can buy healing potions in Free Time or Investigation
Command abbreviations 2 - commands plus a number instead of having to write out a whole word.
Currency 4 - Coins. Not too much to say about this. Can be earned by Free Time events.
Map 3 - An ASCII map of the school.
Saving the game 10 - The game saves the player’s place in the trial and their current credibility.
File read & write 3 - The trial’s text is in a text file, and we use a read algorithm to turn it into the trial as it’s printed.

    Point total: 50


Known bugs:
Game will crash if you try to use a non-numeric second word in a Free Time or Investigation command.

Known misbehaviors:
Game can’t save before trial.
Trial commands rely on being numeric to progress, so it is possible for someone to skip refuting or agreeing. This defaults to counting as a refute.
Not exactly a misbehavior, but there are a few weak points of logic in the trial and I’m sorry.
When in trial, the game “forgets” that you picked up any evidence, so the me command says you are still missing evidence. Has no effect other than visual.

Project Work Division:
Yao:
Saving the game
Shop/Currency/Healing items
File reading algorithm
Work to modify existing code in main, monster (now character) and item (now evidence) files.
Trial class revisions

Casey:
Writing text files
Events/Free Time mode
Switching between game states (Free Time, Investigation, Trial)
Regeneration/Penalty
Wait/Victory condition
Trial class creation
