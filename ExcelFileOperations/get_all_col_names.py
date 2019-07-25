import xlrd

class ReadExcelData:
    def __init__(self, loc):
        self.loc = loc
    def get_test_data(self):
        wbook = xlrd.open_workbook(self.loc)
        sheet = wbook.sheet_by_name("Sheet1")
        ncols = sheet.ncols
        for i in range(ncols):
            print(sheet.cell_value(0,i))


obj = ReadExcelData("C:\\Users\\mallikar\\Documents\\Python_Workspace\\PyTest_Project"
                    "\\ExcelFileOperations\\TestData.xlsx")
obj.get_test_data()



"""
The above code is to read username and password data from excel sheet
step 1 : define location of file:
         loc = "fileLocation"
step 2 : open workbook:
         wbook = xlrd.open_workbook(loc)
step 3 : get sheet:
         sheet = wbook.sheet_by_index/name(index/name)
step 4 : get cell value:
         sheet.cell_value(rowNumber, colNumber)
"""