from PyQt5.QtWidgets import QMainWindow,QSpinBox,QApplication,QLineEdit,QPushButton,QLabel,QRadioButton,QFormLayout
from PyQt5 import uic
import sys
import random
import string
import pyperclip

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("password generator.ui",self)
        self.setWindowTitle("Password Generator")
        self.edit1=self.findChild(QLineEdit,"lineEdit")
        self.button=self.findChild(QPushButton,"pushButton")
        self.label1=self.findChild(QLabel,"label_3")
        
        self.formlayout1=self.findChild(QFormLayout,"formLayout")
        self.formlayout2=self.findChild(QFormLayout,"formLayout_2")
        self.label2=self.findChild(QLabel,"label")
        self.label3=self.findChild(QLabel,"label_2")
        self.spin=self.findChild(QSpinBox,"spinBox")
        self.radiobutton=self.findChild(QRadioButton,"radioButton")
        self.radiobutton2=self.findChild(QRadioButton,"radioButton_2")
        self.radiobutton3=self.findChild(QRadioButton,"radioButton_3")
        self.radiobutton4=self.findChild(QRadioButton,"radioButton_4")
        self.radiobutton5=self.findChild(QRadioButton,"radioButton_5")
        self.radiobutton6=self.findChild(QRadioButton,"radioButton_6")
        self.radiobutton7=self.findChild(QRadioButton,"radioButton_7")
        self.button2=self.findChild(QPushButton,"pushButton_2")
        self.button3=self.findChild(QPushButton,"pushButton_3")
        self.button.font
               
        self.radiobutton.setChecked(True)
        self.radiobutton4.setChecked(True)
        self.spin.setValue(10)
        
        self.button.clicked.connect(self.pass_generator)               
        self.button2.clicked.connect(self.copy)
        self.button3.clicked.connect(self.close_win)
        
        self.show()
    #Define function to Generate Password
    def pass_generator(self):
       characters2=""  
       if self.radiobutton.isChecked():                   
            
            characters = string.ascii_lowercase
            characters += string.ascii_uppercase
       elif self.radiobutton2.isChecked():
            
            characters = string.ascii_lowercase
       elif self.radiobutton3.isChecked():
            
            characters = string.ascii_uppercase
       if self.radiobutton4.isChecked():
            
            characters2 = string.digits
            characters2 += string.punctuation
       elif self.radiobutton5.isChecked():
             
            characters2 = string.digits
       elif self.radiobutton6.isChecked():
            
            characters2 = string.punctuation
       #Mix All characters as uppercase & lowercase & numbers & puncuation 
       characters+=characters2       
     
       password = ''.join(random.choice(characters) for _ in range(self.spin.value()))
        
       self.edit1.setText(password)
    
    def copy(self):
        
        pyperclip.copy(self.edit1.text())
                
    
    def close_win(self):
        sys.exit(0)

app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()