import numpy as np
from keras.models import load_model

def getstate(copy):
    state = 0
    for i, letter in enumerate(copy):
        if letter == " ":
            state = state + 0
        elif letter == "X":
            state = state + pow(3, i)
        else:
            state = state + 2 * pow(3, i)
    return int(state)


def getstateArray(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(r)

    while len(nums) < 9:
        nums.append(0.0)
    return nums


'''
state = getstate(["O", " ", " ", " ", " ", " ", " ", " ", " "])
print("State =", state)
print("Array = ", getstateArray(state))
'''

state = getstateArray(5)
print(state)
print(getstate(state))
model = load_model("NeuralNetworkModel.h5")
Row = model.predict(np.array(state).reshape(1, 9))
print(Row[0])
