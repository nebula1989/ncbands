import ezsheets

sheet_id = '18QjjiR0-wilPyaLMvY217OImu9eDmZlbaLpGS_BwjXU'
ss = ezsheets.Spreadsheet(sheet_id)
ss.refresh()
print(ss.title)

