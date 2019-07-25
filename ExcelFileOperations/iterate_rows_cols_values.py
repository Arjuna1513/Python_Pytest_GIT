import xlrd

class ReadExcelData:
    def __init__(self, loc):
        self.loc = loc
    def get_test_data(self):
        wbook = xlrd.open_workbook(self.loc)
        sheet = wbook.sheet_by_name("Sheet1")
        rows = sheet.nrows
        cols = sheet.ncols
        return rows,cols

    def get_sheet(self):
        wbook = xlrd.open_workbook(self.loc)
        sheet = wbook.sheet_by_name("Sheet1")
        return sheet

    def display_rows_cols_values(self):
        sheet = self.get_sheet()
        rows,cols = self.get_test_data()
        for i in range(1, rows):
            for j in range(cols):
                print(sheet.cell_value(i,j))

obj = ReadExcelData("C:\\Users\\mallikar\\Documents\\Python_Workspace\\PyTest_Project"
                    "\\ExcelFileOperations\\TestData.xlsx")
obj.display_rows_cols_values()

"""
here get_test_data() returns 2 values i.e. total rows and total columns
and when we call obj.get_user_data() it returns tuple of values and that tuple is unzipped using
rows, cols = obj.get_user_data()
"""


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