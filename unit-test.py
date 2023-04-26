valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
tasks_list = []
key = True
while key:
    day_prompt = input("What day do you want to edit? (Mon, Tue, Wed, Thu, Fri, Sat, Sun) ").lower()
    if day_prompt not in valid_days:
        print('invalid, try again')
        continue
    elif day_prompt == day:
        new_task = input("What is your new task for {}? ".format(day)).lower()
        tasks_list.append(new_task)
        key = False
    elif day_prompt == 'no':
        key = False
