import xlrd
import xlwt

def filter(path):
    book = xlrd.open_workbook(path)

    out_book =xlwt.Workbook()
    out_sheet = out_book.add_sheet('sheet1')
    
    sheet = book.sheet_by_index(0)

    rows_count = sheet.nrows
    cols_count =  sheet.ncols
    
    out_row_count=0
    for x in range(rows_count):
        if(int(sheet.cell(x,3).value)==1):
            #print(int(sheet.cell(x,3).value))
            print(str(sheet.cell(x,4).value)+"\t\t"+str(int(sheet.cell(x,5).value))+"\t\t"+str(int(sheet.cell(x,6).value)))
            out_sheet.write(out_row_count,0,str(sheet.cell(x,4).value))
            out_sheet.write(out_row_count,1,str(int(sheet.cell(x,5).value)))
            out_sheet.write(out_row_count,2,str(int(sheet.cell(x,6).value)))
            out_row_count = out_row_count + 1 
    out_book.save('output.xls') 
            
            
    x = input()



filter("Input0.xlsx")
