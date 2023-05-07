class WeeklyPlan:

    def __init__(self):
        self.day_plan = {}

    def add_task(self, day, task):
        self.day_plan[day] = task

    def get_task(self, day):
        return self.day_plan[day]

    def edit_task(self, day, new_task):
        self.day_plan[day] = new_task

    def save_plan(self):
        # Import the json module.
        import json

        # Create a dictionary to store the weekly plan.
        weekly_plan_dict = {}

        for day, task in self.day_plan.items():
            weekly_plan_dict[day] = task

        # Use the json.dump() function to dump the dictionary to a file.
        with open("weekly_plan.json", "w") as f:
            json.dump(weekly_plan_dict, f, indent=4)

        # Save the file.
        f.close()

def main():

    # Create an instance of the WeeklyPlan class.
    weekly_plan = WeeklyPlan()

    # Add tasks to the weekly plan.
    weekly_plan.add_task("mon", "Go to work")
    weekly_plan.add_task("tue", "Go to the gym")
    weekly_plan.add_task("wed", "Meet with friends")
    weekly_plan.add_task("thu", "Go to the grocery store")
    weekly_plan.add_task("fri", "Relax")
    weekly_plan.add_task("sat", "Go out with friends")
    weekly_plan.add_task("sun", "Watch a movie")

    # Get a task from the weekly plan.
    task = weekly_plan.get_task("mon")
    print(task)

    # Edit a task in the weekly plan.
    weekly_plan.edit_task("fri", "Go shopping")

    # Save the weekly plan to storage.
    weekly_plan.save_plan()

if __name__ == "__main__":

    main()
