from fitness_data_observers import FitnessDataObservers

class GoalRemainder(FitnessDataObservers):
    def __init__(self, goal_steps, goal_calories, goal_active_minutes):
        self.goal_steps = goal_steps
        self.goal_calories = goal_calories
        self.goal_active_minutes = goal_active_minutes

    def data_action(self, data):
        steps_remaining = self.goal_steps - data.getSteps()
        calories_remaining = self.goal_calories - data.getCalories()
        active_minutes_remaining = self.goal_active_minutes - data.getActiveMinutes()

        print(
            "Goal Remainder: Steps remaining: {}, Calories remaining: {}, "
            "Active Minutes remaining: {}".format(
                steps_remaining, calories_remaining, active_minutes_remaining
            )
        )
