import tkinter as tk
import random
import time
from config import MIN_NUMBER, MAX_NUMBER, NUMBERS_TO_ASK, REMOVE_ZERO

class NumberGuessingGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Number Guessing Game")
        self.window.geometry("500x400")
        
        self.numbers_selected = []
        self.current_question = 0
        
        # Title
        self.title_label = tk.Label(window, text="Let me guess your number!", font=("Arial", 16))
        self.title_label.pack(pady=(20, 10))
        
        # Instructions
        self.instruction_label = tk.Label(
            window, 
            text=f"I'll ask for {NUMBERS_TO_ASK} numbers, then I'll guess the next one you think of.\n"
                 f"Enter numbers between {MIN_NUMBER} and {MAX_NUMBER}",
            font=("Arial", 12)
        )
        self.instruction_label.pack(pady=(5, 20))
        
        # Question label
        self.question_label = tk.Label(window, text=f"Enter number {self.current_question + 1}:", font=("Arial", 12))
        self.question_label.pack(pady=(10, 5))
        
        # Number input
        self.number_var = tk.StringVar()
        self.number_entry = tk.Entry(window, textvariable=self.number_var, font=("Arial", 32), justify='center', width=5)
        self.number_entry.pack(pady=10)
        self.number_entry.focus()
        
        # Submit button
        self.submit_button = tk.Button(window, text="Submit", font=("Arial", 12), command=self.submit_number)
        self.submit_button.pack(pady=10)
        
        # Status message
        self.status_var = tk.StringVar()
        self.status_var.set("Enter your first number")
        self.status_label = tk.Label(window, textvariable=self.status_var, font=("Arial", 12))
        self.status_label.pack(pady=10)
        
        # Result label (initially hidden)
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(window, textvariable=self.result_var, font=("Arial", 24), fg="green")
        
        # Restart button (initially hidden)
        self.restart_button = tk.Button(window, text="Play Again", font=("Arial", 12), command=self.restart_game)
        
        # Bind Enter key to submit
        self.window.bind('<Return>', lambda event: self.submit_number())
    
    def submit_number(self):
        number_text = self.number_var.get().strip()
        
        # Validate input
        if not number_text.isdigit():
            self.status_var.set("Please enter a valid number!")
            return
        
        number = int(number_text)
        
        if MIN_NUMBER <= number <= MAX_NUMBER:
            self.numbers_selected.append(number)
            self.number_var.set("")  # Clear input
            self.current_question += 1
            
            if self.current_question < NUMBERS_TO_ASK:
                # More questions to ask
                self.question_label.config(text=f"Enter number {self.current_question + 1}:")
                self.status_var.set(f"Number {self.current_question} accepted. {NUMBERS_TO_ASK - self.current_question} more to go.")
            else:
                # All questions asked, reveal the guess
                self.make_guess()
        else:
            self.status_var.set(f"Number must be between {MIN_NUMBER} and {MAX_NUMBER}!")
    
    def make_guess(self):
        # Hide input elements
        self.question_label.pack_forget()
        self.number_entry.pack_forget()
        self.submit_button.pack_forget()
        
        # Update status
        self.status_var.set("Thinking about your next number...")
        self.window.update()
        
        # Calculate result (simulate delay)
        self.window.after(2000, self.show_result)
    
    def show_result(self):
        # Create final array
        final_array = []
        for i in range(MIN_NUMBER, MAX_NUMBER+1):
            if i not in self.numbers_selected:
                final_array.append(i)
        
        # Remove zero if configured
        if REMOVE_ZERO and 0 in final_array:
            final_array.remove(0)
        
        # Pick random number
        if final_array:
            picked_number = random.choice(final_array)
            self.result_var.set(f"I'm sure it's {picked_number}!")
        else:
            self.result_var.set("No possible number left!")
        
        # Update UI
        self.status_var.set("Think of a new number and I'll guess it")
        self.result_label.pack(pady=20)
        self.restart_button.pack(pady=10)
    
    def restart_game(self):
        # Reset game state
        self.numbers_selected = []
        self.current_question = 0
        
        # Hide result elements
        self.result_label.pack_forget()
        self.restart_button.pack_forget()
        
        # Show input elements again
        self.question_label.config(text=f"Enter number {self.current_question + 1}:")
        self.question_label.pack(pady=(10, 5))
        self.number_entry.pack(pady=10)
        self.submit_button.pack(pady=10)
        
        # Reset status
        self.status_var.set("Enter your first number")
        self.number_var.set("")
        self.number_entry.focus()

# Initialize and run the application
if __name__ == "__main__":
    window = tk.Tk()
    game = NumberGuessingGame(window)
    window.mainloop()

