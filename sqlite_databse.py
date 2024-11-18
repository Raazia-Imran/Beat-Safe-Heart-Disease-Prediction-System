import sqlite3
from tkinter import messagebox
import pandas
from fontTools.misc.psOperators import ps_mark


print("trying to connect")
# B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R
def Save_Data_SQLite(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q,prediction):
    try:
        print("Attempting to connect to the SQLite database...")

        # Connect to SQLite database (or create it if it doesn’t exist)
        connection = sqlite3.connect('Hear.db')
        mycursor = connection.cursor()
        print("Connection to SQLite established")



        # Create table if it does not exist
        command1 = """CREATE TABLE IF NOT EXISTS data(
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT,
                        registration_date INTEGER,
                        DOB TEXT,
                        age INTEGER,
                        sex TEXT,
                        Cp TEXT,
                        trestbps INTEGER,
                        chol INTEGER,
                        fbs TEXT,
                        restecg TEXT,
                        thalach INTEGER,
                        exang TEXT,
                        oldpeak REAL,
                        slope TEXT,
                        ca INTEGER,
                        thal TEXT,
                        result TEXT
                    )"""
        mycursor.execute(command1)

        # Insert data into the table
        command2 = """INSERT INTO data(
                       Name,registration_date,DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, 
                       exang, oldpeak, slope, ca, thal, result
                    ) 
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)"""
        mycursor.execute(command2, (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q,prediction))

        # Commit the changes
        connection.commit()
        print("Data inserted successfully!")

    except sqlite3.Error as error:
        print("Failed to insert data into SQLite table", error)
        messagebox.showerror("Error", f"Failed to insert data: {error}")

    finally:
        # Close the database connection
        if connection:
            connection.close()
            print("SQLite connection is closed")

    messagebox.showinfo("Register", "New user added successfully!!!")

#Save_Data_SQLite(
   # "John Doe", "1990-01-01", 33, "Male", "typical", 120, 240, "No",
   # "Normal", 150, "No", 1.5, "Upsloping", 0, "Normal", "Healthy"
