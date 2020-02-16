import numpy as np


class DataHandler:
    def __init__(self):
        self.data = np.genfromtxt('QTableMini.csv', delimiter=',')

    def SaveQ(self):
        print("SAVING QTABLE")
        np.savetxt("QTableMini.csv", self.data, delimiter=",")

    def addorUpdateData(self, state, action, newQ):
        if np.array(np.where(self.data[:, 0] == state)).size != 0:
            state_row = np.where(self.data[:, 0] == state)
        else:
            new_row = np.where(self.data[:, 0] == 0.11)
            First_new_row = new_row[0][0]
            self.data[First_new_row][0] = state

            state_row = np.where(self.data[:, 0] == state)
            print("State Row: ", state_row[0])
        self.data[int(state_row[0])][action + 1] = newQ

    def getQ(self, state, action):
        if np.array(np.where(self.data[:, 0] == state)).size != 0:
            if state == 0:
                state_row = [1]
            else:
                state_row = np.where(self.data[:, 0] == state)
            print("State Row: ", state_row)
            return self.data[int(state_row[0])][action + 1]
        else:
            return 0

    def getQRow(self, state):
        if np.array(np.where(self.data[:, 0] == state)).size != 0:
            Row = self.data[np.where(self.data[:, 0] == state)]
            Row = Row[0][1:]
            return Row
        else:
            return np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])

    def getstateArray(self, i):
        n = self.data[i + 1][0]
        if n == 0:
            return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(r)

        while len(nums) < 9:
            nums.append(0.0)
        return nums

    def getQArray(self, i):
        return self.data[i + 1][1:]
