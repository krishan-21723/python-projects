import pyttsx3
import PyPDF2

book = open('file.pdf', 'rb')  # change file name and location
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print (pages)
speaker = pyttsx3.init()
for page in range(pages):
    page = pdfReader.getPage(page);
    text = page.extractText();
    speaker.say(text)

speaker.runAndWait()
