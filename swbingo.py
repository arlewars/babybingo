import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# List of words to randomly place on the Bingo card
bingo_words = [
    "diaper change", "first steps", "baby bottle", "pacifier", "blankie", 
    "bassinet", "baby monitor", "car seat", "formula", "high chair", 
    "juice", "Nursery", "nap time", "peek-a-boo", "teething", 
    "toddler", "wipes", "toy", "milk", "bib", "onesie", 
    "stroller", "rattle", "baby", "daddy", "mommy",
    "spoil", "babysitter", "nappy", "fussy", "preschool",
    "brat", "triplets", "umbilical cord", "tots", "bambino",
    "pappoose", "twins", "ween", "crib", "diaper pail",
    "playpen", "bouncer", "baby lotion", "bottle warmer", "hooded towel"
]

# Function to generate a Bingo card with dynamic borders based on word length
def generate_bingo_card():
    # Shuffle the words list to randomize the placement
    random.shuffle(bingo_words)

    # Initialize the 5x5 Bingo card with "Baby Bingo" at the top
    bingo_card = [["" for _ in range(5)] for _ in range(5)]
    
    # Fill the 5x5 grid with the random words
    idx = 0
    for row in range(5):
        for col in range(5):
            if row == 2 and col == 2:  # Middle space is the free space
                bingo_card[row][col] = "FREE SPACE"
            else:
                bingo_card[row][col] = bingo_words[idx]
                idx += 1

    return bingo_card

# Function to update cell text when clicked
def cell_clicked(row, col):
    current_text = cells[row][col].cget("text")
    if current_text != "FREE SPACE":
        new_text = f"~~{current_text}~~" if not current_text.startswith("~~") else current_text[2:-2]
        cells[row][col].config(text=new_text)

# Function to clear the board
def clear_board():
    for row in range(5):
        for col in range(5):
            if row == 2 and col == 2:
                cells[row][col].config(text="FREE SPACE")
            else:
                cells[row][col].config(text=bingo_card[row][col])

# Function to generate a new random Bingo board
def new_board():
    global bingo_card
    bingo_card = generate_bingo_card()
    clear_board()

# Function to create the tkinter app
def create_tkinter_app():
    global cells, bingo_card, logo_img

    root = tk.Tk()
    root.title("Baby Bingo")

    # Load logo image if it exists
    if os.path.exists("sw.png"):
        img = Image.open("sw.png")
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(img)
        logo_label = tk.Label(root, image=logo_img)
        logo_label.grid(row=0, column=5, rowspan=2, padx=10, pady=10)

    bingo_card = generate_bingo_card()

    # Create a grid of buttons for the Bingo card
    cells = [[None for _ in range(5)] for _ in range(5)]
    for row in range(5):
        for col in range(5):
            cells[row][col] = tk.Label(root, text=bingo_card[row][col], width=20, height=5, borderwidth=2, relief="solid")
            cells[row][col].grid(row=row, column=col, padx=2, pady=2)
            cells[row][col].bind("<Button-1>", lambda e, r=row, c=col: cell_clicked(r, c))

    # Create a "Clear Board" button
    clear_button = tk.Button(root, text="Clear Board", command=clear_board)
    clear_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Create a "New Board" button
    new_board_button = tk.Button(root, text="New Board", command=new_board)
    new_board_button.grid(row=5, column=3, columnspan=2, pady=10)

    root.mainloop()

# Run the tkinter app
create_tkinter_app()

