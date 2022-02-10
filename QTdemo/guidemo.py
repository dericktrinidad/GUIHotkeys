import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("guidemo.ui", self)
        self.choose_profile.clicked.connect(self.goto_choose_profile)
        self.hotkeys.clicked.connect(self.goto_hotkeys)
        # self.clicked.connect(self.Run)

    def goto_choose_profile(self):
        choose = ChooseProfile()
        widget.addWidget(choose)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_hotkeys(self):
        hotkey = HotkeyWidget()
        widget.addWidget(hotkey)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ChooseProfile(QDialog):
    def __init__(self):
        super(ChooseProfile, self).__init__()
        loadUi("choose_profile.ui", self)
        self.back_btn.clicked.connect(self.go_back)
    def go_back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
    # def goto_create(self):
    #     pass
    # def goto_edit(self):
    #     pass
    # def goto_delete(self):
    #     pass

class HotkeyWidget(QDialog):
    def __init__(self):
        super(HotkeyWidget, self).__init__()
        loadUi("hotkeys.ui", self)
        self.back_btn.clicked.connect(self.go_back)
        # inputs
        self.up_key.connect(self.in_up_key)
        self.dn_key.connect(self.in_dn_key)
        self.lt_key.connect(self.in_lt_key)
        self.rt_key.connect(self.in_rt_key)
    # widget controls
    def go_back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
    def add_hk(self):
        pass
    def del_hk(self):
        pass
    def run(self):
        pass

    # keyboard inputs
    def in_up_key(self):
        pass
    def in_dn_key(self):
        pass
    def in_lt_key(self):
        pass
    def in_rt_key(self):
        pass

# class RunProfile(QDialog):
#     def __init__(self):
#         super(RunProfile, self).__init__()
#         loadUi("edit_hk.ui", self)
#   main
app = QApplication(sys.argv)

#call window
welcome =WelcomeScreen()
# profile = ChooseProfile()
# run = RunProfile()

widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")