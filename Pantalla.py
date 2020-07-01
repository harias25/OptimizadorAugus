import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
import re
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from Optimizador.Optimizador import Optimizador


class Ui_MainWindow(object):

    resultChanged = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameCodigo = QtWidgets.QFrame(self.centralwidget)
        self.frameCodigo.setGeometry(QtCore.QRect(0, 30, 500, 675))
        self.frameCodigo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCodigo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCodigo.setObjectName("frameCodigo")

        self.frameCodigo2 = QtWidgets.QFrame(self.centralwidget)
        self.frameCodigo2.setGeometry(QtCore.QRect(505, 30, 500, 675))
        self.frameCodigo2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCodigo2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCodigo2.setObjectName("frameCodigo")

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 1001, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuPrograma = QtWidgets.QMenu(self.menubar)
        self.menuPrograma.setObjectName("menuPrograma")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionArbir = QtWidgets.QAction(MainWindow)
        self.actionArbir.setObjectName("actionArbir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionCerrrar = QtWidgets.QAction(MainWindow)
        self.actionCerrrar.setObjectName("actionCerrrar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCopiar = QtWidgets.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionPegar = QtWidgets.QAction(MainWindow)
        self.actionPegar.setObjectName("actionPegar")
        self.actionCortar = QtWidgets.QAction(MainWindow)
        self.actionCortar.setObjectName("actionCortar")
        self.actionBuscar = QtWidgets.QAction(MainWindow)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionReemplazar = QtWidgets.QAction(MainWindow)
        self.actionReemplazar.setObjectName("actionReemplazar")
       
        self.actionEjecutar_Ascendente = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_Ascendente.setObjectName("actionEjecutar_Ascendente")
        
        self.actionTabla_de_Simbolos = QtWidgets.QAction(MainWindow)
        self.actionTabla_de_Simbolos.setObjectName("actionTabla_de_Simbolos")
    

        self.actionAyuda = QtWidgets.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcercaDe = QtWidgets.QAction(MainWindow)
        self.actionAcercaDe.setObjectName("actionAcercaDe")

        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionArbir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrrar)
        self.menuArchivo.addAction(self.actionSalir)

        self.menuPrograma.addAction(self.actionEjecutar_Ascendente)
        self.menuReportes.addAction(self.actionTabla_de_Simbolos)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcercaDe)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuPrograma.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())


        self.__myFont = QFont()
        self.__myFont.setPointSize(12)
        #************************************************ REGLAS DEL LENGUAJE AUGUS *****************************************
        self.editor = QsciScintilla()
        self.editor.setText("")              
        self.editor.setLexer(None)           
        self.editor.setUtf8(True)             
        self.editor.setFont(self.__myFont)    

        #AJUSTES DE TEXTO
        self.editor.setWrapMode(QsciScintilla.WrapWord)
        self.editor.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.editor.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        #FIN DE LINEA
        self.editor.setEolMode(QsciScintilla.EolWindows)
        self.editor.setEolVisibility(False)

        #SANGRIA
        self.editor.setIndentationsUseTabs(False)
        self.editor.setTabWidth(4)
        self.editor.setIndentationGuides(True)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)

        self.editor.setCaretForegroundColor(QColor("#ff0000ff"))
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.editor.setCaretWidth(2)

        # MARGENES
        self.editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.editor.setMarginWidth(0, "0000")  #con este se puede quitar la linea
        self.editor.setMarginsForegroundColor(QColor("#ff888888"))

        #**************************************** CODIGO OPTMIZADO *****************************************************
        self.consola = QsciScintilla()
        self.consola.setText("")              
        self.consola.setLexer(None)           
        self.consola.setUtf8(True)             
        self.consola.setFont(self.__myFont)    

        #AJUSTES DE TEXTO
        self.consola.setWrapMode(QsciScintilla.WrapWord)
        self.consola.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.consola.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        #FIN DE LINEA
        self.consola.setEolMode(QsciScintilla.EolWindows)
        self.consola.setEolVisibility(False)

        #SANGRIA
        self.consola.setIndentationsUseTabs(False)
        self.consola.setTabWidth(4)
        self.consola.setIndentationGuides(True)
        self.consola.setTabIndents(True)
        self.consola.setAutoIndent(True)

        self.consola.setCaretForegroundColor(QColor("#ff0000ff"))
        self.consola.setCaretLineVisible(True)
        self.consola.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.consola.setCaretWidth(2)

        # MARGENES
        self.consola.setMarginType(0, QsciScintilla.NumberMargin)
        self.consola.setMarginWidth(0, "0000")  #con este se puede quitar la linea
        self.consola.setMarginsForegroundColor(QColor("#ff888888"))

        self.__lexer2 = QsciLexerRuby(self.consola)
        self.consola.setLexer(self.__lexer2)

        self.__lyt2 = QVBoxLayout()
        self.frameCodigo2.setLayout(self.__lyt2)
        self.__lyt2.addWidget(self.consola)


        #SE COLOCAN LAS REGLAS DEL EDITOR
        self.__lexer = QsciLexerRuby(self.editor)
        self.editor.setLexer(self.__lexer)

        self.__lyt = QVBoxLayout()
        self.frameCodigo.setLayout(self.__lyt)
        self.__lyt.addWidget(self.editor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionNuevo.triggered.connect(self.clean)
        self.actionArbir.triggered.connect(self.open)
        self.actionGuardar.triggered.connect(self.save)
        self.actionGuardar_Como.triggered.connect(self.save_as)
        self.actionCerrrar.triggered.connect(self.clear)
        self.actionSalir.triggered.connect(self.exit)
        self.ruta_archivo  = None
        self.actionEjecutar_Ascendente.triggered.connect(self.ascendente)
        #self.actionEjecutar_Descendente.triggered.connect(self.descendente)
        self.actionTabla_de_Simbolos.triggered.connect(self.generarTabla)

        #self.ts_global = TS.Entorno(None)
        #self.ast =  AST.AST([]) 
        self.listado_gramatical = []
        self.instrucciones = []
        self.hilo_terminado = True

        

    def clean(self):
        self.ruta_archivo = None
        self.editor.setText("")
        self.consola.clear()

    def generarTabla(self):
        pass

    def ascendente(self):
        optimizador = Optimizador()
        optimizador.optimizar(self)

    def exit(self):
        sys.exit()

    def clear(self):
        self.ruta_archivo = None
        self.editor.setText("")

    def open(self):
        root = tk.Tk()
        root.withdraw()
        ruta = filedialog.askopenfilename(title="Seleccione un archivo de Entrada")
        if not ruta: return
        try:
            f = open(ruta,"r")
            input = f.read()
            self.editor.setText(input)
            f.close()
            self.ruta_archivo = ruta
        except Exception as e:
            raise
            QMessageBox.critical(self.centralwidget,'Error Cargando el Archivo', 'No es posible abrir el archivo: %r' % ruta)

    def save(self):
        if(self.ruta_archivo==None):
            root = tk.Tk()
            root.withdraw()
            ruta = filedialog.asksaveasfilename(title="Seleccione la ruta donde desea guardar el Archivo",filetypes=[('all files', '.*'), ('text files', '.txt')])
        else:
            ruta = self.ruta_archivo
        if not ruta: return
        try:
            f = open(ruta,"w")
            f.write(self.editor.text())
            f.close()
        except Exception as e:
            raise
            QMessageBox.critical(self.centralwidget,'Error Guardando el Archivo', 'No es posible guardar el archivo: %r' % ruta)

    def save_as(self):
        ruta = filedialog.asksaveasfilename(title="Seleccione la ruta donde desea guardar el Archivo",filetypes=[('all files', '.*'), ('text files', '.txt')])
        if not ruta: return
        try:
            f = open(ruta,"w")
            f.write(self.editor.text())
            f.close()
            self.ruta_archivo = ruta
        except Exception as e:
            raise
            QMessageBox.critical(self.centralwidget,'Error Guardando el Archivo', 'No es posible guardar el archivo: %r' % ruta)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IDE OPTIMIZADOR AUGUS - HAROLDO PABLO ARIAS MOLINA - 201020247"))
        #self.consola.setText(_translate("MainWindow", ""))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuPrograma.setTitle(_translate("MainWindow", "Programa"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionArbir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como"))
        self.actionCerrrar.setText(_translate("MainWindow", "Cerrrar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))

        
        self.actionEjecutar_Ascendente.setText(_translate("MainWindow", "Optimizar"))
       
        self.actionTabla_de_Simbolos.setText(_translate("MainWindow", "Reporte de Optimización"))
       

        self.actionAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.actionAcercaDe.setText(_translate("MainWindow", "Acerca de"))

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**9)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint)
    MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    interfaz = ui
    MainWindow.show()
    sys.exit(app.exec_())


