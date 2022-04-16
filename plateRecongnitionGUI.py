import imp
import os
import sys
import cv2
import plateRecongnition
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_slots()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1486, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(40)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plateImg = QtWidgets.QLabel(self.centralwidget)
        self.plateImg.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.plateImg.setText("")
        self.plateImg.setObjectName("plateImg")
        self.horizontalLayout.addWidget(self.plateImg)
        self.preImg = QtWidgets.QLabel(self.centralwidget)
        self.preImg.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.preImg.setText("")
        self.preImg.setObjectName("preImg")
        self.horizontalLayout.addWidget(self.preImg)
        self.susImg = QtWidgets.QLabel(self.centralwidget)
        self.susImg.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.susImg.setText("")
        self.susImg.setObjectName("susImg")
        self.horizontalLayout.addWidget(self.susImg)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setObjectName("label_0")
        self.horizontalLayout_2.addWidget(self.label_0)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(40)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.recongnitionImg = QtWidgets.QLabel(self.centralwidget)
        self.recongnitionImg.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.recongnitionImg.setText("")
        self.recongnitionImg.setObjectName("recongnitionImg")
        self.verticalLayout_3.addWidget(self.recongnitionImg)
        self.binImg = QtWidgets.QLabel(self.centralwidget)
        self.binImg.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.binImg.setText("")
        self.binImg.setObjectName("binImg")
        self.verticalLayout_3.addWidget(self.binImg)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pchar_0 = QtWidgets.QLabel(self.centralwidget)
        self.pchar_0.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.pchar_0.setText("")
        self.pchar_0.setObjectName("pchar_0")
        self.horizontalLayout_4.addWidget(self.pchar_0)
        self.pchar_1 = QtWidgets.QLabel(self.centralwidget)
        self.pchar_1.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.pchar_1.setText("")
        self.pchar_1.setObjectName("pchar_1")
        self.horizontalLayout_4.addWidget(self.pchar_1)
        self.pchar_2 = QtWidgets.QLabel(self.centralwidget)
        self.pchar_2.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.pchar_2.setText("")
        self.pchar_2.setObjectName("pchar_2")
        self.horizontalLayout_4.addWidget(self.pchar_2)
        self.pchar_3 = QtWidgets.QLabel(self.centralwidget)
        self.pchar_3.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.pchar_3.setText("")
        self.pchar_3.setObjectName("pchar_3")
        self.horizontalLayout_4.addWidget(self.pchar_3)
        self.pchar_4 = QtWidgets.QLabel(self.centralwidget)
        self.pchar_4.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.pchar_4.setText("")
        self.pchar_4.setObjectName("pchar_4")
        self.horizontalLayout_4.addWidget(self.pchar_4)
        self.pchar_5 = QtWidgets.QLabel(self.centralwidget)
        self.pchar_5.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.pchar_5.setText("")
        self.pchar_5.setObjectName("pchar_5")
        self.horizontalLayout_4.addWidget(self.pchar_5)
        self.pchar_6 = QtWidgets.QLabel(self.centralwidget)
        self.pchar_6.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.pchar_6.setText("")
        self.pchar_6.setObjectName("pchar_6")
        self.horizontalLayout_4.addWidget(self.pchar_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.char_0 = QtWidgets.QLabel(self.centralwidget)
        self.char_0.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.char_0.setText("")
        self.char_0.setObjectName("char_0")
        self.horizontalLayout_5.addWidget(self.char_0)
        self.char_1 = QtWidgets.QLabel(self.centralwidget)
        self.char_1.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.char_1.setText("")
        self.char_1.setObjectName("char_1")
        self.horizontalLayout_5.addWidget(self.char_1)
        self.char_2 = QtWidgets.QLabel(self.centralwidget)
        self.char_2.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.char_2.setText("")
        self.char_2.setObjectName("char_2")
        self.horizontalLayout_5.addWidget(self.char_2)
        self.char_3 = QtWidgets.QLabel(self.centralwidget)
        self.char_3.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.char_3.setText("")
        self.char_3.setObjectName("char_3")
        self.horizontalLayout_5.addWidget(self.char_3)
        self.char_4 = QtWidgets.QLabel(self.centralwidget)
        self.char_4.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.char_4.setText("")
        self.char_4.setObjectName("char_4")
        self.horizontalLayout_5.addWidget(self.char_4)
        self.char_5 = QtWidgets.QLabel(self.centralwidget)
        self.char_5.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.char_5.setText("")
        self.char_5.setObjectName("char_5")
        self.horizontalLayout_5.addWidget(self.char_5)
        self.char_6 = QtWidgets.QLabel(self.centralwidget)
        self.char_6.setStyleSheet("QLabel{background-color:rgb(255,255,255);}")
        self.char_6.setText("")
        self.char_6.setObjectName("char_6")
        self.horizontalLayout_5.addWidget(self.char_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.loadImg = QtWidgets.QPushButton(self.centralwidget)
        self.loadImg.setObjectName("loadImg")
        self.verticalLayout_7.addWidget(self.loadImg)
        self.preProcess = QtWidgets.QPushButton(self.centralwidget)
        self.preProcess.setObjectName("preProcess")
        self.verticalLayout_7.addWidget(self.preProcess)
        self.suspectPlate = QtWidgets.QPushButton(self.centralwidget)
        self.suspectPlate.setObjectName("suspectPlate")
        self.verticalLayout_7.addWidget(self.suspectPlate)
        self.platehRcognition = QtWidgets.QPushButton(self.centralwidget)
        self.platehRcognition.setObjectName("platehRcognition")
        self.verticalLayout_7.addWidget(self.platehRcognition)
        self.plateProcess = QtWidgets.QPushButton(self.centralwidget)
        self.plateProcess.setObjectName("plateProcess")
        self.verticalLayout_7.addWidget(self.plateProcess)
        self.charSegmentation = QtWidgets.QPushButton(self.centralwidget)
        self.charSegmentation.setObjectName("charSegmentation")
        self.verticalLayout_7.addWidget(self.charSegmentation)
        self.recognitionResult = QtWidgets.QPushButton(self.centralwidget)
        self.recognitionResult.setObjectName("recognitionResult")
        self.verticalLayout_7.addWidget(self.recognitionResult)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1486, 26))
        self.menubar.setObjectName("menubar")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionda = QtWidgets.QAction(MainWindow)
        self.actionda.setObjectName("actionda")
        self.actionbao = QtWidgets.QAction(MainWindow)
        self.actionbao.setObjectName("actionbao")
        self.actiontui = QtWidgets.QAction(MainWindow)
        self.actiontui.setObjectName("actiontui")
        self.actionjianqie = QtWidgets.QAction(MainWindow)
        self.actionjianqie.setObjectName("actionjianqie")
        self.actionfuzhi = QtWidgets.QAction(MainWindow)
        self.actionfuzhi.setObjectName("actionfuzhi")
        self.actionzhantie = QtWidgets.QAction(MainWindow)
        self.actionzhantie.setObjectName("actionzhantie")
        self.actiongaunyu = QtWidgets.QAction(MainWindow)
        self.actiongaunyu.setObjectName("actiongaunyu")
        self.menu_1.addAction(self.actionda)
        self.menu_1.addAction(self.actionbao)
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.actiontui)
        self.menu_2.addAction(self.actionjianqie)
        self.menu_2.addAction(self.actionfuzhi)
        self.menu_2.addAction(self.actionzhantie)
        self.menu_3.addAction(self.actiongaunyu)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "车牌识别"))
        self.label_0.setText(_translate("MainWindow", "车牌图片"))
        self.label_1.setText(_translate("MainWindow", "车牌预处理"))
        self.label_2.setText(_translate("MainWindow", "疑似车牌区域"))
        self.label_3.setText(_translate("MainWindow", "车牌识别和提取"))
        self.label_4.setText(_translate("MainWindow", "车牌二值化和校正"))
        self.label_5.setText(_translate("MainWindow", "字符分割"))
        self.label_6.setText(_translate("MainWindow", "识别结果"))
        self.loadImg.setText(_translate("MainWindow", "加载图片"))      #设置plateImg图框   
        self.preProcess.setText(_translate("MainWindow", "预处理"))     #设置preImg图框
        self.suspectPlate.setText(_translate("MainWindow", "疑似车牌")) #设置susImg图框
        self.platehRcognition.setText(_translate("MainWindow", "车牌识别")) #设置recongnitionImg图框
        self.plateProcess.setText(_translate("MainWindow", "车牌处理"))     #设置binImg图框
        self.charSegmentation.setText(_translate("MainWindow", "字符分割"))     #设置pchar_0-pchar_6图框
        self.recognitionResult.setText(_translate("MainWindow", "识别结果"))    #设置char_0-char_6图框
        self.menu_1.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.actionda.setText(_translate("MainWindow", "打开"))
        self.actionbao.setText(_translate("MainWindow", "保存"))
        self.actiontui.setText(_translate("MainWindow", "退出"))
        self.actionjianqie.setText(_translate("MainWindow", "剪切"))
        self.actionfuzhi.setText(_translate("MainWindow", "复制"))
        self.actionzhantie.setText(_translate("MainWindow", "粘贴"))
        self.actiongaunyu.setText(_translate("MainWindow", "关于"))

    def init_slots(self):
        self.loadImg.clicked.connect(self.load_image)
        self.preProcess.clicked.connect(self.pre_image)
        self.suspectPlate.clicked.connect(self.sus_image)
        self.platehRcognition.clicked.connect(self.rcong_image)
        self.plateProcess.clicked.connect(self.plate_image)
        self.charSegmentation.clicked.connect(self.char_image)
        self.recognitionResult.clicked.connect(self.result_image)
    
    def load_image(self):
        img_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开图片", "", "Images(*.png *.jpg *jpeg);;All Files(*)")
        if not img_path:
            return
        plateRecongnition.plate_recongnition(img_path)
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(439, 342, QtCore.Qt.KeepAspectRatio)
        self.plateImg.setPixmap(pix)
        self.plateImg.setScaledContents(True)
        
    def pre_image(self):
        img_path = './carIdentityData/opencv_output/preImg.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(439, 342, QtCore.Qt.KeepAspectRatio)
        self.preImg.setPixmap(pix)
        self.preImg.setScaledContents(True)

    def sus_image(self):
        img_path = './carIdentityData/opencv_output/susImg.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(439, 342, QtCore.Qt.KeepAspectRatio)
        self.susImg.setPixmap(pix)
        self.susImg.setScaledContents(True)

    def rcong_image(self):
        img_path = './carIdentityData/opencv_output/recongnitionImg.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(540, 170, QtCore.Qt.KeepAspectRatio)
        self.recongnitionImg.setPixmap(pix)
        self.recongnitionImg.setScaledContents(True)

    def plate_image(self):
        img_path = './carIdentityData/opencv_output/binImg.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(540, 170, QtCore.Qt.KeepAspectRatio)
        self.binImg.setPixmap(pix)
        self.binImg.setScaledContents(True)

    def char_image(self):
        img_path = './carIdentityData/opencv_output/pchar_0.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.pchar_0.setPixmap(pix)
        self.pchar_0.setScaledContents(True)
        
        img_path = './carIdentityData/opencv_output/pchar_1.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.pchar_1.setPixmap(pix)
        self.pchar_1.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/pchar_2.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.pchar_2.setPixmap(pix)
        self.pchar_2.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/pchar_3.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.pchar_3.setPixmap(pix)
        self.pchar_3.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/pchar_4.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.pchar_4.setPixmap(pix)
        self.pchar_4.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/pchar_5.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.pchar_5.setPixmap(pix)
        self.pchar_5.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/pchar_6.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.pchar_6.setPixmap(pix)
        self.pchar_6.setScaledContents(True)
        
    def result_image(self):
        img_path = './carIdentityData/opencv_output/char_0.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.char_0.setPixmap(pix)
        self.char_0.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/char_1.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.char_1.setPixmap(pix)
        self.char_1.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/char_2.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.char_2.setPixmap(pix)
        self.char_2.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/char_3.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.char_3.setPixmap(pix)
        self.char_3.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/char_4.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.char_4.setPixmap(pix)
        self.char_4.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/char_5.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.char_5.setPixmap(pix)
        self.char_5.setScaledContents(True)

        img_path = './carIdentityData/opencv_output/char_6.jpg'
        if not img_path:
            return
        pix = QtGui.QPixmap(img_path)
        pix = pix.scaled(70, 160, QtCore.Qt.KeepAspectRatio)
        self.char_6.setPixmap(pix)
        self.char_6.setScaledContents(True)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())