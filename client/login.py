# import requests
# import json
# import os
# from tkinter import *
# import tkinter.messagebox as tm


# class LoginFrame(Frame):
#     def __init__(self, master):
#         super().__init__(master)

#         self.label_username = Label(self, text="Username")
#         self.label_password = Label(self, text="Password")

#         self.entry_username = Entry(self)
#         self.entry_password = Entry(self, show="*")

#         self.label_username.grid(row=0, sticky=E)
#         self.label_password.grid(row=1, sticky=E)
#         self.entry_username.grid(row=0, column=1)
#         self.entry_password.grid(row=1, column=1)

#         self.checkbox = Checkbutton(self, text="Keep me logged in")
#         self.checkbox.grid(columnspan=2)

#         self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
#         self.signupbtn = Button(self, text="Sign Up", command=self._sign_up_btn_clicked)
#         self.logbtn.grid(columnspan=2)
#         self.signupbtn.grid(columnspan=2)

#         self.pack()

#     def _login_btn_clicked(self):
#         # print("Clicked")
#         username = self.entry_username.get()
#         password = self.entry_password.get()
#         #authenticate from server side
#         payload = {}
#         payload["userName"] = username
#         payload["pass"] = password
#         #payload = {'user':'user', 'pass':'123456'}
#         r = requests.post('http://localhost:8080/auth/login', json=payload)
#         print(r.text)
        
#         print(payload["userName"])

#         if r.text == "Success":
#             tm.showinfo("Login info", "Welcome: " + username)
#             #os.system('python3 showchessboard2.py')
#             sys.exit()
#         else:
#             tm.showerror("Login error", "Incorrect username")

#     def _sign_up_btn_clicked(self):
#         # print("Clicked")
#         username = self.entry_username.get()
#         password = self.entry_password.get()
#         #authenticate from server side
#         payload = {}
#         payload["userName"] = username
#         payload["pass"] = password
#         #payload = {'user':'user', 'pass':'123456'}
#         r = requests.post('http://localhost:8080/auth/signup', json=payload)
#         print(r.text)
        
#         print(payload["userName"])

#         if r.text == "Success":
#             #tm.showinfo("Login info", "Welcome: " + username)
#             #os.system('python3 showchessboard2.py')
#             #sys.exit()
#             tm.showerror("Sign up info", "Sign Up Success")
#         else:
#             tm.showerror("Signup error", "Try Again")

# root = Tk()
# lf = LoginFrame(root)
# root.mainloop()



from PyQt5 import QtWidgets
import requests
from showchessboard3 import *
# from mainwindow import Ui_MainWindow

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):

        payload = {}
        payload["userName"] = self.textName.text()
        payload["pass"] = self.textPass.text()
        #payload = {'user':'user', 'pass':'123456'}
        r = requests.post('http://localhost:8080/auth/login', json=payload)
        print(r.text)
        
        print(payload["userName"])

        if (r.text == "Success"):
            QtWidgets.QMessageBox.warning(self, 'Success', 'Success')
            # self.close()
            print("here")

            
            self.game = Gomoku()
            self.game.show()
            #self.close()
            #self.close()
            #sys.exit(app.exec_())


            print("test")
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
