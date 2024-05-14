import tkinter as tk

# Define the solution string
solution_str = "{0 -> 13, 1 -> 14, 2 -> 15, 3 -> 16, 4 -> 17, 5 -> 12, 6 -> 25, 7 -> 1, 8 -> 2, 9 -> 18, 10 -> 11, 11 -> 24, 12 -> 3, 13 -> 21, 14 -> 19, 15 -> 10, 16 -> 23, 17 -> 22, 18 -> 4, 19 -> 20, 20 -> 9, 21 -> 8, 22 -> 7, 23 -> 6, 24 -> 5}"

# Parsing the solution string into a dictionary
# Strip the outer braces and split by comma
entries = solution_str.strip('{}').split(', ')
print(entries)
solution_dict = {int(k.strip()): int(v.strip()) for part in entries for k, v in (part.split(' -> '),)}
print(solution_dict)

# Calculate board size
size = int(len(solution_dict) ** 0.5)

# Create the GUI window
root = tk.Tk()
root.title("Hidato Solution")

# Create a grid of labels to display the numbers
for key, value in solution_dict.items():
    row, col = divmod(key, size) # gives the row and column index as tuple
    label = tk.Label(root, text=str(value), font=('Arial', 20), width=4, height=2, borderwidth=1, relief="solid")
    label.grid(row=row, column=col)

# Run the application
root.mainloop()
