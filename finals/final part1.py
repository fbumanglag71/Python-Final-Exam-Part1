## Author: Francisco Bumanglag
## Project: Final Exam Part1
## Assignment: Module 8 Project 1
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 31, 2023


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import os 



#DELETE THE MATH DB IF IT EXISTS  -- (update link as needed)
db_path = "C:\\Users\\franc\\OneDrive\\Documents\\SAC\\SUMMER 2023\\CMPR114 PHYTON\\MODULE8\\part2\\finals part2\\Math.db"
if os.path.exists(db_path):
    os.remove(db_path)
    
#CREATE THE MATH DATABASE 
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                (id INTEGER PRIMARY KEY,
                firstname TEXT,
                lastname TEXT,
                score REAL)''')
conn.commit()

#IMPORT THE DATA FROM THE TEXT FILE AND INSERT TINO THE DATABASE -- (update link as needed)
text_file_path = "C:\\Users\\franc\\OneDrive\\Documents\\SAC\\SUMMER 2023\\CMPR114 PHYTON\\MODULE8\\part1\\finals\\finals\\test_results.txt"
with open(text_file_path, "r") as file:
    for line in file:
        fields = line.strip().split()
        firstname = fields[0]
        lastname = fields[1]
        score = float(fields[3].replace('%', ''))
        cursor.execute("INSERT INTO scores (firstname, lastname, score) VALUES (?, ?, ?)",
                       (firstname, lastname, score))
conn.commit()


#validate if entry is numeric -- only alphabetic characters allowed
def validate_input():
    global firstname, lastname

    if not firstname.get().isalpha():
        messagebox.showerror("Error", "First name should contain only alphabetic characters.")
        return False

    if not lastname.get().isalpha():
        messagebox.showerror("Error", "Last name should contain only alphabetic characters.")
        return False

    return True

def calculate_score():
    global firstname, lastname, var_question1, var_question2, var_question3, var_question4, var_question5

    if not validate_input():
        return

    #calcuate the percentage ocrrect
    correct_answers = [50, 5000, 2, 150, 50]
    user_answers = [
        var_question1.get(),
        var_question2.get(),
        var_question3.get(),
        var_question4.get(),
        var_question5.get()
    ]
    num_correct = sum(1 for i in range(5) if user_answers[i] == str(correct_answers[i]))
    percent_correct = (num_correct / 5) * 100

    messagebox.showinfo("Result", f"{firstname.get()} {lastname.get()} received {percent_correct:.0f}% test score.")

    #save to text file
    with open("test_results.txt", "w") as f:
        f.write(f"{firstname.get()} {lastname.get()} received {percent_correct:.0f}% test score.")

    #display results on console
    print(f"First Name: {firstname.get()}")
    print(f"Last Name: {lastname.get()}")
    print(f"Percentage Correct: {percent_correct:.0f}%")



def main():
    global firstname, lastname, var_question1, var_question2, var_question3, var_question4, var_question5

    root = tk.Tk()
    root.title("Math Test")
    root.geometry("300x450")
    root.configure(bg="dark grey")

    
    #IMPORT THE BACKGROUND IMAGE -- (update link as needed)
    bg_image_path = "C:\\Users\\franc\\OneDrive\\Documents\\SAC\\SUMMER 2023\\CMPR114 PHYTON\\MODULE8\\part2\\finals part2\\mathimage.jpg"
    bg_image = Image.open(bg_image_path)
    self.bg_photo = ImageTk.PhotoImage(bg_image)  
    self.bg_label = ttk.Label(root, image=self.bg_photo)
    self.bg_label.place(relwidth=1, relheight=1)
         


    #CREATE THE SAVE BUTTON
    self.save_button = ttk.Button(root, text="SAVE", command=self.display_scores)
    self.save_button.pack(pady=10)
    
    def display_scores(self):
        cursor.execute("SELECT firstname, lastname, score FROM scores")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Firstname: {row[0]}, Lastname: {row[1]}, Score: {row[2]}")


    #lastname and firstname labels
    lastname_label = tk.Label(root, text="Last Name:", bg="dark grey", fg="white", font=("bold", 12))
    firstname_label = tk.Label(root, text="First Name:", bg="dark grey", fg="white", font=("bold", 12))



    #inputs for lastname and firstname
    lastname = tk.StringVar()
    firstname = tk.StringVar()

    lastname_entry = tk.Entry(root, textvariable=lastname)
    firstname_entry = tk.Entry(root, textvariable=firstname)


    #labels for the questions
    question1_label = tk.Label(root, text="What is 100 - 50?")
    question2_label = tk.Label(root, text="What is 100 x 50?")
    question3_label = tk.Label(root, text="What is 100 / 50?")
    question4_label = tk.Label(root, text="What is 100 + 50?")
    question5_label = tk.Label(root, text="GCF of 100 and 50")


    #variable to store the users answers
    var_question1 = tk.StringVar()
    var_question2 = tk.StringVar()
    var_question3 = tk.StringVar()
    var_question4 = tk.StringVar()
    var_question5 = tk.StringVar()

      #radio buttons for each question
    question1_radio1 = tk.Radiobutton(root, text="50", variable=var_question1, value="50", bg="dark grey")
    question1_radio2 = tk.Radiobutton(root, text=".50", variable=var_question1, value=".50", bg="dark grey")
    question1_radio3 = tk.Radiobutton(root, text="0.5", variable=var_question1, value="0.5", bg="dark grey")

    question2_radio1 = tk.Radiobutton(root, text="500", variable=var_question2, value="500", bg="dark grey")
    question2_radio2 = tk.Radiobutton(root, text="50", variable=var_question2, value="50", bg="dark grey")
    question2_radio3 = tk.Radiobutton(root, text="5000", variable=var_question2, value="5000", bg="dark grey")

    question3_radio1 = tk.Radiobutton(root, text=".2", variable=var_question3, value=".2", bg="dark grey")
    question3_radio2 = tk.Radiobutton(root, text="20", variable=var_question3, value="20", bg="dark grey")
    question3_radio3 = tk.Radiobutton(root, text="2", variable=var_question3, value="2", bg="dark grey")

    question4_radio1 = tk.Radiobutton(root, text="1150", variable=var_question4, value="1150", bg="dark grey")
    question4_radio2 = tk.Radiobutton(root, text="150", variable=var_question4, value="150", bg="dark grey")
    question4_radio3 = tk.Radiobutton(root, text="15", variable=var_question4, value="15", bg="dark grey")

    question5_radio1 = tk.Radiobutton(root, text="1", variable=var_question5, value="1", bg="dark grey")
    question5_radio2 = tk.Radiobutton(root, text="2", variable=var_question5, value="2", bg="dark grey")
    question5_radio3 = tk.Radiobutton(root, text="50", variable=var_question5, value="50", bg="dark grey")

    #the submit button
    submit_button = tk.Button(root, text="Submit", command=calculate_score, bg="dark grey", fg="white", font=("bold", 12))

    #add additional rows using empty labels
    padding_label1 = tk.Label(root, text="", bg = "dark grey")
    padding_label2 = tk.Label(root, text="", bg = "dark grey")
    padding_label3 = tk.Label(root, text="", bg = "dark grey")
    padding_label4 = tk.Label(root, text="", bg = "dark grey")
    padding_label5 = tk.Label(root, text="", bg = "dark grey")
    padding_label6 = tk.Label(root, text="", bg = "dark grey")

     #place all widgets using grid
    lastname_label.grid(row=1, column=0)
    lastname_entry.grid(row=1, column=1)

    firstname_label.grid(row=2, column=0)
    firstname_entry.grid(row=2, column=1)

    padding_label1.grid(row=3, column=0)

    question1_label.grid(row=4, column=0, columnspan=3)
    question1_radio1.grid(row=5, column=0)
    question1_radio2.grid(row=5, column=1)
    question1_radio3.grid(row=5, column=2)


    padding_label2.grid(row=6, column=0) 

    question2_label.grid(row=7, column=0, columnspan=3)
    question2_radio1.grid(row=8, column=0)
    question2_radio2.grid(row=8, column=1)
    question2_radio3.grid(row=8, column=2)

    padding_label3.grid(row=9, column=0)

    question3_label.grid(row=10, column=0, columnspan=3)
    question3_radio1.grid(row=11, column=0)
    question3_radio2.grid(row=11, column=1)
    question3_radio3.grid(row=11, column=2)

    padding_label4.grid(row=12, column=0)

    question4_label.grid(row=13, column=0, columnspan=3)
    question4_radio1.grid(row=14, column=0)
    question4_radio2.grid(row=14, column=1)
    question4_radio3.grid(row=14, column=2)

    padding_label5.grid(row=15, column=0)

    question5_label.grid(row=16, column=0, columnspan=3)
    question5_radio1.grid(row=17, column=0)
    question5_radio2.grid(row=17, column=1)
    question5_radio3.grid(row=17, column=2)

    padding_label6.grid(row=18, column=0) 

    submit_button.grid(row=19, column=1)

    #set radio button variables
    var_question1.set("None")
    var_question2.set("None")
    var_question3.set("None")
    var_question4.set("None")
    var_question5.set("None")


#CREATE THE MAIN WINDOW APP
root = tk.Tk()
root.mainloop()




if __name__ == "__main__":
    main()








