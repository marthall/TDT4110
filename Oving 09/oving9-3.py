birthdays = {
        "22 nov": ["Lars", "Mathias"],
        "10 des": "elle"
}

def add_birthday_to_date(date, name):
    try:
        birthdays[date].append(name)
    except KeyError:
        birthdays[date] = name
    except AttributeError:
        birthdays[date] = [birthdays[date], name]


add_birthday_to_date("22 nov", "martin")
add_birthday_to_date("10 des", "kari")
add_birthday_to_date("5 nov", "per")
print(birthdays)
