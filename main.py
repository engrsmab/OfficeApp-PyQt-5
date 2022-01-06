from Python_Files.STARTER_ import Starter
from Python_Files.Logged_In import *
from Files.Img.imgs_ import *
from PyQt5.QtWidgets import QGraphicsDropShadowEffect 
import Python_Files.Backend as Backend
class Start:
    def __init__(self) -> None:
        LoginStatus,data = Backend.Login_Status(pc_name)
        if LoginStatus:
            self.start_dashboard(data)
        self.start_ui = Starter()
        self.start_ui.setupUi(MainWindow)
        MainWindow.show()
        self.setup_starter()
    def setup_starter(self):
        # self.start_ui.label.setPixmap(QtGui.QPixmap(Images[0]))
        self.start_ui.pushButton.clicked.connect(self.login_window)
        self.start_ui.Reg_Btn.clicked.connect(self.register_window)
        
    def login_window(self):
        self.login = Ui_MainWindow()
        self.login.setupUi(MainWindow)
        self.login.create_btn.clicked.connect(self.register_window)
        self.login.login_btn.clicked.connect(self.validate_login)
        self.login.Password.returnPressed.connect(self.validate_login)
        self.login.Username.returnPressed.connect(self.validate_login)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(35)
        self.login.frame_3.setGraphicsEffect(shadow)
    
    def validate_login(self):
        entries = [self.login.Username.text(),self.login.Password.text()]
        c = self.login.remember_me.isChecked()
        data = Backend.Login_Backend(entries,c,pc_name)
        if data != "wrong":
            self.start_dashboard(data)
    def validate_submit(self):
        data = [self.register.name_entry.text(),self.register.contact_entry.text(),self.register.email_entry.text(),self.register.mail_entry.text(),self.register.user_entry.text(),self.register.password_entry.text(),self.register.type_combo.currentText(),self.register.id_entry.text()]
        Backend.Submit(entries=data)

    def register_window(self):
        self.register = Register_Ui()
        self.register.setupUi(MainWindow)
        types = ["Employee","Bill Officer","Owner"]
        for names in types:
            self.register.type_combo.addItem(names)
        self.register.submit_btn.clicked.connect(self.login_window)
        self.register.submit_btn_2.clicked.connect(self.validate_submit)
    def start_dashboard(self,data):
        self.dashboard = logged_in(MainWindow,data)
        self.dashboard.dashboard.logout_btn.clicked.connect(self.logout)
    def logout(self):
        msg = Backend.ask_dialog("Logout Notification","Do you want to logout?","This will return to login screen")
        #msg.buttonClicked.connect(self.login_window)
        if msg == Backend.QMessageBox.Yes:
            self.login_window()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Start()
    sys.exit(app.exec_())