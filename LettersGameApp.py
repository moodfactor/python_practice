from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.textinput import TextInput



class LetterGame(App):
    
    words = ["cat", "dog", "hat", "mat", "bat"]
    timer_label = Label(text="00:00")
    word_label = Label(text="")
    # Create a list of buttons for the letters of the word
    letter_buttons = []
    
    def __init__(self,words,timer_label,word_label, letter_buttons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.words = words
        self.timer_label = timer_label
        self.word_label = word_label
        self.letter_buttons = letter_buttons
    
    def build(self):
        # Create a grid layout
        layout = GridLayout(cols=3)

        # Add buttons for each letter of the alphabet
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            button = Button(text=letter, on_press=self.on_letter_press)
            button.bind(on_press=self.on_letter_press)
            layout.add_widget(button)

        # Create a label for the timer
        
        layout.add_widget(self.timer_label)

        # Start the timer
        Clock.schedule_interval(self.update_timer, 1)

        # Create a list of words

        # Create a label for the word
        
        layout.add_widget(self.word_label)

        
        for letter in self.words[0]:
            letter_button = Button(text=letter, on_press=self.on_letter_press)
            self.letter_buttons.append(letter_button)
            layout.add_widget(letter_button)

        return layout

    def on_letter_press(self, instance):
        # Get the letter that was pressed
        letter = instance.text

        # Check if the letter is in the word
        if letter in self.words[0]:
            # Remove the letter from the word
            self.words[0] = self.words[0].replace(letter, "")

            # If the word is empty, then the player has won
            if self.words[0] == "":
                self.root.remove_widget(self.word_label)
                for letter_button in self.letter_buttons:
                    self.root.remove_widget(letter_button)

                # Create a label to congratulate the player
                congratulations_label = Label(text="Congratulations!")
                self.root.add_widget(congratulations_label)

    def update_timer(self, dt):
        
        # Get the current time
        current_time = str(Clock.get_time())

        # Update the timer label
        self.timer_label.text = current_time


if __name__ == "__main__":
    LetterGame(words=["cat", "dog", "hat", "mat", "bat"],
               timer_label=Label(text="00:00"), 
               word_label=Label(text=""),
               letter_buttons=[],).run()