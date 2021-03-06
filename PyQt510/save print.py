#conding=utf-8

'''
这是一个关于文本保存以及打印文件相关对话框的小例子!
文章链接：http://www.xdbcb8.com/archives/281.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog, QDialog
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter

class Example(QWidget):
    '''
    文本保存以及打印文件对话框
    '''
    def __init__(self):
        '''
        一些初始设置
        '''
        super().__init__()
        self.printer = QPrinter()
        self.initUI()
    
    def initUI(self):
        '''
        界面初始设置
        '''
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('关注微信公众号：学点编程吧--保存、打印文件')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)
        
        self.bt1 = QPushButton('打开文件', self)
        self.bt1.move(350, 20)
        self.bt2 = QPushButton('打开多个文件', self)
        self.bt2.move(350, 70)
        self.bt3 = QPushButton('选择字体', self)
        self.bt3.move(350, 120)
        self.bt4 = QPushButton('选择颜色', self)
        self.bt4.move(350, 170)
        self.bt5 = QPushButton('保存文件', self)
        self.bt5.move(350, 220)
        self.bt6 = QPushButton('页面设置', self)
        self.bt6.move(350, 270)
        self.bt7 = QPushButton('打印文档', self)
        self.bt7.move(350, 320)
        
        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.openfiles)
        self.bt3.clicked.connect(self.choicefont)
        self.bt4.clicked.connect(self.choicecolor)
        self.bt5.clicked.connect(self.savefile)
        self.bt6.clicked.connect(self.pagesettings)
        self.bt7.clicked.connect(self.printdialog)
        
        self.show()
    
    def openfile(self):
        '''
        打开文件对话框
        '''
        fname = QFileDialog.getOpenFileName(self, '学点编程吧:打开文件', './')
        if fname[0]:
            # fname[0]绝对路径
            with open(fname[0], 'r', encoding='gb18030', errors='ignore') as f:
                self.tx.setText(f.read())
                
    def openfiles(self):
        '''
        打开多个文件对话框
        '''
        fnames = QFileDialog.getOpenFileNames(self, '学点编程吧:打开多个文件', './')#注意这里返回值是元组
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname, 'r', encoding='gb18030', errors='ignore') as f:
                    self.tx.append(f.read())#读取的文件附加到之前的文件之后
                
    def choicefont(self):
        '''
        字体选择对话框
        '''
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)
        
    def choicecolor(self):
        '''
        颜色选择对话框
        '''
        col = QColorDialog.getColor()

        if col.isValid():
            self.tx.setTextColor(col)
            
    def savefile(self):
        '''
        文件保存对话框
        '''
        fileName = QFileDialog.getSaveFileName(self, '学点编程吧:保存文件', './', "Text files (*.txt)")
        #增加一个过滤器，以便仅显示与过滤器匹配的文件
        if fileName[0]:
            with open(fileName[0], 'w', encoding='gb18030', errors='ignore') as f:
                f.write(self.tx.toPlainText())#获取的QTextEdit的内容使用toPlainText()函数

    def pagesettings(self):
        '''
        页面设置对话框
        '''
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec_()

    def printdialog(self):
        '''
        打印机配置的对话框
        '''
        printdialog = QPrintDialog(self.printer, self)#QPrintDialog类提供了一个用于指定打印机配置的对话框
        if QDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)#选择好打印机后，点击打印，调用QTextEdit中的print方法进行相关的打印。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())