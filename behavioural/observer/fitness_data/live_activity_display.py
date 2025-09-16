from fitness_data_observers import FitnessDataObservers

class LiveActivityDisplay(FitnessDataObservers):
    def data_action(self, data):
        print(
            "Live data: Steps: {}, Calories: {}, Active Minutes: {}".format(
                data.getSteps(), data.getCalories(), data.getActiveMinutes()
            )
        )
