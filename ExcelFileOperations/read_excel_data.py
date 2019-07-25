import xlrd

class ReadExcelData:
    def __init__(self, loc):
        self.loc = loc
    def get_test_data(self, rowNum, colNum):
        wbook = xlrd.open_workbook(self.loc)
        sheet = wbook.sheet_by_name("Sheet1")
        value = sheet.cell_value(rowNum, colNum)
        return value

obj = ReadExcelData("C:\\Users\\mallikar\\Documents\\Python_Workspace\\PyTest_Project"
                    "\\ExcelFileOperations\\TestData.csv")
uname = obj.get_test_data(1,0)
upwd = obj.get_test_data(1,1)
print(f"Username and password details are : {uname} : {upwd}")


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