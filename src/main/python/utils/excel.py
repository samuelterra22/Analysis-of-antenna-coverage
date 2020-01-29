import xlsxwriter


def to_excel(filename, title, data):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet("data")

    # Start from the first cell. Rows and columns are zero indexed.
    row = col = 0
    worksheet.write(row, col, title)

    row = 2

    # Iterate over the data and write it out row by row.
    for line in range(len(data)):
        col = 0
        for item in range(len(data[0])):
            worksheet.write(row, col, data[line][item])
            col += 1
        row += 1

    # Close file
    workbook.close()
