import xlrd
# from Testssmeoa.cases.test_notice import cass
class readExcel:
    def read(self,path,index=0):
        book=xlrd.open_workbook(path)
        sheet=book.sheets()[index]
        return sheet
    def get_source(self):
        s=self.read('\\Users\\Administrator\\Desktop\\test.xlsx')
        return s
if __name__=='__main__':
    s=readExcel().read('C:\\Users\\Administrator\\Desktop\\test.xlsx')
    # print(s.cell(1,3).value) #在指定单元格获取内容
    for i in range(1,s.nrows):
        list= s.row_values(i)
        newlist = list[2:10]
        print(newlist)
       # test_notice().count(newlist) #执行公告管理新增


