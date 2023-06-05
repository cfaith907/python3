import xlrd
# file location
loc = ("c:\\Users\\connor.faith\\Desktop\\tests.xls")# open file
xfile = xlrd.open_workbook(loc)# 0 is the index of sheet in file i.e. 1st sheet
# We can read 3rd sheet if our file had multiple sheets like this: xfile.sheet_by_index(2)
sheet = xfile.sheet_by_index(0)

# print numb of rows
print("there are %i rows" % sheet.nrows) 

# define empty array
duplicates = []
bin_pallet = [] 

# loop through all rows
for i in range(sheet.nrows):
    # get value of current column sheet.cell_value(i, 0) or i, 1 etc
    value = sheet.cell_value(i, 0)

    # check if value already exits
    # if true, add to dupes array
    # if false, at too notdupes **
    if value in bin_pallet:
        duplicates.append(sheet.cell_value(i, 0))
    else:
        bin_pallet.append(sheet.cell_value(i, 0))
        
print("%i duplicate/s found" % len(duplicates))
# return how many dupes identified 
print(duplicates)
# return duplicates themselves 