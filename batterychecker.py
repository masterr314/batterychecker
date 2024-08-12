import psutil


def main():
    battery = psutil.sensors_battery()

    if battery is None:
        print("No battery found.")
        exit()

    percentage = battery.percent
    print(f"Battery Percentage: {percentage}%")


if __name__ == "__main__":
    main()

