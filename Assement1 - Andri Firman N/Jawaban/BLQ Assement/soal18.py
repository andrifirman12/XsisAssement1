def calculate_duration(input_hours, input_calories, input_time):
    exercise_duration = 0
    minutes_in_an_hour = 60
    for i in range(len(input_hours)):
        time_difference = input_time - input_hours[i]
        exercise_duration += 0.1 * input_calories[i] * time_difference

    return exercise_duration / minutes_in_an_hour


def case_burning_calories(exercise_duration):
    return (100 * exercise_duration * 2) + 500


def burning_calories(input_hours, input_calories, input_time):
    duration = calculate_duration(input_hours, input_calories, input_time)
    print("Donna needs", case_burning_calories(duration), "cc of water")


input_hours = [9, 13, 15, 17]
input_calories = [30, 20, 50, 80]
input_time = 18

div = "-------------------------------"
print(div)
burning_calories(input_hours, input_calories, input_time)
print(div)
