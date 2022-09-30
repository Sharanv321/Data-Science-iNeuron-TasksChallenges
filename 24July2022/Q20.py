# Q20) write a function by which you will be able to append two PDF files .

def appendPDFFiles(file1, file2):

    import PyPDF2

    # Open the files that have to be merged one by one
    pdf1File = open(file1, 'rb')
    pdf2File = open(file2, 'rb')

    # Read the files that you have opened
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()

    # Loop through all the pagenumbers for the first document
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # Loop through all the pagenumbers for the second document
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # Now that you have copied all the pages in both the documents, write them into the a new document
    pdfOutputFile = open('C://Users//shara//Desktop//Javascript//MergedFiles.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)

    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()

    appendPDFFiles('C://Users//shara//Desktop//Javascript//File1.pdf',
                   'C://Users//shara//Desktop//Javascript//File2.pdf')