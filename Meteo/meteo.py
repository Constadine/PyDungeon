import random
import time

seasons = ('winter', 'spring', 'summer', 'autumn')
weather = ('sunny', 'rainy', 'cloudy', 'partly cloudy')
temperature = ('frosty', 'cold', 'mild', 'warm', 'hot', 'blazing')


def get_var_value(filename="varstore.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


day_of_year = get_var_value()
print(f'This is the {day_of_year} day of the year.')

time.sleep(1)

# random weather and temp, print proper meteo message

if day_of_year < 90:
    random_temp = random.randint(-10, 20)
    random_weather_index = random.randint(0, 3)
    print(f"It's {seasons[0].capitalize()}...")
    random_weather = weather[random_weather_index]
    print(random_weather, random_temp)
    if random_temp < -2:
        if random_weather == 'sunny':
            print(
                f"The weather will be {random_weather}, but quite {temperature[0]} at {random_temp} C")
        elif random_weather == 'rainy':
            print(
                f"The weather will be {random_weather} with a high possibility of snowing, because it's going to be {temperature[0]} at {random_temp} C")
        elif random_weather == 'cloudy':
            print(f"The weather will be {random_weather}")  # continue here
elif day_of_year < 180:
    random_temp = random.randint(0, 26)
    print(f"It's {seasons[1].capitalize}...")
elif day_of_year < 270:
    random_temp = random.randint(18, 42)
    print(f"It's {seasons[2].capitalize}...")
else:
    random_temp = random.randint(0, 28)
    print(f"It's {seasons[3].capitalize}...")
