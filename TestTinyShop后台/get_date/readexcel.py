import  xlrd
class readExcel:
    def read(self,path,index=0):
        book=xlrd.open_workbook(path)
        sheet=book.sheets()[index]
        return sheet
    def get_source(self):
        s=self.read('\\Users\\Administrator\\Desktop\\test1.xls')
        return s
if __name__=='__main__':
    s=readExcel().get_source()