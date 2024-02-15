import imdb
import tkinter as tk
from tkinter import ttk

def search_movie():
    # Clear previous search results
    results_box.delete(1.0, tk.END)
    
    # Initialize IMDb object
    ia = imdb.IMDb()

    # Get user input
    movie_name = movie_entry.get()

    # Search for movies
    movies = ia.search_movie(movie_name)

    # Display search results
    for movie in movies:
        results_box.insert(tk.END, f"{movie['title']} ({movie['year']})\n")
        results_box.insert(tk.END, "-----------------------------\n")

# Create main window
root = tk.Tk()
root.title("IMDb Movie Search")

# Create a frame for the input
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Label and Entry for movie name
movie_label = ttk.Label(input_frame, text="Enter Movie:")
movie_label.grid(row=0, column=0, padx=10)

movie_entry = ttk.Entry(input_frame, width=40)
movie_entry.grid(row=0, column=1, padx=10)

# Search button
search_button = ttk.Button(input_frame, text="Search", command=search_movie)
search_button.grid(row=0, column=2, padx=10)

# Results text box
results_box = tk.Text(root, height=20, width=50)
results_box.pack(pady=10)

# Run the main loop
root.mainloop()
