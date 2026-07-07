# prompts the user for their date of birth in "YYYY-MM-DD" format
# print out how many full years + weeks of this year of life has been passed
# assume that the user was born at midnight (i.e., 00:00:00) on that date
# And assume that the current time is also midnight
# In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date
# Exit via sys.exi if the user does not input a date in YYYY-MM-DD format => "Invalid date"
# Ensure that your program will not raise any exceptions


from datetime import date, datetime
import sys
from colorama import init, Fore, Style


init(autoreset=True)


def main():
    birth = input("Date of Birth: ")

    try:
        birth_date = extract_date(birth)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()

    if birth_date > today:
        sys.exit("Invalid date")

    years, weeks = calculate_age(birth_date, today)

    print(style(years, weeks))


def extract_date(date_str):
    birth_date = datetime.strptime(
        date_str, "%Y-%m-%d").date()  # to turn into date format
    return birth_date


def calculate_age(birth_date, today):
    # Completed years
    years = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1

    # Last birthday
    birthday_year = today.year

    try:
        last_birthday = birth_date.replace(year=birthday_year)
    except ValueError:
        # Handle February 29 in non-leap years
        last_birthday = date(birthday_year, 2, 28)

    if last_birthday > today:
        birthday_year -= 1

        try:
            last_birthday = birth_date.replace(year=birthday_year)
        except ValueError:
            last_birthday = date(birthday_year, 2, 28)

    weeks = (today - last_birthday).days // 7

    return years, weeks


def style(years, weeks):
    filled = "■" * weeks
    empty = "□" * (52 - weeks)

    return f"""
        {Fore.YELLOW}{Style.BRIGHT}
        ╔══════════════════════════════════════════════════════╗
        ║                🕯️ MEMENTO MORI CALENDAR               ║
        ╚══════════════════════════════════════════════════════╝
        {Style.RESET_ALL}

        {Fore.CYAN}{Style.BRIGHT}Current Position{Style.RESET_ALL}

        {Fore.WHITE}Year : {Fore.GREEN}{years}
        {Fore.WHITE}Week : {Fore.GREEN}{weeks} / 52

        {Fore.GREEN}{filled}{Fore.LIGHTBLACK_EX}{empty}

        {Fore.YELLOW}Fill row {years} through week {weeks}.{Style.RESET_ALL}

        {Fore.GREEN} 💠 It is not that we have a short time to live, but that we waste much of it. 💠{Style.RESET_ALL}
    """


if __name__ == "__main__":
    main()
