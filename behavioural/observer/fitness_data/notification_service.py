from fitness_data_observers import FitnessDataObservers

class NotificationService(FitnessDataObservers):
    def data_action(self, data):
        print(
            "Notification: You have completed {} steps, burned {} calories, and "
            "spent {} active minutes today!".format(
                data.getSteps(), data.getCalories(), data.getActiveMinutes()
            )
        )
