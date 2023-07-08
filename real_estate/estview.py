import sys
import io
import os
import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
import subprocess

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
'''
self.gu = {'남구' : 1, '달서구' : 2, '달성군' : 3, '동구': 4, '북구' : 5, '서구' : 6, '수성구': 7, '중구' : 8}
        self.dong = 
        1남구[['대명동', '봉덕동', '이천동'],
        2달서구['갈산동', '감삼동', '대곡동', '대천동', '도원동', '두류동', '본동', '본리동', '상인동', '성당동', '송현동', '신당동', '용산동', '월성동', '월암동', '유천동', '이곡동', '장기동', '장동', '죽전동', '진천동', '파호동', '호림동', '호산동'],
        3달성군['가창면', '구지면', '논공읍', '다사읍', '옥포읍', '유가읍', '하빈면', '현풍읍', '화원읍'],
        4동구['각산동', '검사동', '괴전동', '금강동', '내곡동', '내동', '능성동', '대림동', '덕곡동', '도동', '도학동', '동내동', '동호동', '둔산동', '매여동', '미곡동', '미대동', '방촌동', '백안동', '봉무동', '부동', '불로동', '사복동', '상매동', '서호동', '송정동', '숙천동', '신기동', '신무동', '신서동', '신암동', '신용동', '신천동', '신평동', '용계동', '용수동', '율암동', '율하동', '입석동', '중대동', '지묘동', '지저동', '진인동', '평광동', '효목동'],
        5북구['검단동', '고성동1가', '고성동2가', '고성동3가', '관음동', '구암동', '국우동', '금호동', '노곡동', '노원동1가', '노원동2가', '노원동3가', '대현동', '도남동', '동변동', '동천동', '동호동', '매천동', '복현동', '사수동', '산격동', '서변동', '연경동', '읍내동', '조야동', '칠성동1가', '칠성동2가', '침산동', '태전동', '팔달동', '학정동'],
        6서구['내당동', '비산동', '상리동', '원대동1가', '원대동2가', '원대동3가', '이현동', '중리동', '평리동'],
        7수성구['가천동', '고모동', '노변동', '대흥동', '두산동', '만촌동', '매호동', '범물동', '범어동', '사월동', '삼덕동', '상동', '성동', '수성동1가', '수성동2가', '수성동3가', '수성동4가', '시지동', '신매동', '연호동', '욱수동', '이천동', '중동', '지산동', '파동', '황금동'],
        8중구['계산동1가', '계산동2가', '공평동', '교동', '남산동', '남성로', '남일동', '달성동', '대봉동', '대신동', '대안동', '덕산동', '도원동', '동문동', '동산동', '동성로1가', '동성로2가', '동성로3가', '동인동1가', '동인동2가', '동인동3가', '동인동4가', '동일동', '문화동', '봉산동', '북내동', '북성로1가', '북성로2가', '사일동', '삼덕동1가', '삼덕동2가', '삼덕동3가', '상덕동', '상서동', '서내동', '서문로1가', '서문로2가', '서성로1가', '서성로2가', '서야동', '수동', '수창동', '시장북로', '완전동', '용덕동', '인교동', '장관동', '전동', '종로1가', '종로2가', '태평로1가', '태평로2가', '태평로3가', '포정동', '하서동', '향촌동', '화전동']]
'''
# 나눔고딕 폰트 경로
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

# 나눔고딕 폰트 설정
font_prop = fm.FontProperties(fname=font_path)




#######################################################################################################33
#버튼1 남구
def run_program():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "namgu남구":
            hidden_button.place_forget()#히든버튼1
            hidden_button2.place_forget()#히든버튼2
            hidden_button3.place_forget()#히든버튼3
