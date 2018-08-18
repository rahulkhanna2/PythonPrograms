from openpyxl import load_workbook
wb = load_workbook("ncs_id.xlsx")
sheet = wb.get_sheet_by_name("ncs_id")
final = {}
for i in range(2,59):
    row = "A" + str(i)
    col = "B" + str(i)
    #if ( ((sheet[row].value)!= None) and ((sheet[col].value)!= None) ):
        #final[sheet[row].value] = sheet[col].value
    if sheet[row].value == "2014CSA17":
        print row
