import xlrd


class Excel:
    def read_it(self,path,index=0):
        book=xlrd.open_workbook(path)
        sheet=book.sheets()[index]
        return  sheet
s=Excel().read_it('G:\\XUE GOD 2019\\111.xlsx')

for i in range(1,s.nrows):
   list = s.row_values(i)
   print(list[0:3])