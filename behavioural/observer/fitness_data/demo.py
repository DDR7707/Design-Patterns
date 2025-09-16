from fitness_data import FitnessData
from progress_logger import ProgressLogger
from notification_service import NotificationService
from live_activity_display import LiveActivityDisplay
from goal_remainder import GoalRemainder

class FitnessDataDemo:
    @staticmethod
    def run():
        fitness_data = FitnessData()

        logger = ProgressLogger()
        notification_service = NotificationService()
        live_display = LiveActivityDisplay()
        goal_remainder = GoalRemainder(10000, 500, 60)

        fitness_data.add_observer("Logger", logger)
        fitness_data.add_observer("NotificationService", notification_service)
        fitness_data.add_observer("LiveDisplay", live_display)
        fitness_data.add_observer("GoalRemainder", goal_remainder)

        fitness_data.newDataPushed(5000, 300, 45)
        fitness_data.newDataPushed(10000, 600, 90)
        fitness_data.newDataPushed(15000, 900, 120)
        fitness_data.remove_observer("Logger")
        fitness_data.newDataPushed(20000, 1200, 150)


if __name__ == '__main__':
    FitnessDataDemo.run()