#버튼1-1 # 만약 hidden_button이 보이는 상태이면서 hidden_button이 클릭된 상태라면
def hidden_button_click():
    #global hidden_button
    filename = "song.py"  # 실행시킬 파이썬 파일명
    subprocess.Popen(["python", filename])  # 파이썬 파일 실행
        #버튼의 텍스트를 변경하고, 버튼을 활성화함
    hidden_button.configure(text="버튼이 클릭되었습니다.", state="normal")
    #hidden_button.configure(text="버튼이 클릭되었습니다.", state="disabled")
#버튼1-2
def hidden_button_click2():
    #global hidden_button
    filename = "song.py"  # 실행시킬 파이썬 파일명
    subprocess.Popen(["python", filename])
    hidden_button.configure(text="버튼이 클릭되었습니다.", state="normal")
#버튼1-3
def hidden_button_click3():
    filename = "song.py"  # 실행시킬 파이썬 파일명
    subprocess.Popen(["python", filename])
    hidden_button.configure(text="버튼이 클릭되었습니다.", state="normal")

#################################################################################################################3
#버튼2달서구
def run_program2():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button2_1.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button2_2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button2_3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "Dalseo달서구":
            hidden_button2_1.place_forget()#히든버튼1
            hidden_button2_2.place_forget()#히든버튼2
            hidden_button3_3.place_forget()#히든버튼3
#################################################################################################################3
#버튼3달성군 Dalseong달성군
def run_program3():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button3_1.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button3_2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button3_3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "Dalseo달서구":
            hidden_button3_1.place_forget()#히든버튼1
            hidden_button3_2.place_forget()#히든버튼2
            hidden_button3_3.place_forget()#히든버튼3

#################################################################################################################3
#버튼4동구 Donggu동구
def run_program4():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button4_1.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button4_2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button4_3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "Donggu동구":
            hidden_button4_1.place_forget()#히든버튼1
            hidden_button4_2.place_forget()#히든버튼2
            hidden_button4_3.place_forget()#히든버튼3
#################################################################################################################3
#버튼5북구 Bukgu북구
def run_program5():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button5_1.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button5_2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button5_3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "Bukgu북구":
            hidden_button5_1.place_forget()#히든버튼1
            hidden_button5_2.place_forget()#히든버튼2
            hidden_button5_3.place_forget()#히든버튼3
#################################################################################################################3
#버튼6서구 Seogu서구
def run_program6():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button6_1.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button6_2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button6_3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "Seogu서구":
            hidden_button6_1.place_forget()#히든버튼1
            hidden_button6_2.place_forget()#히든버튼2
            hidden_button6_3.place_forget()#히든버튼3
#################################################################################################################3
#버튼7수성구 Suseong수성구
def run_program7():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button7_1.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button7_2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button7_3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "Suseong수성구":
            hidden_button7_1.place_forget()#히든버튼1
            hidden_button7_2.place_forget()#히든버튼2
            hidden_button7_3.place_forget()#히든버튼3
#################################################################################################################3
#버튼8중구 Jung-gu중구
def run_program8():
    #global hidden_button #이건 왜 전역번슈?
    # 만약 hidden_button이 보이지 않는 상태라면
    if not hidden_button.winfo_viewable():
        hidden_button8_1.place(relx=0.8, rely=0.2, anchor=tk.CENTER)  # hidden_button-1 보이기
        hidden_button8_2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)  # hidden_button-2 보이기
        hidden_button8_3.place(relx=0.8, rely=0.6, anchor=tk.CENTER)  # hidden_button-3 보이기
    # 원래 버튼을 눌렀을 때 hidden_button이 보이는 상태이면 숨기기
    elif run_button["text"] == "Jung-gu중구":
            hidden_button8_1.place_forget()#히든버튼1
            hidden_button8_2.place_forget()#히든버튼2
            hidden_button8_3.place_forget()#히든버튼3

##############################################################################################################
class RoundedCanvas(tk.Canvas):
    def create_rounded_rectangle(self, x1, y1, x2, y2, **kwargs):
        radius = kwargs.pop('radius', 5)
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True)

