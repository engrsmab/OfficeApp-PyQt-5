
from PyQt5 import QtCore, QtGui, QtWidgets
from tkmacosx import widgets
from Python_Files.Requirments import *
from Python_Files.login_ import Ui_MainWindow
from Python_Files.register_ import Register_Ui
from Python_Files.dashboard_ import Ui_dashboard
from tabs.add_bill import Add_Bill
import sys
from Python_Files.search_window_ import Ui_Form
class logged_in:
    def __init__(self,main,profile) -> None:
        self.data = profile
        self.MainWindow = main
        self.dashboard = Ui_dashboard()
        self.dashboard.setupUi(self.MainWindow)
        self.dashboard.designation.setText(self.data[6])
        self.dashboard.name.setText(self.data[0])
        
        self.buttons = [self.dashboard.home_btn,self.dashboard.billing_btn,self.dashboard.projects_btn,self.dashboard.stock_btn,self.dashboard.setting_btn]
        commands = [self.Home,self.Bills,self.Projects,self.Stocks,self.Settings]
        count = 0
        for btn in self.buttons:
            btn.clicked.connect(commands[count])
            count += 1
        
    def Home(self):
        self.set_Btn_Styles(0)
    def Bills(self):
        self.set_Btn_Styles(1)
        search_area = Ui_Form()
        search_area.setupUi(self.dashboard.frame_3)
        search_area.frame.show()
        search_area.scrollArea.show()
        search_area.new_add_btn.clicked.connect(self.Add_bill)
        search_entries = [search_area.Diary_search,search_area.sub_search,search_area.depart_search,search_area.firm_search]

        
       
    def Projects(self):
        self.set_Btn_Styles(2)
        search_area = Ui_Form()
        search_area.setupUi(self.dashboard.frame_3)
        search_area.label_2.setText("Project Title")
        search_area.frame.show()
        search_area.scrollArea.show()
        # search_area.new_add_btn.clicked.connect(self.Add_bill)
        search_entries = [search_area.Diary_search,search_area.sub_search,search_area.depart_search,search_area.firm_search]
    def Stocks(self):
        self.set_Btn_Styles(3)
    def Settings(self):
        self.set_Btn_Styles(4)
    def Add_bill(self):
        add_bill_window = Add_Bill(self.MainWindow)
        add_bill_window.New_Bill_Window.close.clicked.connect(lambda m = self.MainWindow,d = self.data:close(m,d))

    def set_Btn_Styles(self,btn_no):
        press_styleSheet = ("QPushButton{\n"
"color:white;\n"
"background-image:url(:/Pics/bill-32.png);\n"
"background-repeat:none;\n"
"padding-left:40px;\n"
"background-color:rgb(49, 49, 49);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(49, 49, 49);\n"
"color:white;\n"
"}")
        normal_styleSheet = ("QPushButton{\n"
"color:white;\n"
"background-image:url(:/Pics/bill-32.png);\n"
"background-repeat:none;\n"
"padding-left:40px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(49, 49, 49);\n"
"color:white;\n"
"}")
        for btns in range(len(self.buttons)):
            if btns == btn_no:
                self.buttons[btns].setStyleSheet(press_styleSheet)
            else:
                self.buttons[btns].setStyleSheet(normal_styleSheet)
    

def close(main,data):
    main_window = logged_in(main,data)
    main_window.Bills()