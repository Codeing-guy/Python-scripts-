##from selenium import webdriver
##
##driver=webdriver.Chrome()
##driver.get()
##driver.close()


#code for opening yt if no arguments are passed else open whatsapp or yt with some search content
import webbrowser ,sys #,pyperclip

sys.argv
if len(sys.argv) >1 and sys.argv[1]=='wa':
    webbrowser.open('https://web.whatsapp.com')
elif len(sys.argv) >1:
    searchIteam=' '.join(sys.argv[1:])
    webbrowser.open('https://www.youtube.com/results?search_query='+searchIteam)
##elif len(pyperclip.paste())>0:
##    searchIteam=pyperclip.paste()
##    webbrowser.open('https://www.youtube.com/results?search_query='+searchIteam)
else:
     webbrowser.open('https://www.youtube.com')

