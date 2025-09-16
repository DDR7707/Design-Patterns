from fitness_data_subject import FitnessDataSubject

class FitnessData(FitnessDataSubject):
    def __init__(self):
        super().__init__()
        self.steps = 0
        self.calories = 0
        self.active_minutes = 0

    def newDataPushed(self, steps, calories, active_minutes):
        self.update_steps(steps)
        self.update_calories(calories)
        self.update_active_minutes(active_minutes)
        self.notify_observers()

    def add_observer(self, name, location):
        self.observers[name] = location

    def remove_observer(self, name):
        try:
            del self.observers[name]
        except Exception:
            pass

    def notify_observers(self):
        for observer in self.observers.values():
            observer.data_action(self)

    def update_steps(self, steps):
        self.steps = steps

    def update_calories(self, calories):
        self.calories = calories

    def update_active_minutes(self, active_minutes):
        self.active_minutes = active_minutes

    def getSteps(self):
        return self.steps

    def getCalories(self):
        return self.calories

    def getActiveMinutes(self):
        return self.active_minutes
