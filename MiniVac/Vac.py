import sys
import ctypes
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

# 메인윈도우
class M_Window(QMainWindow):
    # 검사결과 관련 클래스 변수
    split_rway = None
    split_rname = None
    report_handler = 0
    
    def __init__(self):
        super().__init__()

        # C 라이브러리 참조
        self.lib = ctypes.CDLL("./libs/lib_engine.so")

        # 라인
        self.v_Line = QFrame(self)
        self.h_Line = QFrame(self)

        # 버튼
        self.scan_Btn = QPushButton("검사시작", self)
        self.report_Btn = QPushButton("검사결과", self)
        self.exit_Btn = QPushButton("종료", self)

        # 라벨
        self.path_Label = QLabel(self)
        self.title_Label = QLabel(self)
        self.scan_Img = QLabel(self)
        self.report_Img = QLabel(self)
        self.exit_Img = QLabel(self)
        self.title_Img = QLabel(self)

        # 파일트리뷰
        self.path = "C:"
        self.index = None
        self.tv = QTreeView(self)
        self.model = QFileSystemModel(self)
        self.pname = None
        self.virus_num = 0

        # 메세지박스
        self.msgBox1 = QMessageBox(self)
        self.msgBox2 = QMessageBox(self)
        self.msgBox3 = QMessageBox(self)
        self.msgBox4 = QMessageBox(self)
        self.msgBox5 = QMessageBox(self)
        self.msgBox6 = QMessageBox(self)

        self.initUI()
    
    def initUI(self):
        # 메인윈도우 창 설정
        self.setWindowTitle("Baby Ratel")
        self.setGeometry(500, 400, 2000, 1300)
        self.setFixedSize(2000, 1300)
        self.setStyleSheet("QMainWindow{background-color: rgb(0, 0, 0);}")
        self.setWindowIcon(QIcon("./Img/ratel_Img.png"))

        # 메세지박스 스타일시트
        self.msgBox1.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox2.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox3.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox4.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox5.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox6.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        
        # 수직 라인
        self.v_Line.setGeometry(550, 40, 21, 1221)
        self.v_Line.setStyleSheet("background-color: line-rgb(255, 255, 255);")
        self.v_Line.setFrameShape(QFrame.VLine)
        self.v_Line.setFrameShadow(QFrame.Sunken)

        # 수평 라인
        self.h_Line.setGeometry(600, 260, 1361, 16)
        self.h_Line.setStyleSheet("background-color: line-rgb(255, 255, 255);")
        self.h_Line.setFrameShape(QFrame.HLine)
        self.h_Line.setFrameShadow(QFrame.Sunken)

        # 검사시작 버튼
        self.scan_Btn.setGeometry(40, 870, 311, 51)
        self.scan_Btn.setStyleSheet("background-color: rgb(139, 139, 139); color: rgb(255, 255, 255); font: 75 12pt \"HY강M\";")
        self.scan_Btn.clicked.connect(self.scan_clicked)

        # 검사시작 이미지
        self.scan_Img.setGeometry(400, 846, 100, 100)
        self.scan_Img.setPixmap(QtGui.QPixmap("./Img/scan_img.png"))

        # 검사결과 버튼
        self.report_Btn.setGeometry(40, 1020, 311, 51)
        self.report_Btn.setStyleSheet("background-color: rgb(139, 139, 139); color: rgb(255, 255, 255); font: 75 12pt \"HY강M\";")
        self.report_Btn.clicked.connect(self.report_clicked)

        # 검사결과 이미지
        self.report_Img.setGeometry(400, 996, 100, 100)
        self.report_Img.setPixmap(QtGui.QPixmap("./Img/report_img.png"))

        # 종료 버튼
        self.exit_Btn.setGeometry(40, 1160, 311, 51)
        self.exit_Btn.setStyleSheet("background-color: rgb(139, 139, 139); color: rgb(255, 255, 255); font: 75 12pt \"HY강M\";")
        self.exit_Btn.clicked.connect(self.exit_clicked)

        # 종료 이미지
        self.exit_Img.setGeometry(400, 1132, 100, 100)
        self.exit_Img.setPixmap(QtGui.QPixmap("./Img/exit_img.png"))

        # 경로 라벨
        self.path_Label.setGeometry(600, 120, 1001, 51)
        self.path_Label.setStyleSheet("color: rgb(255, 255, 255); font: 75 15pt \"HY강M\"; font-weight: bold;")
        self.path_Label.setText("검사 할 파일 : ")

        # 제목 라벨
        self.title_Label.setGeometry(40, 250, 521, 271)
        self.title_Label.setStyleSheet("color: rgb(255, 255, 255); font: 100 28pt \"HY견고딕\";")
        self.title_Label.setText("Baby Ratel")

        self.title_Img.setGeometry(40, 60, 300, 300)
        self.title_Img.setPixmap(QtGui.QPixmap("./Img/ratel_Img.png"))

        # 트리뷰 파일 탐색기
        self.model.setRootPath(self.path)
        self.tv.setModel(self.model)
        self.tv.setGeometry(600, 330, 1351, 931)
        self.tv.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tv.setColumnWidth(0, 500)
        self.tv.clicked.connect(self.setIndex)
        
        self.show()

    # 검사시작 버튼 클릭 이벤트
    def scan_clicked(self):
        if self.pname == None:
            self.msgBox1.critical(self.msgBox1, '오류', '검사할 파일을 선택해주세요.', QMessageBox.Ok)
        else:
            self.lib.init()
            M_Window.report_handler = 0
            path = self.pname
            e_Path = path.encode('utf-8')
            self.r_scan = self.lib.scan(e_Path)

            if self.r_scan == 1:
                file_num = self.lib.r_filenum()
                self.virus_num = self.lib.r_virusnum()
                self.msgBox2.information(self.msgBox2, '검사완료', '총 ' + str(file_num) + '개의 파일의 검사가 완료되었습니다.', QMessageBox.Ok)
                self.msgBox4.information(self.msgBox4, '검사완료', str(self.virus_num) + '개의 파일이 검출되었습니다.', QMessageBox.Ok)
                rway = self.lib.r_way()
                d_rway = ctypes.c_char_p(rway).value.decode('utf-8')
                M_Window.split_rway = d_rway.split(',')
                rname = self.lib.r_name()
                d_rname = ctypes.c_char_p(rname).value.decode('utf-8')
                M_Window.split_rname = d_rname.split(',')

                if self.virus_num != 0:
                    ans = self.msgBox5.information(self.msgBox5, '검사완료', '검사결과를 보시겠습니까?', QMessageBox.Yes | QMessageBox.No)

                    if ans == QMessageBox.Yes:
                        self.report_clicked()

    # 검사결과 버튼 클릭 이벤트
    def report_clicked(self):
        if self.virus_num != 0 and M_Window.report_handler != 1:
            Sub_Window(self)
        else:
            self.msgBox6.warning(self.msgBox6, '오류', '검사결과가 없습니다.', QMessageBox.Ok)

    # 종료 버튼 클릭 이벤트
    def exit_clicked(self):
        ans = self.msgBox3.question(self.msgBox3, "종료", "종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            sys.exit()

    # 경로 설정
    def setIndex(self, index):
        self.index = index
        self.pname = self.model.filePath(self.index)
        self.path_Label.setText("검사 할 파일 : " + self.pname)
        
    def r_way(self):
        return M_Window.split_rway

    def r_name(self):
        return M_Window.split_rname

    # 삭제 이벤트
    def remove_report(self, v):
        del M_Window.split_rname[v]
        del M_Window.split_rway[v]

    # 전체삭제 이벤트
    def removeAll_report(self):
        del M_Window.split_rway
        del M_Window.split_rname
        M_Window.report_handler = 1
        
            
# 검사결과 창
class Sub_Window(QDialog):
    def __init__(self, parent):
        super(Sub_Window, self).__init__(parent)

        # 결과(테이블)
        self.report = QTableWidget(self)
        self.column = 2
        self.row = parent.virus_num
        self.column_Headers = ['이름', '경로']

        # 버튼
        self.delete_Btn = QPushButton("삭제", self)
        self.deleteAll_Btn = QPushButton("전체삭제", self)
        
        # 메세지박스
        self.msgBox1 = QMessageBox(self)
        self.msgBox2 = QMessageBox(self)
        self.msgBox3 = QMessageBox(self)
        self.msgBox4 = QMessageBox(self)
        self.msgBox5 = QMessageBox(self)

        # 이름, 경로
        self.way = parent.r_way()
        self.name = parent.r_name()
        self.delete_idx = None
        self.x = None

        self.initUI()

    def initUI(self):
        # 결과 창 설정
        self.setWindowTitle("검사결과")
        self.setGeometry(1000, 800, 1000, 700)
        self.setFixedSize(1000, 700)
        self.setStyleSheet("QDialog {background-color: rgb(0, 0, 0);}")

        #메세지 박스 스타일시트
        self.msgBox1.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox2.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox3.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox4.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        self.msgBox5.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
        
        # 테이블 설정
        self.report.setGeometry(30, 30, 940, 540)
        self.report.setColumnCount(self.column)
        self.report.setRowCount(self.row)
        self.report.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.report.setHorizontalHeaderLabels(self.column_Headers)
        for k, v in enumerate(self.name):
            col = 0
            item = QTableWidgetItem(v)
            self.report.setItem(k, col, item)
        for k, v in enumerate(self.way):
            col = 1
            item = QTableWidgetItem(v)
            self.report.setItem(k, col, item)
        self.report.setColumnWidth(1, 706)
        
        # 삭제 버튼
        self.delete_Btn.setGeometry(660, 600, 311, 51)
        self.delete_Btn.setStyleSheet("background-color: rgb(139, 139, 139); color: rgb(255, 255, 255); font: 75 12pt \"HY강M\";")
        self.report.cellClicked.connect(self.cell_clicked)
        self.delete_Btn.clicked.connect(self.delete_clicked)

        # 전체삭제 버튼
        self.deleteAll_Btn.setGeometry(335, 600, 311, 51)
        self.deleteAll_Btn.setStyleSheet("background-color: rgb(139, 139, 139); color: rgb(255, 255, 255); font: 75 12pt \"HY강M\";")
        self.deleteAll_Btn.clicked.connect(self.deleteAll_clicked)
        
        self.show()
        
    # 테이블 클릭 이벤트
    def cell_clicked(self):
        self.x = self.report.selectedIndexes()
        if self.x[0].column() == 0:
            self.msgBox1.critical(self.msgBox1, '오류', '파일 경로를 선택해주십시오.', QMessageBox.Ok)
        self.delete_idx = self.report.item(self.x[0].row(), self.x[0].column()).text()
        # 디버그 : print(self.delete_idx)

    # 삭제 버튼 클릭 이벤트
    def delete_clicked(self):
        if self.delete_idx == None:
            self.msgBox1.warning(self.msgBox1, '오류', '선택된 파일이 없습니다', QMessageBox.Ok)
        else:
            ans = self.msgBox2.question(self.msgBox2, '삭제', '선택된 파일을 삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)

            if ans == QMessageBox.Yes:
                os.remove(self.delete_idx)
                self.report.removeRow(self.x[0].row())
                M_Window().remove_report(self.x[0].row())
                self.msgBox3.information(self.msgBox3, '삭제완료', '선택된 파일이 삭제 완료되었습니다.', QMessageBox.Ok)

    # 전체 삭제 버튼 클릭 이벤트
    def deleteAll_clicked(self):
        ans = self.msgBox4.question(self.msgBox4, '전체삭제', '전체 파일을 삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)

        if ans == QMessageBox.Yes:
            for i in range(self.row):
                col = 1
                remove_way = self.report.item(i, col).text()
                os.remove(remove_way)
            self.report.clearContents()
            M_Window().removeAll_report()
            self.msgBox5.information(self.msgBox5, '삭제완료', '파일 삭제가 완료되었습니다.', QMessageBox.Ok)

if __name__ == '__main__':
    os.chdir(os.getcwd())
    app = QApplication(sys.argv)
    ex = M_Window()
    sys.exit(app.exec_())
