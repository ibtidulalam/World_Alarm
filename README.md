Location-based Alarm Notification App

Description:
This Python-based alarm notification app allows users to set location-based alarms and receive popup notifications on their Windows or macOS devices. The app supports both Windows and macOS platforms, providing a user-friendly way to schedule alarms for specific times in different time zones.

Features:

Cross-platform: The app works on both Windows and macOS, making it accessible to a wide range of users.

Location-Based Alarms: Users can set alarms for specific locations using the IANA Time Zone Identifiers, such as 'America/Toronto' or 'Europe/Madrid'.

Non-Second Sensitive: The app is hour and minute sensitive, allowing users to set alarms with a specified time without worrying about seconds.

Popup Notifications: Alarms trigger popup notifications on the user's device when the specified time is reached.

Customizable: Users can easily customize the location and time for their alarms by modifying a few variables in the script.

Requirements:

Python: Make sure you have Python installed on your system. The script is compatible with Python 3.x.

Required Python Libraries: Install the following Python libraries using pip:

pytz for handling time zones.
plyer for cross-platform notifications.
time for controlling the loop and timing.

Install these libraries by running the following commands:
pip install pytz
pip install plyer

How to Use:

Clone or download this repository to your local machine. Modify the location, alarm_hour, and alarm_minute variables in the script to set your desired location and alarm time.

Run the script using Python:
python alarm_notification.py

The app will continuously check the time, and when the specified alarm time is reached, a popup notification will appear on your device.

