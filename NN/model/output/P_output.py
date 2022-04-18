
from keras.models import Sequential
from keras.layers import Dense


class P_output:
    def __init__(self, p_id=""):
        self.p_id = p_id

    def baseline_model(self, input_dim):
        # Create model here
        model = Sequential()
        model.add(Dense(15, input_dim=input_dim, activation='relu'))
        model.add(Dense(15, activation='relu'))
        model.add(Dense(11, activation='softmax'))
        model.compile(loss='categorical_crossentropy',
                      optimizer='adam', metrics=['accuracy'])
        return model
