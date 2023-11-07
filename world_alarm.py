import datetime
import pytz
from plyer import notification
import time

def show_popup_notification(location, alarm_hour, alarm_minute):
    try:
        # Convert the alarm time to the specified timezone
        timezone = pytz.timezone(location)

        while True:
            now = datetime.datetime.now(timezone)
            if now.hour == alarm_hour and now.minute == alarm_minute:
                notification_title = "Alarm Notification"
                notification_message = f"It's time for your alarm in {location}"
                notification.notify(
                    title=notification_title,
                    message=notification_message,
                )
                # Sleep for a while to prevent constant checking
                time.sleep(60)  # Sleep for 60 seconds
            else:
                # Sleep to avoid continuous checking
                time.sleep(10)  # Sleep for 10 seconds
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    location = 'America/Toronto'  # Set the location to Madrid, Spain
    alarm_hour = 21  # Set the alarm hour to 6 PM
    alarm_minute = 58 # Set the alarm minute

    show_popup_notification(location, alarm_hour, alarm_minute)
