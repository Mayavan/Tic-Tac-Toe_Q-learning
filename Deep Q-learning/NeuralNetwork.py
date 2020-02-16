import numpy as np
from keras.models import load_model

from QTableDataHandler import DataHandler


class NeuralNetwork:
    def __init__(self):
        self.model = load_model("NeuralNetworkModel.h5")
        self.data = DataHandler()

    def trainModel(self):
        Input = np.array(self.data.getstateArray(0))
        Output = np.array(self.data.getQArray(0))
        print("Input: ", Input, " Output: ", Output)

        for i in range(1, 4408):
            state = np.array(self.data.getstateArray(i))
            QRow = np.array(self.data.getQArray(i))
            print("State: ", state, " QRow: ", QRow)
            Input = np.append(Input, np.array(state), axis=0)
            Output = np.append(Output, np.array(QRow), axis=0)
        Input = Input.reshape(4408, 9)
        Output = Output.reshape(4408, 9)
        print("Input: ", Input, " Output: ", Output)

        self.model.fit(Input, Output, epochs=50, verbose=2)
        self.model.save("NeuralNetworkModel.h5")

    def getmove(self, state, possiblemoves):
        print("State is", state)
        print("Q-Values are ", self.getQValues(state))

        return possiblemoves[np.argmax(np.take(self.getQValues(state) + 1, possiblemoves))]

    def getQValues(self, state):
        Row = self.model.predict(np.array(state).reshape(1, 9))
        return Row[0]


if __name__ == "__main__":
    NeuralNetwork().trainModel()
