import datetime

data = [
    {"name": "Bill Gates", "birthday": datetime.date(1955, 10, 28)},
    {"name": "Kostiantyn Romanchuk", "birthday": datetime.date(1985, 5, 5)},
    {"name": "Nikolaj Romancuk", "birthday": datetime.date(2007, 5, 17)},
    {"name": "Anton Romancuk", "birthday": datetime.date(2005, 12, 20)},
    {"name": "Test User", "birthday": datetime.date(1990, 10, 7)},
    {"name": "Test User2", "birthday": datetime.date(1990, 10, 8)},
    {"name": "Test User3", "birthday": datetime.date(1990, 10, 12)},
    {"name": "Test User4", "birthday": datetime.date(1990, 10, 14)}
]

def get_birthdays_one_week_away(data):
    current_date = datetime.date.today()
    people_with_birthday_next_week = []
    people_with_birthday_next_week_dict = {}

    for person in data:
        person_birthday = person["birthday"]
        birthday_this_year = person_birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = person_birthday.replace(year=current_date.year + 1)

        delta_weeks = (birthday_this_year - current_date).days // 7

        if delta_weeks == 1 and not (birthday_this_year.strftime('%A') == 'Saturday' or birthday_this_year.strftime('%A') == 'Sunday'):
            people_with_birthday_next_week.append([birthday_this_year.strftime('%A'), person['name']])
        elif delta_weeks == 0 and (birthday_this_year.strftime('%A') == 'Saturday' or birthday_this_year.strftime('%A') == 'Sunday'):
            people_with_birthday_next_week.append(["Monday", person['name']])

    for people in people_with_birthday_next_week:           
        day = people[0]
        if day not in people_with_birthday_next_week_dict:
            people_with_birthday_next_week_dict[day] = []
        people_with_birthday_next_week_dict[day].append(people[1])

    return people_with_birthday_next_week_dict

# Example usage:
birthdays_next_week_dict = get_birthdays_one_week_away(data)
print("People with birthdays one week away (grouped by day):")
for day, people in birthdays_next_week_dict.items():
    print(f"{day}: {', '.join(people)}")
