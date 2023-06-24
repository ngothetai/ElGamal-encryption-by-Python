from tkinter import *
import numpy as np
import re


# Hàm chuyển đổi ký tự sang số
def text_to_numbers(text):
    numbers = []
    for char in text:
        number = ord(char)  # Chuyển đổi ký tự thành mã ASCII
        numbers.append(number)
    return numbers


# Hàm chuyển đổi số sang ký tự
def numbers_to_text(numbers):
    text = ""
    for number in numbers:
        char = chr(number)  # Chuyển đổi mã ASCII thành ký tự
        text += char
    return text


# Hàm tính nghịch đảo modulo
def mod_inverse(a, m):
    if m == 1:
        return 0
    m0 = m
    x0, x1 = 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


            
# Hàm mã hoá Elgamal
def encrypt():
    try:
        public_key = text_public_key.get()[1:-1].split(',')
        p, alpha, beta = int(public_key[0].strip()), int(public_key[1].strip()), int(public_key[2].strip())
        cipher = []
        
        k = np.random.randint(1, p - 1)  # Chọn số ngẫu nhiên k
        
        text = text_to_numbers(text_ban_ro.get()) # lấy văn bản rõ từ file
                
        for i in range(len(text)):
            y1 = pow(alpha, k, p)
            y2 = (text[i] * pow(beta, k, p)) % p
            cipher.append((y1, y2))
        text_code_text_encrypt.delete(0, END)
        text_code_text_encrypt.insert(END, str(cipher)[1:-1])
    except IOError:
        print('Không thể mã hoá!')


def convert_string_to_tuple_list(string):
    # Tìm tất cả các chuỗi bên trong dấu ngoặc đơn và lưu vào danh sách
    tuple_strings = re.findall(r'\((.*?)\)', string)

    # Chuyển đổi các chuỗi thành tuple và lưu vào danh sách kết quả
    result = []
    for tuple_str in tuple_strings:
        values = tuple(map(int, tuple_str.split(',')))
        result.append(values)

    return result


# Hàm giải mã Elgamal
def decrypt():
    private_key = text_private_key.get()[1:-1].split(',')
    p, a = int(private_key[0].strip()), int(private_key[1].strip())
    plain_text = []
    
    data = '[' +text_code_text_decrypt.get() + ']' # Lấy đoạn mã đã bị mã hoá
    cipher = convert_string_to_tuple_list(data)
    
    try:
        for c in cipher:
            y1, y2 = c
            r_inv = mod_inverse(pow(y1, a, p), p)  # Tính nghịch đảo của r^x (mod p)
            plain_text.append((y2 * r_inv) % p)
        text_giai_ma.delete(0, END)
        text_giai_ma.insert(END, numbers_to_text(plain_text))
    except IOError:
        print('Không thể giải mãi!')
    

def read_text_file(file_path=None):
    file_path = str(text_path_1.get())
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_ban_ro.delete(0, END)
            text_ban_ro.insert(END, text)
    except IOError:
        print("Không thể đọc file.")


def create_key():
    # Lấy dữ liệu tham số từ người dùng nhập
    p = int(text_P.get())
    Alpha = int(text_Alpha.get())
    a = int(text_a.get())
    
    # Tính Beta
    beta = pow(Alpha, a, p)
    
    # Tạo khoá
    private_key = (p, a)
    public_key = (p, Alpha, beta)
    
    # Chèn kết quả khoá vào ô
    text_private_key.delete(0, END)    
    text_private_key.insert(END, str(private_key))
    text_public_key.delete(0, END)
    text_public_key.insert(END, str(public_key))
    print('Đã tạo khoá thành công!')
    

def delete_key():
    text_private_key.delete(0, END)
    text_public_key.delete(0, END)
    print('Đã xoá tất cả các khoá riêng tư và công khai!')


def push_code():
    text_code_text_decrypt.delete(0, END)
    text_code_text_decrypt.insert(END, text_code_text_encrypt.get())


def save_encrypt_file():
    encrypt = text_code_text_encrypt.get()
    try:
        with open('encrypt.txt', 'w') as file:
            file.write(encrypt)
        print("Ghi file thành công.")
    except IOError:
        print("Không thể ghi file.")


