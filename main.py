import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import qdarktheme
import subprocess

from ui_pyqt5 import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.init_ui(self)
        self.ui.setupUi(self)
        self.ui.init_run(mode='first')

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.live_btn_2.setChecked(True)
        
        self.ui.stackedWidget.currentChanged.connect(self.on_stackedWidget_currentChanged)
        
        self.update_theme()
        QtWidgets.QApplication.instance().paletteChanged.connect(self.update_theme)
        
    def update_theme(self):
        style_file = QtCore.QFile("./style/style.qss")
        style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        modify_stylesheet = QtCore.QTextStream(style_file).readAll()
        
        is_dark_mode = self.check_system_dark_mode()
        theme = "dark" if is_dark_mode else "light"
        
        theme_stylesheet_file = QtCore.QFile(f"./style/{theme}_style.qss")
        theme_stylesheet_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        theme_stylesheet = QtCore.QTextStream(theme_stylesheet_file).readAll()
        
        qdarktheme_stylesheet = qdarktheme.load_stylesheet(theme=theme)
        
        stylesheet = modify_stylesheet + theme_stylesheet + qdarktheme_stylesheet
        
        QtWidgets.QApplication.instance().setStyleSheet(stylesheet)
        
        self.ui.set_icons(is_dark_mode)

    # def is_system_dark_mode(self):
        # bg_color = QtWidgets.QApplication.palette().color(QtGui.QPalette.Window).lightness()
        # return bg_color < 128
        
    def check_system_dark_mode(self):
        if sys.platform == "win32":
            reg_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
            reg_value = "AppsUseLightTheme"
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key) as key:
                    value = winreg.QueryValueEx(key, reg_value)[0]
                    return value == 0
            except FileNotFoundError:
                return False
            except Exception as e:
                print(f"Error checking dark mode on Windows: {e}")
                return False

        if sys.platform == "darwin":
            script = "tell application \"System Events\" to get the dark mode of appearance preferences"
            try:
                result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
                return result.stdout.strip() == "true"
            except Exception as e:
                print(f"Error checking dark mode on macOS: {e}")
                return False
        return False

    def on_stackedWidget_currentChanged(self, index):
        self.ui.reset_values()
        btn_list = self.ui.icon_only_widget.findChildren(QtWidgets.QPushButton) + self.ui.full_menu_widget.findChildren(QtWidgets.QPushButton)
        
        for btn in btn_list:
            if index in [2, 3]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    def on_live_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_live_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_downloader_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_downloader_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        # search_text = self.ui.search_input.text().strip()
        # if search_text:
        #     self.ui.label_search.setText(search_text)

    def on_setting_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

