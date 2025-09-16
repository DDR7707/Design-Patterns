Imagine you're developing a Fitness Tracker App that connects to a wearable device and receives real-time fitness data.

This data includes:

👣 Steps taken

⏱️ Active minutes

🔥 Calories burned

Whenever new data is received from the device, it gets pushed into a central object — let’s call it FitnessData.

Now, multiple modules within your app need to react to these updates:
LiveActivityDisplay
Displays real-time stats (e.g., step count, active minutes) on the app's dashboard.

ProgressLogger
Periodically logs fitness data to a database or file for historical trend analysis.

NotificationService
Sends alerts to the user, such as:

"🎉 Goal achieved!" when they reach 10,000 steps.

"⏳ Time to move!" if they’ve been inactive for too long.

In a simple approach, the FitnessData object directly holds and manages references to all its dependent modules.
