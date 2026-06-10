import json
import matplotlib.pyplot as plt

def visualize():
    with open("../data/weather_data.json", "r") as f:
        data = json.load(f)

    labels = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]
    values = [data["temperature"], data["humidity"], data["pressure"]]

    plt.figure()
    plt.bar(labels, values)

    plt.title(f"Weather Data for {data['city']}")
    plt.xlabel("Parameters")
    plt.ylabel("Values")

    plt.savefig("../dashboard.png")
    plt.show()

if __name__ == "__main__":
    visualize()
