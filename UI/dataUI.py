# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BrainExtraction(object):
    def setupUi(self, BrainExtraction):
        BrainExtraction.setObjectName("BrainExtraction")
        BrainExtraction.resize(706, 421)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BrainExtraction.sizePolicy().hasHeightForWidth())
        BrainExtraction.setSizePolicy(sizePolicy)
        BrainExtraction.setMaximumSize(QtCore.QSize(1000, 1000))
        BrainExtraction.setLayoutDirection(QtCore.Qt.LeftToRight)
        BrainExtraction.setAutoFillBackground(False)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(BrainExtraction)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(BrainExtraction)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineImagePath = QtWidgets.QLineEdit(BrainExtraction)
        self.lineImagePath.setObjectName("lineImagePath")
        self.horizontalLayout.addWidget(self.lineImagePath)
        self.btnImagePath = QtWidgets.QToolButton(BrainExtraction)
        self.btnImagePath.setObjectName("btnImagePath")
        self.horizontalLayout.addWidget(self.btnImagePath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(BrainExtraction)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.LineHippo = QtWidgets.QLineEdit(BrainExtraction)
        self.LineHippo.setObjectName("LineHippo")
        self.horizontalLayout_2.addWidget(self.LineHippo)
        self.btnHippoPath = QtWidgets.QToolButton(BrainExtraction)
        self.btnHippoPath.setObjectName("btnHippoPath")
        self.horizontalLayout_2.addWidget(self.btnHippoPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(BrainExtraction)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.LineFeaturePath = QtWidgets.QLineEdit(BrainExtraction)
        self.LineFeaturePath.setObjectName("LineFeaturePath")
        self.horizontalLayout_3.addWidget(self.LineFeaturePath)
        self.btnFeaturePath = QtWidgets.QToolButton(BrainExtraction)
        self.btnFeaturePath.setObjectName("btnFeaturePath")
        self.horizontalLayout_3.addWidget(self.btnFeaturePath)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(BrainExtraction)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.LineBrainPath = QtWidgets.QLineEdit(BrainExtraction)
        self.LineBrainPath.setObjectName("LineBrainPath")
        self.horizontalLayout_4.addWidget(self.LineBrainPath)
        self.btnBrainSegPath = QtWidgets.QToolButton(BrainExtraction)
        self.btnBrainSegPath.setObjectName("btnBrainSegPath")
        self.horizontalLayout_4.addWidget(self.btnBrainSegPath)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(BrainExtraction)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.LineOutput = QtWidgets.QLineEdit(BrainExtraction)
        self.LineOutput.setObjectName("LineOutput")
        self.horizontalLayout_5.addWidget(self.LineOutput)
        self.BtnChooseOutput = QtWidgets.QToolButton(BrainExtraction)
        self.BtnChooseOutput.setObjectName("BtnChooseOutput")
        self.horizontalLayout_5.addWidget(self.BtnChooseOutput)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.BtnStart = QtWidgets.QPushButton(BrainExtraction)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnStart.sizePolicy().hasHeightForWidth())
        self.BtnStart.setSizePolicy(sizePolicy)
        self.BtnStart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BtnStart.setObjectName("BtnStart")
        self.verticalLayout.addWidget(self.BtnStart)
        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(BrainExtraction)
        QtCore.QMetaObject.connectSlotsByName(BrainExtraction)

    def retranslateUi(self, BrainExtraction):
        _translate = QtCore.QCoreApplication.translate
        BrainExtraction.setWindowTitle(_translate("BrainExtraction", "Analysis&Data"))
        self.label_4.setText(_translate("BrainExtraction", "OriginImage"))
        self.btnImagePath.setText(_translate("BrainExtraction", "..."))
        self.label.setText(_translate("BrainExtraction", "Hippocumpus Mask"))
        self.btnHippoPath.setText(_translate("BrainExtraction", "..."))
        self.label_5.setText(_translate("BrainExtraction", "Feature Path"))
        self.btnFeaturePath.setText(_translate("BrainExtraction", "..."))
        self.label_6.setText(_translate("BrainExtraction", "BrainSeg Path"))
        self.btnBrainSegPath.setText(_translate("BrainExtraction", "..."))
        self.label_2.setText(_translate("BrainExtraction", "Output Path"))
        self.BtnChooseOutput.setText(_translate("BrainExtraction", "..."))
        self.BtnStart.setText(_translate("BrainExtraction", "Start Calculate!"))

