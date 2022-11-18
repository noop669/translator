from tkinter import *
from tkinter import ttk
import requests as r2

root = Tk()
root.title('Переводчик')
root.geometry('730x480')
root.resizable(width=False, height=False)
rBtn = IntVar()


def translater():
        if (rBtn.get() == 0):
            translator = []
        elif (rBtn.get() == 1):
            translator = []
        txt = pole.get('0.0', END)
        w = translator.translate(txt)
        w = translator.delete('1.0', END)
        poleTranslate.delete('1.0', 'end')
        poleTranslate.insert('1.0', w)
def translater():
    URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
    URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
    KEY = 'MTY2ZTcxNTQtZWQ1OC00NWI4LWI0MGEtNDg4ZDNkYmRjZTk0OjJjYjVmODM4ZTBlMDRjNmE5NGVhMjMzYTE1ZGYxNzJl'
    headers_auth = {'Authorization': 'Basic ' + KEY}
    auth = r2.post(URL_AUTH, headers= headers_auth)
    if auth.status_code == 200:
        token = auth.text 
        txt = pole.get('0.0', END)    
        if txt:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': txt,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = r2.get(URL_TRANSLATE, headers = headers_translate, params = params)
            res = r.json()
            try:
                return(poleTranslate.insert('1.0', res["Translation"]["Translation"]))
            except:
                return('Not found translation')
        else:
            return('Error!')  

#поле ввода
pole = Text(root, width=80, height=10, font='Arial, 13')
pole.pack(pady=10)

#кнопка со значением 0
algo01 = Radiobutton(root, text="Перевод на русский", 
variable=rBtn, value=0, font='Arial, 12')
algo01.place(x=50, y=215)

#кнопка перевода
Btn = ttk.Button(root, text="Перевести", command=translater)
Btn.pack()

#кнопка со значением 1
algo02 = Radiobutton(root, text="Перевод на английский", 
variable=rBtn, value=1, font='Arial, 12')
algo02.place(x=430, y=215)

#поле вывода
poleTranslate = Text(root, width=80, height=10, font='Arial, 13')
poleTranslate.pack(pady = 10)

root.mainloop()