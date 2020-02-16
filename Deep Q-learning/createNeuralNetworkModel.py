import numpy as np
from keras.layers import LeakyReLU
from keras.models import Sequential
from keras import optimizers, losses
from keras.layers.core import Dense, Dropout, Activation


class NeuralNetwork:
    def __init__(self):
        model = self.createModel("relu")
        model.save("NeuralNetworkModel.h5")

    def createModel(self, activationType):
        hiddenLayers = [10, 500, 100, 400, 50]
        model = Sequential()

        model.add(Dense(hiddenLayers[0], input_shape=(9,), init='lecun_uniform'))
        model.add(Activation(activationType))

        for index in range(1, len(hiddenLayers)):
            print("adding layer " + str(index))
            layerSize = hiddenLayers[index]
            model.add(Dense(layerSize, init='lecun_uniform'))
            model.add(Activation(activationType))

        model.add(Dense(9, init='lecun_uniform'))
        model.add(Activation("linear"))

        optimizer = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
        model.compile(loss=losses.mean_squared_error, optimizer=optimizer)
        model.summary()
        return model


if __name__ == "__main__":
    NeuralNetwork()
