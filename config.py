import os

BATTERY_PERCENTAGE_THRESHOLD = os.environ.get('BATTERY_PERCENTAGE_THRESHOLD', 3)  # percent
CHECK_INTERVAL = os.environ.get('CHECK_INTERVAL', 5)  # minutes
