import random
# from CMAC import CMAC
import numpy as np

from QTableDataHandler import DataHandler

'''-------------------------------------------------
QTable has 19683 rows with index 0-19682 and 9 columns 0-8
-------------------------------------------------'''


class QLearning:
    def __init__(self, alpha=0.3, gamma=0.9, epsilon=0.5):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        self.oldAction = 0
        self.oldState = 0
        self.data = DataHandler()

    def SaveQ(self):
        self.data.SaveQ()

    def updateQ(self, next_state, next_possiblemoves, state, action, reward, gameIsPlaying, message="Updating"):
        if gameIsPlaying == False:
            newQ = reward
            print(message, "Reward for state:", state, " action:", action, " is ", reward)
        else:
            print(
                "{} next_state:{}, next_action:{}, state:{}, action:{}".format(message, next_state, next_possiblemoves,
                                                                               state, action))
            highestQ = np.max(np.take(self.data.getQRow(next_state), next_possiblemoves))
            oldQ = self.data.getQ(state, action)
            newQ = reward + self.gamma * highestQ
            change = self.alpha * (newQ - oldQ)
            newQ = oldQ + change
        self.data.addorUpdateData(state, action, newQ)

    def getmove(self, state, possiblemoves):
        if self.epsilon > np.random.uniform():
            return random.choice(possiblemoves)
        else:
            print("State is", state)
            print(self.data.getQRow(state))

            return possiblemoves[np.argmax(np.take(self.data.getQRow(state), possiblemoves))]
