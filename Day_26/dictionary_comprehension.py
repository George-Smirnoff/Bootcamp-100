import random

def cel_far_converter(cel):
    return (cel * 9/5) + 32


def main():
    # Use Dict comprehension to create a dictionary of students with random score
    names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanore", "Freddie"]
    students_score = {student:random.randint(0, 100) for student in names_list}
    # print(students_score)


    # Filter students with score 60+
    passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
    print(passed_students)


    # TASKS
    # 1
    # Create a dict with word and its lenght
    sentence = "What is Airspeed Velocity of an Unladen Swallow?"
    result = {word:len(word) for word in sentence.split(' ')}
    print(result)


    # 2
    # Conwert Celsius to Fahrenheit
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "wednesday": 15,
        "thursDay": 14,
        "friday": 21,
        "saTURday": 22,
        "SUNday": 24
    }

    weather_f = {day.capitalize():cel_far_converter(tempr) for (day, tempr) in weather_c.items()}
    print(weather_f)


if __name__ == '__main__':
    main()