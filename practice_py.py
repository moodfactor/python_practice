import time

def get_day_plan():

    day_plan = {}

    for day in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]:

        task = input("What is your task for {}? ".format(day)).lower()

        if task == "":
            continue

        day_plan[day] = task

    return day_plan

def show_weekly_plan(day_plan):

    print("Your weekly plan:")

    for day, task in day_plan.items():

        print("  * {}: {}".format(day.capitalize(), task))

def edit_day_plan(day_plan):

    valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    while True:

        day = input("What day do you want to edit? (Mon, Tue, Wed, Thu, Fri, Sat, Sun) ").lower()

        if day not in valid_days:
            print("Invalid day. Please try again.")
            continue

        elif day in valid_days:
            new_task = input("What is your new task for {}? ".format(day)).lower()
            day_plan[day]+= f', {new_task}'
            break

        elif new_task == "":
            break

        day_plan[day] = new_task

    return day_plan

def main():

    day_plan = get_day_plan()

    while True:

        show_weekly_plan(day_plan)

        edit = input("Do you want to edit a day? (y/n) ").lower()

        if edit == "y":
            day_plan = edit_day_plan(day_plan)

        if edit == "n":
            break

    print("Your final schedule:")

    show_weekly_plan(day_plan)

if __name__ == "__main__":

    main()
    