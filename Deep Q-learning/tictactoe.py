from game import Game

AI = "AI"
computer = "computer"
human = "human"

print("Hello!! You are gonna play 10 times against the AI.\n Let's see if you can tie all the 10 games")

Player1 = AI
Player2 = computer
episodes = 100

win, loss, tie = Game().play(player_1=Player1, player_2=Player2, episodes=episodes, alpha=1, gamma=0.9, epsilon=0)

word = "Won:" + str(win) + " Lost:" + str(loss) + " and Tied:" + str(tie) + " times"

print(word)

