from customtkinter import *
import psycopg2
import psycopg2.extras

hostname = "localhost"
database = ""
user_db = ""
pwd = ""
port_id = 5432
cur = None
conn = None

def delete_3():
    screen3.destroy()

def delete_4():
    screen4.destroy()

def delete_5():
    screen5.destroy()

def delete_6():
    screen6.destroy()

def delete_7():
    screen7.destroy()

def delete_8():
    screen8.destroy()

def wrong_password():
    global screen3
    screen3 = CTkToplevel(screen)
    screen3.title("Info")
    screen3.geometry("230x70+1550+350")
    screen3.resizable(False,False)
    CTkLabel(screen3, text= "Wrong password", font=("Times New Roman",18),text_color="red").pack()
    CTkButton(screen3,text="OK",command=delete_3,width=70,height=17,
              corner_radius=90,font=("Helvetica",15)).pack(pady=5)

def user_not_found():
    global screen4
    screen4 = CTkToplevel(screen)
    screen4.title("Info")
    screen4.geometry("230x70+1550+350")
    screen4.resizable(False,False)
    CTkLabel(screen4, text= "User not found", font=("Times New Roman",18),text_color="red").pack()
    CTkButton(screen4,text="OK",command=delete_4,width=70,height=17,
              corner_radius=90,font=("Helvetica",15)).pack(pady=5)

def user_exist():
    global screen5
    screen5 = CTkToplevel(screen)
    screen5.title("Info")
    screen5.geometry("230x70+1550+350")
    screen5.resizable(False,False)
    CTkLabel(screen5, text= "The username already exist", font=("Times New Roman",18),text_color="red").pack()
    CTkButton(screen5,text="OK",command=delete_5,width=70,height=17,
              corner_radius=90,font=("Helvetica",15)).pack(pady=5)

def registration_success():
    global screen6
    screen6 = CTkToplevel(screen)
    screen6.title("Info")
    screen6.geometry("230x70+1550+350")
    screen6.resizable(False,False)
    CTkLabel(screen6, text= "Registration success", font=("Times New Roman",18),text_color="#00FF00").pack()
    CTkButton(screen6,text="OK",command=delete_6,width=70,height=17,
              corner_radius=90,font=("Helvetica",15)).pack(pady=5)

def weak_password():
    global screen7
    screen7 = CTkToplevel(screen)
    screen7.title("Info")
    screen7.geometry("380x70+1520+350")
    screen7.resizable(False,False)
    CTkLabel(screen7, text= "The password must contain at least 3 characters", font=("Times New Roman",18),text_color="red").pack()
    CTkButton(screen7,text="OK",command=delete_7,width=70,height=17,
              corner_radius=90,font=("Helvetica",15)).pack(pady=5)
def login_success():
    global screen8
    screen8 = CTkToplevel(screen)
    screen8.title("Info")
    screen8.geometry("230x70+1550+350")
    screen8.resizable(False,False)
    CTkLabel(screen8, text= "Success, you are logged", font=("Times New Roman",18),text_color="#00FF00").pack()
    CTkButton(screen8,text="OK",command=delete_8,width=70,height=17,
              corner_radius=90,font=("Helvetica",15)).pack(pady=5)
    
def register_user():

    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        create_script = """ CREATE TABLE IF NOT EXISTS login (
                            user_id SERIAL PRIMARY KEY,
                            user_name varchar(40) NOT NULL,
                            password varchar(40) NOT NULL)"""
        cur.execute(create_script)

        username1 = username_entry.get()
        password1 = password_entry.get()
        cur.execute("SELECT user_name FROM login")
        if [username1] in cur:
            user_exist()
        else:
            if len(password1) <= 3:
                weak_password()
            else:
                add_login_script = """ INSERT INTO login(user_name, password) VALUES(%s,%s)"""
                insert_values = (username1,password1)
                cur.execute(add_login_script, insert_values)
                registration_success()

        username1 = None
        password1 = None

        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def login_verify():
    username2 = username_verify.get()
    password2 = password_verify.get()

    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=user_db, password=pwd, port=port_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        select_username = "SELECT user_name FROM login" 
        select_password = "SELECT password FROM login WHERE user_name = %s"
        cur.execute(select_username)
        if [username2] in cur:
            cur.execute(select_password,(username2,))
            if [password2] in cur:
                login_success()
            else:
                wrong_password()
        else:
            user_not_found()

        username2 = None
        password2 = None

        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def register():
    global screen1
    screen1 = CTkToplevel(screen)
    screen1.title("Registration")
    screen1.geometry("300x250+1200+350")
    screen1.resizable(False,False)

    global username_entry
    global password_entry

    CTkLabel(screen1, text="REGISTRATION PROCESS",width=300,height=35,font=("Helvetica",18)).pack()

    CTkLabel(screen1,text = "Username* ",width=300,height=35,font=("Helvetica",18)).pack()
    username_entry = CTkEntry(screen1,border_color="#FFCC70",width=150, height=30)
    username_entry.pack()
    CTkLabel(screen1, text="Password* ",width=300,height=35,font=("Helvetica",18)).pack()
    password_entry = CTkEntry(screen1,border_color="#FFCC70",width=150, height=30)
    password_entry.pack()
    CTkLabel(screen1, text="").pack()

    CTkButton(screen1,text="Register", width=150,height=25, command=register_user,border_color="#FFCC70",font=("Helvetica",15)).pack()

def login():
    global screen2
    global username_verify
    global password_verify

    screen2 = CTkToplevel(screen)
    screen2.title("Logging")
    screen2.geometry("300x250+1200+350")
    screen2.resizable(False,False)

    CTkLabel(screen2, text="LOGGING PROCESS",width=300,height=35,font=("Helvetica",18)).pack()

    CTkLabel(screen2,text = "Username* ",width=300,height=35,font=("Helvetica",18)).pack()
    username_verify = CTkEntry(screen2,border_color="#FFCC70",width=150, height=30)
    username_verify.pack()
    CTkLabel(screen2, text="Password* ",width=300,height=35,font=("Helvetica",18)).pack()
    password_verify = CTkEntry(screen2,border_color="#FFCC70",width=150, height=30)
    password_verify.pack()
    CTkLabel(screen2, text="").pack()
   
    CTkButton(screen2,text="Login", width=150,height=25, command=login_verify,border_color="#FFCC70",font=("Helvetica",15)).pack()

def main_screen():
    global screen
    screen = CTk()
    screen.geometry("500x200+650+350")
    set_appearance_mode("dark")
    screen.title("LOGIN SCREEN")
    screen.resizable(False,False)
  
    CTkLabel(screen,text="WELCOME TO THE APPLICATION", font=("Helvetica", 18)).pack(pady=10)
    CTkLabel(screen,text="").pack()
    CTkButton(screen,text="Login",command=login,width=300,height=35,font=("Helvetica",18),
              corner_radius=30,border_width=2,fg_color="transparent", border_color="#FFCC70").pack()
    CTkLabel(screen,text="").pack()
    CTkButton(screen,text="Register",command=register,width=300,height=35,font=("Helvetica",18),
              corner_radius=30,border_width=2,fg_color="transparent", border_color="#FFCC70").pack()

    screen.mainloop()

if __name__ == "__main__":
    main_screen()

