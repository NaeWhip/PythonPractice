import calendar

def valid_date(use_date):

    # Counts slashes and prompts an error if it's not the correct date format
    if use_date.count("/") != 2:
        print("Error: Date must be in mm/dd/yyyy format with slashes.")
        return None

    # Separates spaces with slashes
    date_format = use_date.split("/")

    # Formats the date and prompts an error when not a number
    try:
        date_month = int(date_format[0])
        date_day = int(date_format[1])
        date_year = int(date_format[2])

    except ValueError:
        print("Error: Date must be in numbers.")
        return None

    # Enforces an error when numbers doesn't meet the date requirement
    if (date_month < 1 or date_month > 12):
        print("Error: Month must be between 1 and 12.")
        return None
    if (date_day < 1 or date_day > 31):
        print("Error: Day must be between 1 and 31.")
        return None

    # Returns the date format
    return date_month, date_day, date_year

def main():

    # Loops until user enters the correct date format
    while True:

        # Prompts user to enter a date
        user_date_input = input("Enter a date in the format mm/dd/yyyy: ")

        # Passes the valid_date function
        date_result = valid_date(user_date_input)

        if date_result is not None: 
            break

    date_month, date_day, date_year = date_result

    # Converts month into english name
    month_name = calendar.month_name[date_month]

    # Outputs the users input in correct date format
    print(f'{month_name} {date_day}, {date_year}')


# Calls the main function
if __name__ == "__main__":
    main()


    

