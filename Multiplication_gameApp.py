from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock


class MultiplicationGame(App):
    score = 0
    current_problem = None
    current_time = None
    
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.problems = [
            (2, 3),
            (4, 5),
            (6, 7),
            (8, 9),
            (10, 11),
        ]

    def on_start(self):
        # Set the score to 0
        self.score = 0
        # Get the next problem
        self.current_problem = self.problems.pop()
        # Set the question label
        self.question_label.text = str(self.current_problem[0]) + " x " + str(self.current_problem[1])
        # Set the answer button
        self.answer_button.text = ""
        # Start the timer
        Clock.schedule_interval(self.update_timer, 1)
        # Set the current time
        self.current_time = Clock.get_time()
        # Set the score label
        self.score_label.text = str(self.score)
        # Set the current time label
        self.current_time_label.text = str(self.current_time)
        # Set the current time label
        self.current_time_label.text = str(self.current_time)
        # Set the current time label 
    
    def build(self):
        # Create a grid layout
        layout = GridLayout(cols=2)

        # Create a label for the question
        question_label = Label(text="")
        layout.add_widget(question_label)

        # Create a button for the answer
        answer_button = Button(text="")
        answer_button.bind(on_press=self.on_answer_press)
        layout.add_widget(answer_button)

        # Create a label for the score
        score_label = Label(text="0")
        layout.add_widget(score_label)

        # Create a list of multiplication problems
        

        # Get the next problem
        self.current_problem = self.problems.pop()

        # Set the question label
        self.on_start().question_label.text = str(self.current_problem[0]) + " x " + str(self.current_problem[1])

        # Set the answer button
        answer_button.text = ""

        # Start the timer
        Clock.schedule_interval(self.update_timer, 1)

        return layout

    def on_answer_press(self, instance):
        # Get the answer that the student entered
        answer = instance.text

        # Check if the answer is correct
        if answer == str(self.current_problem[0] * self.current_problem[1]):
            # The answer is correct, so add a point to the score
            self.score += 1

            # Get the next problem
            self.current_problem = self.problems.pop()

            # Set the question label
            self.on_start().question_label.text = str(self.current_problem[0]) + " x " + str(self.current_problem[1])

            # Set the answer button
            self.answer_button.text = ""
        else:
            # The answer is incorrect, so subtract a point from the score
            self.score -= 1

    def update_timer(self, dt):
        # Get the current time
        current_time = str(Clock.get_time())

        # Update the score label
        self.score_label.text = str(self.score)


if __name__ == "__main__":
    MultiplicationGame().run()