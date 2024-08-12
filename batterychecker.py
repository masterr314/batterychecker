import atexit

import psutil
from apscheduler.schedulers.blocking import BlockingScheduler
from loguru import logger
import beepy as beep
from config import *


scheduler = BlockingScheduler()

ALLOW_NOTIFICATIONS = True


@atexit.register
def _exit():
    logger.info('BatteryChecker stopped')


def battery_check():
    global ALLOW_NOTIFICATIONS

    battery = psutil.sensors_battery()

    if battery is None:
        logger.error("No battery found.")
        scheduler.shutdown()
        return

    percentage = battery.percent

    if percentage <= BATTERY_PERCENTAGE_THRESHOLD and ALLOW_NOTIFICATIONS:
        beep.beep(1)
        ALLOW_NOTIFICATIONS = False
    elif percentage > BATTERY_PERCENTAGE_THRESHOLD and not ALLOW_NOTIFICATIONS:
        ALLOW_NOTIFICATIONS = True

    logger.info(f"Battery Percentage: {percentage}%")


def main():
    scheduler.add_job(battery_check, 'interval', minutes=CHECK_INTERVAL)
    logger.info('BatteryChecker is running...')
    logger.info('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
