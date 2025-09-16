from fitness_data_observers import FitnessDataObservers

class ProgressLogger(FitnessDataObservers):
    def data_action(self, data):
        with open("fitness_progress.log", "a") as log_file:
            log_file.write(
                "Steps: {}, Calories: {}, Active Minutes: {}\n".format(
                    data.getSteps(), data.getCalories(), data.getActiveMinutes()
                )
            )
        print("Progress logged to fitness_progress.log")
