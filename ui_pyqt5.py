from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from radiko import *

class StreamThread(QtCore.QThread):
    stream_loaded = QtCore.pyqtSignal(bool, str)
    
    def __init__(self, radiko_instance):
        super().__init__()
        self.radiko = radiko_instance
        
    def run(self):
        try:
            m3u8_url = self.radiko.load_m3u8()
            if m3u8_url:
                self.stream_loaded.emit(True, m3u8_url)
            else:
                self.stream_loaded.emit(False, "[Error] Failed to get the stream URL.")
        except Exception as e:
            self.stream_loaded.emit(False, f"[Error]: {str(e)}")

class DownloadThread(QtCore.QThread):
    download_complete = QtCore.pyqtSignal(bool, str)

    def __init__(self, radiko_instance):
        super().__init__()
        self.radiko = radiko_instance

    def run(self):
        try:
            self.radiko.save_mp3_file()
            self.download_complete.emit(True, "✅ Download complete!")
        except Exception as e:
            self.download_complete.emit(False, f"❌ Download failed: {str(e)}")

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.version = '1.0.0'
        self.stations = {}
        self.selected_date = None
        self.selected_station = None
        self.selected_title = None
        self.stream_thread = None
        self.areaFree = False
        self.timeFree = False
        self.start_time = None
        self.end_time = None
        
        self.mode = None
        self.current_page = None
        
        self.current = QtCore.QDateTime.currentDateTime()
        self.current_date = self.current.date()
        self.current_time = self.current.time()
        self.convert_time = None

        self.folder_path = None
        self.init_path = './data/mp3/download.mp3'
        
    def reset_values(self):
        # self.search_input.clear()
        # self.label_search.clear()
        
        self.page_1_station_list.clearSelection()
        self.page_1_station_list.scrollToTop()
        self.page_1_program_title_text.clear()
        self.page_1_program_pfm_text.clear()
        self.page_1_image_label.clear()
        
        self.page_2_date_edit.setDate(self.current_date)
        self.page_2_station_list.clearSelection()
        self.page_2_title_list.clearSelection()
        self.page_2_station_list.scrollToTop()
        self.page_2_title_list.scrollToTop()
        self.page_2_program_title_text.clear()
        self.page_2_time_text.clear()
        self.page_2_program_pfm_text.clear()
        self.page_2_image_label.clear()

    def init_run(self, mode=None):
        self.args = self.set_params()

        self.radiko = Radiko_Downloader(self.args)
        
        if mode == 'first':
            self.load_stations()
        
    def init_ui(self, MainWindow):
        MainWindow.resize(1700, 1200)
    
    def set_icons(self, dark_mode):
        icon_folder = f"./images/icons/dark/" if dark_mode else f"./images/icons/light/"
        
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "antenna-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "antenna-512-color.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "save-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon1.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "save-512-bg.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.icon5 = QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "exit-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon6 = QtGui.QIcon()
        self.icon6.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "menu-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon7 = QtGui.QIcon()
        self.icon7.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "search-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon8 = QtGui.QIcon()
        self.icon8.addPixmap(QtGui.QPixmap(os.path.join(icon_folder, "settings-32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.live_btn_1.setIcon(self.icon)
        self.live_btn_2.setIcon(self.icon)
        self.downloader_btn_1.setIcon(self.icon1)
        self.downloader_btn_2.setIcon(self.icon1)
        self.exit_btn_1.setIcon(self.icon5)
        self.exit_btn_2.setIcon(self.icon5)
        self.change_btn.setIcon(self.icon6)
        self.search_btn.setIcon(self.icon7)
        self.setting_btn.setIcon(self.icon8)
        
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap("./images/images/radiko.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.live_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.live_btn_1.setText("")
        self.live_btn_1.setIconSize(QtCore.QSize(30, 30))
        self.live_btn_1.setCheckable(True)
        self.live_btn_1.setAutoExclusive(True)
        self.live_btn_1.setObjectName("live_btn_1")
        self.verticalLayout.addWidget(self.live_btn_1)
        
        self.downloader_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.downloader_btn_1.setText("")
        self.downloader_btn_1.setIconSize(QtCore.QSize(30, 30))
        self.downloader_btn_1.setCheckable(True)
        self.downloader_btn_1.setAutoExclusive(True)
        self.downloader_btn_1.setObjectName("downloader_btn_1")
        self.verticalLayout.addWidget(self.downloader_btn_1)
        
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        self.exit_btn_1.setIconSize(QtCore.QSize(40, 40))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("./images/images/radiko.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.live_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.live_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.live_btn_2.setCheckable(True)
        self.live_btn_2.setAutoExclusive(True)
        self.live_btn_2.setObjectName("live_btn_2")
        self.verticalLayout_2.addWidget(self.live_btn_2)
        
        self.downloader_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.downloader_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.downloader_btn_2.setCheckable(True)
        self.downloader_btn_2.setAutoExclusive(True)
        self.downloader_btn_2.setObjectName("downloader_btn_2")
        self.verticalLayout_2.addWidget(self.downloader_btn_2)
        
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn_2.setIconSize(QtCore.QSize(30, 30))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setObjectName("change_btn")
        self.change_btn.setIconSize(QtCore.QSize(20, 20))
        self.change_btn.setCheckable(True)
        self.horizontalLayout_4.addWidget(self.change_btn)
        
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        
        self.search_btn = QtWidgets.QPushButton(self.widget)
        self.search_btn.setText("")
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        
        self.setting_btn = QtWidgets.QPushButton(self.widget)
        self.setting_btn.setText("")
        self.setting_btn.setObjectName("setting_btn")
        self.horizontalLayout_4.addWidget(self.setting_btn)
        self.verticalLayout_5.addWidget(self.widget)
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.radiko_live_UI(MainWindow)
        self.radiko_downloader_UI(MainWindow)
        self.search_UI(MainWindow)
        self.setting_UI(MainWindow)
        
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_UI(MainWindow)
        
        self.stackedWidget.setCurrentIndex(3)
        self.toggle_UI(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def toggle_UI(self, MainWindow):
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden)
        self.live_btn_1.toggled['bool'].connect(self.live_btn_2.setChecked)
        self.downloader_btn_1.toggled['bool'].connect(self.downloader_btn_2.setChecked)
        self.live_btn_2.toggled['bool'].connect(self.live_btn_1.setChecked)
        self.downloader_btn_2.toggled['bool'].connect(self.downloader_btn_1.setChecked)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)

    def retranslate_UI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radiko Downloader"))
        self.logo_label_3.setText(_translate("MainWindow", "Radiko"))
        self.live_btn_2.setText(_translate("MainWindow", "Live"))
        self.downloader_btn_2.setText(_translate("MainWindow", "Download"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.label_search.setText(_translate("MainWindow", "To Be Updated"))
        
    def radiko_live_UI(self, MainWindow):
        self.page = QtWidgets.QWidget()
        self.page_1_main_layout = QtWidgets.QVBoxLayout()
        self.page_1_top_group = QtWidgets.QVBoxLayout()
        
        self.video_widget = QtMultimediaWidgets.QVideoWidget()
        self.media_player = QtMultimedia.QMediaPlayer()
        
        self.media_player.setVideoOutput(self.video_widget)
        
        self.page_1_channel_group = QtWidgets.QGroupBox("Select Broadcast")
        self.page_1_channel_layout = QtWidgets.QVBoxLayout()
        
        self.page_1_station_list = QtWidgets.QListWidget()
        self.page_1_station_list.itemClicked.connect(self.on_station_selected)
        self.page_1_channel_layout.addWidget(QtWidgets.QLabel("Select a Station:"))
        self.page_1_channel_layout.addWidget(self.page_1_station_list)
        self.page_1_channel_group.setLayout(self.page_1_channel_layout)

        self.page_1_top_group.addWidget(self.page_1_channel_group)

        self.page_1_info_group = QtWidgets.QGroupBox("Program Information")
        self.page_1_info_layout = QtWidgets.QVBoxLayout()
        self.page_1_image_label = QtWidgets.QLabel()
        self.page_1_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.page_1_image_label.setFixedHeight(300)
        self.page_1_info_layout.addWidget(self.page_1_image_label)
        self.page_1_program_title_text = QtWidgets.QTextEdit()
        self.page_1_program_title_text.setReadOnly(True)
        self.page_1_info_layout.addWidget(QtWidgets.QLabel("Program:"))
        self.page_1_info_layout.addWidget(self.page_1_program_title_text)
        self.page_1_program_pfm_text = QtWidgets.QTextEdit()
        self.page_1_program_pfm_text.setReadOnly(True)
        self.page_1_info_layout.addWidget(QtWidgets.QLabel("Performer:"))
        self.page_1_info_layout.addWidget(self.page_1_program_pfm_text)
        self.page_1_info_group.setLayout(self.page_1_info_layout)

        self.page_1_top_info_group = QtWidgets.QGroupBox("Broadcast Information")
        self.page_1_top_info_layout = QtWidgets.QHBoxLayout()
        
        self.page_1_top_info_layout.addLayout(self.page_1_top_group)
        self.page_1_top_info_layout.addWidget(self.page_1_info_group)
        
        self.page_1_top_info_group.setLayout(self.page_1_top_info_layout)
        
        self.toggle_button = QtWidgets.QPushButton("Play")
        self.toggle_button.setObjectName("toggle_button")
        self.toggle_button.setCheckable(True)
        self.toggle_button.clicked.connect(self.toggle_play_pause)

        self.page_1_main_layout.addWidget(self.page_1_top_info_group)
        self.page_1_main_layout.addWidget(self.video_widget)
        self.page_1_main_layout.addWidget(self.toggle_button)

        self.page.setLayout(self.page_1_main_layout)
        self.stackedWidget.addWidget(self.page)
        
    def radiko_downloader_UI(self, MainWindow):
        self.page_2 = QtWidgets.QWidget()
        self.page_2_main_layout = QtWidgets.QVBoxLayout()

        self.page_2_top_group = QtWidgets.QVBoxLayout()
        
        self.page_2_date_group = QtWidgets.QGroupBox("Select Date")
        self.page_2_date_layout = QtWidgets.QVBoxLayout()
        
        self.page_2_date_edit = QtWidgets.QDateEdit()
        self.page_2_date_edit.setDate(self.current_date)
        self.page_2_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.page_2_date_edit.setCalendarPopup(True)
        self.page_2_date_edit.dateChanged.connect(self.fetch_program_schedule)
        self.page_2_date_layout.addWidget(QtWidgets.QLabel("Select Broadcast Date:"))
        self.page_2_date_layout.addWidget(self.page_2_date_edit)
        self.page_2_date_group.setLayout(self.page_2_date_layout)

        self.page_2_channel_group = QtWidgets.QGroupBox("Select Broadcast")
        self.page_2_channel_layout = QtWidgets.QVBoxLayout()
        
        self.page_2_station_list = QtWidgets.QListWidget()
        self.page_2_station_list.itemClicked.connect(self.on_station_selected)
        self.page_2_channel_layout.addWidget(QtWidgets.QLabel("Select a Station:"))
        self.page_2_channel_layout.addWidget(self.page_2_station_list)
        self.page_2_channel_group.setLayout(self.page_2_channel_layout)
        
        self.page_2_title_list = QtWidgets.QListWidget()
        self.page_2_title_list.itemClicked.connect(self.on_title_selected)
        self.page_2_channel_layout.addWidget(QtWidgets.QLabel("Select Program:"))
        self.page_2_channel_layout.addWidget(self.page_2_title_list)
        self.page_2_channel_group.setLayout(self.page_2_channel_layout)

        self.page_2_top_group.addWidget(self.page_2_date_group)
        self.page_2_top_group.addWidget(self.page_2_channel_group)

        self.page_2_info_group = QtWidgets.QGroupBox("Program Information")
        self.page_2_info_layout = QtWidgets.QVBoxLayout()
        self.page_2_image_label = QtWidgets.QLabel()
        self.page_2_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.page_2_image_label.setFixedHeight(300)
        self.page_2_info_layout.addWidget(self.page_2_image_label)
        self.page_2_program_title_text = QtWidgets.QTextEdit()
        self.page_2_program_title_text.setReadOnly(True)
        self.page_2_time_text = QtWidgets.QTextEdit()
        self.page_2_time_text.setReadOnly(True)
        self.page_2_info_layout.addWidget(QtWidgets.QLabel("Broadcast Time:"))
        self.page_2_info_layout.addWidget(self.page_2_time_text)
        self.page_2_program_pfm_text = QtWidgets.QTextEdit()
        self.page_2_program_pfm_text.setReadOnly(True)
        self.page_2_info_layout.addWidget(QtWidgets.QLabel("Performer:"))
        self.page_2_info_layout.addWidget(self.page_2_program_pfm_text)
        self.page_2_info_group.setLayout(self.page_2_info_layout)

        self.page_2_top_info_group = QtWidgets.QGroupBox("Broadcast Information")
        self.page_2_top_info_layout = QtWidgets.QHBoxLayout()
        
        self.page_2_top_info_layout.addLayout(self.page_2_top_group)
        self.page_2_top_info_layout.addWidget(self.page_2_info_group)
        
        self.page_2_top_info_group.setLayout(self.page_2_top_info_layout)
        
        self.page_2_setting_group = QtWidgets.QGroupBox("Setup and Download")
        self.page_2_setting_layout = QtWidgets.QVBoxLayout()

        self.page_2_file_layout = QtWidgets.QHBoxLayout()

        self.file_path_line_edit = QtWidgets.QLineEdit()
        self.file_path_line_edit.setPlaceholderText(self.init_path)
        self.file_path_line_edit.setReadOnly(True)
        self.file_path_line_edit.mousePressEvent = self.on_file_path_clicked
        self.page_2_file_layout.addWidget(self.file_path_line_edit)

        self.select_folder_button = QtWidgets.QPushButton("📁 Save")
        self.select_folder_button.clicked.connect(self.start_download)
        self.page_2_file_layout.addWidget(self.select_folder_button)

        self.page_2_setting_layout.addLayout(self.page_2_file_layout)

        self.console_output = QtWidgets.QTextEdit()
        self.console_output.setReadOnly(True)
        self.page_2_setting_layout.addWidget(QtWidgets.QLabel("Console Output:"))
        self.page_2_setting_layout.addWidget(self.console_output)
        self.page_2_setting_group.setLayout(self.page_2_setting_layout)

        self.page_2_main_layout.addWidget(self.page_2_top_info_group)
        self.page_2_main_layout.addWidget(self.page_2_setting_group)

        self.page_2.setLayout(self.page_2_main_layout)
        self.stackedWidget.addWidget(self.page_2)

    def search_UI(self, MainWindow):
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_search = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_search.setFont(font)
        self.label_search.setAlignment(QtCore.Qt.AlignCenter)
        self.label_search.setObjectName("label_search")
        self.gridLayout_7.addWidget(self.label_search, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)

    def setting_UI(self, MainWindow):
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_8.setAlignment(QtCore.Qt.AlignCenter)
        
        self.profile_pic = QtWidgets.QLabel(self.page_4)
        pixmap = QtGui.QPixmap("./images/images/profile-circle.png")
        pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.profile_pic.setPixmap(pixmap)
        self.profile_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_pic.setFixedSize(200, 200)
        self.gridLayout_8.addWidget(self.profile_pic, 0, 0, 1, 2, QtCore.Qt.AlignCenter)
        
        self.profile_label_name = QtWidgets.QLabel("devhaaana", self.page_4)
        self.profile_label_name.setObjectName("profile_label_name")
        self.profile_label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_8.addWidget(self.profile_label_name, 1, 0, 1, 2, QtCore.Qt.AlignCenter)
        
        github_url = 'https://github.com/devhaaana'
        self.gridLayout_8.addWidget(self.create_profile_section(self.page_4, "Program Information", "Radiko streaming and download system"), 2, 0, 1, 2)
        self.gridLayout_8.addWidget(self.create_profile_section(self.page_4, "Program Version", "v1.0.0"), 3, 0, 1, 2)
        self.gridLayout_8.addWidget(self.create_profile_section(self.page_4, "GitHub", f"<a href={github_url}>{github_url}</a>"), 4, 0, 1, 2)
        self.gridLayout_8.addWidget(self.create_profile_section(self.page_4, "Copyright", "Copyright 2025. devhaaana All rights reserved."), 5, 0, 1, 2)
        
        self.gridLayout_8.setAlignment(QtCore.Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)
    
    def create_profile_section(self, parent, title, content):
        container = QtWidgets.QFrame(parent)
        container.setObjectName("container")
        container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        
        container_layout = QtWidgets.QVBoxLayout(container)
        container_layout.setSpacing(5)
        
        container_label_title = QtWidgets.QLabel(title, container)
        container_label_title.setObjectName("container_label_title")
        
        container_label_content = QtWidgets.QLabel(content, container)
        container_label_content.setObjectName("container_label_content")
        container_label_content.setOpenExternalLinks(True)

        
        container_layout.addWidget(container_label_title)
        container_layout.addWidget(container_label_content)
        
        return container

    def get_current_date(self, mode):
        new_date = self.current.addDays(-1) if self.current_time.hour() < 5 else self.current
        if mode == 'date':
            return new_date.date().toString("yyyyMMdd")
        elif mode == 'convert_time':
            return self.current.toString("yyyyMMddHH0000")
    
    def get_select_date(self):
        return self.page_2_date_edit.date().toString("yyyyMMdd")
    
    def load_stations(self):
        try:
            stations = self.radiko.get_station_info(get_mode='stationID')
            if stations:
                for station in stations:
                    station_name = station['name']
                    station_id = station['id']
                    self.update_station_ui(station_name, station_id)
            else:
                print("No stations found.")
        except Exception as e:
            print(f"[Error] Loading stations: {e}")

    def on_station_selected(self, item):
        self.current_page = self.stackedWidget.currentIndex()
        self.selected_station = item.text().split("(")[-1].strip(")")
        self.page_1_image_label.clear()
        self.page_2_image_label.clear()
        
        if self.current_page == 0:
            self.page_1_program_title_text.clear()
            
            if self.media_player.state() == QtMultimedia.QMediaPlayer.PlayingState:
                self.pause_video()
                self.media_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl()))
            
            self.fetch_program_details()
            self.toggle_button.setChecked(False)
            self.toggle_button.setText("Play")
        
        self.fetch_program_schedule()

    def on_title_selected(self, item):
        self.selected_title = item.text()
        self.page_2_program_title_text.setText(self.selected_title)
        self.fetch_program_details(self.selected_title)

    def fetch_program_schedule(self):
        self.fetch_data(parse_function=self.parse_program_data)

    def fetch_program_details(self, title=None):
        self.fetch_data(parse_function=lambda xml_data: self.parse_program_details_data(xml_data, title))
    
    def fetch_data(self, parse_function):
        if self.current_page == 0:
            self.selected_date = self.get_current_date(mode='date')
            self.mode = 'live'
        elif self.current_page == 1:
            self.selected_date = self.get_select_date()
            self.mode = 'download'
        self.radiko.get_program_data(selected_station=self.selected_station, selected_date=self.selected_date, parse_function=parse_function)
            
    def parse_program_data(self, xml_data):
        self.page_2_title_list.clear()
        
        titles = self.radiko.get_program_title(xml_data)
        for title in titles:
            self.page_2_title_list.addItem(title)

    def parse_program_details_data(self, xml_data, selected_title):
        self.convert_time = self.get_current_date(mode='convert_time')
        self.start_time, self.end_time, title, performer, img_url = self.radiko.get_program_time(xml_data=xml_data, mode=self.mode, selected_title=selected_title, current_time=self.convert_time)
        self.update_program_ui(self.start_time, self.end_time, title, performer, img_url)

    def update_station_ui(self, station_name, station_id):
        self.page_1_station_list.addItem(f"{station_name} ({station_id})")
        self.page_2_station_list.addItem(f"{station_name} ({station_id})")

    def update_program_ui(self, start_time, end_time, title, performer, img_url):
        time_str = f'{start_time} ~ {end_time}'
        
        if self.current_page == 0:
            self.page_1_program_title_text.append(f'[ {title} ]')
            self.page_1_program_title_text.append(time_str)
            self.page_1_program_pfm_text.setText(performer)
        elif self.current_page == 1:
            self.page_2_time_text.setText(time_str)
            self.page_2_program_pfm_text.setText(performer)
            
        self.set_program_image(img_url)
            
    def set_program_image(self, img_url):
        if img_url:
            pixmap = QtGui.QPixmap()
            img = self.radiko.get_program_image(img_url=img_url)
            pixmap.loadFromData(img)
            if self.current_page == 0:
                self.page_1_image_label.setPixmap(pixmap.scaled(self.page_1_image_label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            elif self.current_page == 1:
                self.page_2_image_label.setPixmap(pixmap.scaled(self.page_2_image_label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def select_folder(self):
        folder_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Set the save path", self.init_path, "MP3 Files (*.mp3)")

        if folder_path:
            if not folder_path.lower().endswith(".mp3"):
                folder_path += ".mp3"
            self.folder_path = folder_path
            self.file_path_line_edit.setText(self.folder_path)
            
        return folder_path
    
    def on_file_path_clicked(self, event=None):
        self.select_folder()
            
    def set_params(self):
        args = {
            'version': self.version,
            'station': self.selected_station,
            'areaFree': self.areaFree,
            'timeFree': self.timeFree,
            'startTime': self.start_time,
            'endTime': self.end_time,
            'save_path': self.folder_path
        }
        
        return args
    
    def start_download(self):
        if not self.selected_station:
            self.console_output.append("❌ No station selected.")
            QtWidgets.QApplication.processEvents()
            return

        if not self.folder_path:
            self.folder_path = self.select_folder()
            if not self.folder_path:
                self.console_output.append("❌ Folder selection has been canceled.")
                QtWidgets.QApplication.processEvents()
                return
        else:
            self.console_output.append(f"📌 Set the save path: '{self.folder_path}'")
            QtWidgets.QApplication.processEvents()

        args = self.set_params()

        try:
            self.radiko = Radiko_Downloader(args)
            self.console_output.append("📥 Start MP3 download...")
            QtWidgets.QApplication.processEvents()

            self.download_thread = DownloadThread(self.radiko)
            self.download_thread.download_complete.connect(self.on_download_complete)
            self.download_thread.start()

        except Exception as e:
            self.console_output.append(f"❌ Download failed: {str(e)}")
            QtWidgets.QApplication.processEvents()
            
    def on_download_complete(self, success, message):
        self.console_output.append(message)
        QtWidgets.QApplication.processEvents()

    def toggle_play_pause(self):
        if self.toggle_button.isChecked():
            self.toggle_button.setText("Pause")
            self.play_video()
        else:
            self.toggle_button.setText("Play")
            self.pause_video()
            
    def on_stream_loaded(self, success, message):
        if success:
            print(f'[Success] Successed to get the stream URL.')
            m3u8_url = message
            self.media_player.stop()
            self.media_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(m3u8_url)))
            self.media_player.play()
        else:
            print(message)
            self.toggle_button.setChecked(False)
            self.toggle_button.setText("Play")
        
    def play_video(self):
        self.init_run()
        if self.stream_thread is not None and self.stream_thread.isRunning():
            self.stream_thread.quit()
        self.stream_thread = StreamThread(self.radiko)
        self.stream_thread.stream_loaded.connect(self.on_stream_loaded)
        self.stream_thread.start()
            
    def pause_video(self):
        if self.media_player:
            self.media_player.pause()