def read_encrypt_file():
    try:
        with open('encrypt.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            text_.delete(0, END)
            text_ban_ro.insert(END, text)
    except IOError:
        print("Không thể đọc file.")


# Thiết kế giao diện
root= Tk()
root.title('Graphical Use Interface')
root.geometry('1200x500')

 
canvas = Canvas(root, width=1200, height=500)
canvas.pack()

# vẽ đường thẳng dọc màu đỏ
canvas.create_line(320, 0, 320, 500, fill="black")


# vẽ đường thẳng dọc màu đỏ
canvas.create_line(760, 0, 760, 500, fill="black")


# Tạo khoá
title = Label(root, text= 'Tạo khoá', font=('Arial Black',14))
title.place(x= 50 , y = 60 )

label_P = Label(root, text = '     P:    ', font= ('Arial', 10),bg="#DDDDDD")
label_P.place(x= 50 , y = 150)
text_P = Entry(root)
text_P.place(x= 110 , y= 150)

label_Alpha = Label(root, text= " Alpha: ",font= ('Arial', 10 ), bg="#DDDDDD")
label_Alpha.place(x= 50, y=180)
text_Alpha = Entry(root)
text_Alpha.place(x= 110 , y= 180)

label_a= Label(root,text= "     a:    ", font= ("Arial", 10),bg="#DDDDDD")
label_a.place(x=50,y=210)
text_a= Entry(root)
text_a.place(x= 110 , y= 210)

label_private_key = Label(root, text = 'Private key:', font= ('Arial', 8),bg="#DDDDDD")
label_private_key.place(x= 50 , y = 300)
text_private_key= Entry(root)
text_private_key.place(x= 110 , y= 300)

label_public_key= Label(root, text= "Public key:",font= ('Arial', 8), bg="#DDDDDD")
label_public_key.place(x= 50, y=330)
text_public_key= Entry(root)
text_public_key.place(x= 110 , y= 330)

but_Create_key = Button(root, text = 'Tạo khoá',bg='Cyan',width = '10', command=create_key)
but_Create_key.place(x= 130, y=360)
but_Delete_key = Button(root, text = 'Xoá khoá',bg='Cyan',width = '10', command=delete_key)
but_Delete_key.place(x= 130, y=390)


# Mã hoá
label_Encrypt = Label(root,text = 'Mã hoá', font=('Arial Black',14))
label_Encrypt.place(x=350,y=60)

label_ban_ro = Label(root,text= 'Đường dẫn')
label_ban_ro.place(x= 350,y=100)
text_path_1 = Entry(root)
text_path_1.place(x= 420 , y= 100, width=220, height=20)

but_File_text = Button(root, text = 'Tệp văn bản',bg='Cyan',width = '10', command=read_text_file)
but_File_text.place(x= 650,y=100)

label_ban_ro = Label(root,text= 'Văn bản')
label_ban_ro.place(x= 350,y=170)

text_ban_ro = Entry(root)
text_ban_ro.place(x= 420 , y= 150, width=220, height=100)

but_Encrypt = Button(root, text = 'Mã hoá',bg='Cyan',width = '10', command=encrypt)
but_Encrypt.place(x= 470,y=280)

label_code_text_encrypt = Label(root,text= 'Codetext')
label_code_text_encrypt.place(x= 350, y= 330)
text_code_text_encrypt = Entry(root)
text_code_text_encrypt.place(x= 420 , y= 360, width=220, height=100)

but_push = Button(root, text= 'Chuyển', bg = 'Cyan', width = '10', command=push_code)
but_push.place(x= 650 , y = 360 )

but_store_encrypt = Button(root, text= 'Lưu', bg = 'Cyan', width = '10', command=save_encrypt_file)
but_store_encrypt.place(x= 650 , y = 390 )


# Giải mã
label_Decrypt = Label(root, text ='Giải mã',font=('Arial Black',14))
label_Decrypt.place(x= 770,y=60)


label_giai_ma = Label(root,text= 'Văn bản')
label_giai_ma.place(x= 770,y=170)

text_giai_ma= Entry(root)
text_giai_ma.place(x= 840 , y= 150, width=220, height=100)

label_code_text_decrypt = Label(root,text= 'Codetext')
label_code_text_decrypt.place(x= 770, y= 330)

text_code_text_decrypt = Entry(root)
text_code_text_decrypt.place(x= 840 , y= 360, width=220, height=100)

label_store_decrypt = Button(root,text = 'Lưu', bg = "Cyan", width = '10', height = '2')
label_store_decrypt.place(x= 1070, y = 360)



root.mainloop()