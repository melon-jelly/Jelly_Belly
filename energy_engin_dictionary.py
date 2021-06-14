from tkinter import *
import pandas as pd
import os
global dat


print(os.getcwd())

dat = pd.read_excel("./energy_engin_dic.xlsx")


def click():
    print("버튼이 클릭되었습니다.")
    word = entry.get()
    output.delete(0.0, END)
    print("{}을 검색했습니다".format(word))
    try:
        def_word = dat.loc[dat['한글명'] == word, '내용'].values[0]
    except:
        def_word = "단어의 뜻을 찾을 수 없음."

    output.insert(END, def_word)

window = Tk()
window.title("발전용어사전")

label = Label(window, text="원하는 단어 입력 후 엔터를 눌러주세요")
label.grid(row=0, column=0, sticky=W)

entry = Entry(window, width=15, bg='light green')
entry.grid(row=1,column=0,sticky=W)

btn = Button(window, text = "제출", width=5, command =click)
btn.grid(row=2,column=0,sticky=W)

label2 = Label(window, text ="\n의미:")
label2.grid(row=3, column=0, sticky=W)

output = Text(window, width=50, height=6, wrap=CHAR, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 메인 반복문 실행
window.mainloop()