root = tk.Tk()
root.geometry("600x500")  # 윈도우 크기 지정
root.configure(bg='#7f8c8d') # 전체 배경색 진한 남색으로 설정

# 한글 폰트 지정
font_name = "NanumGothic"
font_size = 12
tk_font = Font(family=font_name, size=font_size)
#font_name = "NanumGothic"
#tk_font = Font(root, family=font_name)

#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')  # utf-8 한글 설정
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 스타일 지정
style = ttk.Style()
style.theme_use("default")
style.configure("Title.TLabel", font=tk_font, foreground="white", background="#3B3B3B", padding=10)

# 창 제목 설정
root.title("부동산")

# 창 제목 레이블 생성
title_label = ttk.Label(root, text="부동산", style="Title.TLabel")
title_label.pack(side="top", fill="x")

# 둥근 사각형 생성
canvas = RoundedCanvas(root, width=600, height=500, bg='#c9c9c9', highlightthickness=0)#새창색갈변경bgfill
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
canvas.create_rounded_rectangle(0, 0, 600, 500, fill='#c9c9c9', outline='white', width=5, radius=25)


#버튼 설정
# 맥북 창 색상
macbook_color = "#c0c0c0"

# 버튼 색상
button_color = "#7f8c8d"
'''
self.gu = {'남구' : 1, '달서구' : 2, '달성군' : 3, '동구': 4, '북구' : 5, '서구' : 6, '수성구': 7, '중구' : 8}
        self.dong = 
        1남구[['대명동', '봉덕동', '이천동'],
        2달서구['갈산동', '감삼동', '대곡동', '대천동', '도원동', '두류동', '본동', '본리동', '상인동', '성당동', '송현동', '신당동', '용산동', '월성동', '월암동', '유천동', '이곡동', '장기동', '장동', '죽전동', '진천동', '파호동', '호림동', '호산동'],
        3달성군['가창면', '구지면', '논공읍', '다사읍', '옥포읍', '유가읍', '하빈면', '현풍읍', '화원읍'],
        4동구['각산동', '검사동', '괴전동', '금강동', '내곡동', '내동', '능성동', '대림동', '덕곡동', '도동', '도학동', '동내동', '동호동', '둔산동', '매여동', '미곡동', '미대동', '방촌동', '백안동', '봉무동', '부동', '불로동', '사복동', '상매동', '서호동', '송정동', '숙천동', '신기동', '신무동', '신서동', '신암동', '신용동', '신천동', '신평동', '용계동', '용수동', '율암동', '율하동', '입석동', '중대동', '지묘동', '지저동', '진인동', '평광동', '효목동'],
        5북구['검단동', '고성동1가', '고성동2가', '고성동3가', '관음동', '구암동', '국우동', '금호동', '노곡동', '노원동1가', '노원동2가', '노원동3가', '대현동', '도남동', '동변동', '동천동', '동호동', '매천동', '복현동', '사수동', '산격동', '서변동', '연경동', '읍내동', '조야동', '칠성동1가', '칠성동2가', '침산동', '태전동', '팔달동', '학정동'],
        6서구['내당동', '비산동', '상리동', '원대동1가', '원대동2가', '원대동3가', '이현동', '중리동', '평리동'],
        7수성구['가천동', '고모동', '노변동', '대흥동', '두산동', '만촌동', '매호동', '범물동', '범어동', '사월동', '삼덕동', '상동', '성동', '수성동1가', '수성동2가', '수성동3가', '수성동4가', '시지동', '신매동', '연호동', '욱수동', '이천동', '중동', '지산동', '파동', '황금동'],
        8중구['계산동1가', '계산동2가', '공평동', '교동', '남산동', '남성로', '남일동', '달성동', '대봉동', '대신동', '대안동', '덕산동', '도원동', '동문동', '동산동', '동성로1가', '동성로2가', '동성로3가', '동인동1가', '동인동2가', '동인동3가', '동인동4가', '동일동', '문화동', '봉산동', '북내동', '북성로1가', '북성로2가', '사일동', '삼덕동1가', '삼덕동2가', '삼덕동3가', '상덕동', '상서동', '서내동', '서문로1가', '서문로2가', '서성로1가', '서성로2가', '서야동', '수동', '수창동', '시장북로', '완전동', '용덕동', '인교동', '장관동', '전동', '종로1가', '종로2가', '태평로1가', '태평로2가', '태평로3가', '포정동', '하서동', '향촌동', '화전동']]
'''
#버튼1남구
# 버튼 생성
#run_button = tk.Button(root, text=u"남구", command=run_program, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button = tk.Button(root, text="namgu남구", command=run_program, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)#버튼위치
#버튼1-1의 숨겨진 버튼(새로추가한 부분)
hidden_button = tk.Button(root, text="1대명동", command=hidden_button_click, font=tk_font, bg=button_color,fg="white", activebackground=macbook_color, activeforeground="white")
#hidden_button.place(relx=0.8, rely=0.2, anchor=tk.CENTER)
#hidden_button.place_forget()
#버튼1-2의 숨겨진 버튼(새로추가한 부분)
hidden_button2 = tk.Button(root, text="2봉덕동", command=hidden_button_click2, font=tk_font, bg=button_color,fg="white", activebackground=macbook_color, activeforeground="white")
#hidden_button2.place(relx=0.8, rely=0.4, anchor=tk.CENTER)
#hidden_button2.place_forget()
#버튼1-3의 숨겨진 버튼(새로추가한 부분)
hidden_button3 = tk.Button(root, text="3이천동", command=hidden_button_click2, font=tk_font, bg=button_color,fg="white", activebackground=macbook_color, activeforeground="white")
#hidden_button3.place_forget()
#################################################################################################################3
#버튼2달서구
run_button2 = tk.Button(root, text="Dalseo달서구", command=run_program2, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button2.place(relx=0.1, rely=0.2, anchor=tk.CENTER)#버튼위치
#################################################################################################################3
#버튼3달성군
run_button3 = tk.Button(root, text="Dalseong달성군", command=run_program3, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button3.place(relx=0.1, rely=0.3, anchor=tk.CENTER)#버튼위치
#################################################################################################################3
#버튼4동구
run_button4 = tk.Button(root, text="Donggu동구", command=run_program4, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button4.place(relx=0.1, rely=0.4, anchor=tk.CENTER)#버튼위치
#################################################################################################################3
#버튼5북구
run_button5 = tk.Button(root, text="Bukgu북구", command=run_program5, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button5.place(relx=0.1, rely=0.5, anchor=tk.CENTER)#버튼위치
#################################################################################################################3
#버튼6서구
run_button6 = tk.Button(root, text="Seogu서구", command=run_program6, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button6.place(relx=0.1, rely=0.6, anchor=tk.CENTER)#버튼위치
#################################################################################################################3
#버튼7수성구
run_button7 = tk.Button(root, text="Suseong수성구", command=run_program7, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button7.place(relx=0.1, rely=0.7, anchor=tk.CENTER)#버튼위치
#################################################################################################################3
#버튼8중구
run_button8 = tk.Button(root, text="Jung-gu중구", command=run_program8, font=tk_font, bg=button_color, fg="white", activebackground=macbook_color, activeforeground="white")
run_button8.place(relx=0.1, rely=0.8, anchor=tk.CENTER)#버튼위치
# 버튼 스타일 지정
style.configure("Macbook.TButton", font=tk_font, background=macbook_color, foreground="white", borderwidth=0, highlightthickness=0)


def button_pressed(event):
    run_button.configure(background="#BEBEBE", foreground="white")
    run_button.configure(font="Helvetica 16", relief="sunken")

def button_released(event):
    run_button.configure(background="SystemButtonFace", foreground="black")
    run_button.configure(font="Helvetica 16", relief="raised")




root.mainloop()
