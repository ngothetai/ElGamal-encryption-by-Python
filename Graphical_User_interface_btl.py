from tkinter import *
import numpy as np
import re
import random


Duong_dan_ban_ro = 'C:\\Users\\theta\\OneDrive\\Desktop\\ban_ro.txt'
Duong_dan_ban_ma = 'C:\\Users\\theta\\OneDrive\\Desktop\\ban_ma.txt'



def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_random_prime(start, end):
    while True:
        number = random.randint(start, end)
        if is_prime(number):
            return number



# Hàm chuyển đổi ký tự sang số
def text_to_numbers(text):
    numbers = []
    for char in text:
        number = ord(char)  # Chuyển đổi ký tự thành mã UTF-8
        numbers.append(number)
    return numbers


# Hàm chuyển đổi số sang ký tự
def numbers_to_text(numbers):
    text = ""
    for number in numbers:
        char = chr(number)  # Chuyển đổi mã UTF-8 thành ký tự
        text += char
    return text

# Hàm modulo luỹ thừa
def pow_modulo(base, exponent, modulo):
    result = 1
    base %= modulo

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulo
        exponent //= 2
        base = (base * base) % modulo

    return result


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
        
        text = text_to_numbers(text_encrypt_ban_ro.get()) # lấy văn bản rõ từ file
                
        for i in range(len(text)):
            y1 = pow_modulo(alpha, k, p)
            y2 = (text[i] * pow_modulo(beta, k, p)) % p
            cipher.append((y1, y2))
        text_encrypt_ban_ma.delete(0, END)
        text_encrypt_ban_ma.insert(END, str(cipher)[1:-1])
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
    
    data = '[' +text_decrypt_ban_ma.get() + ']' # Lấy đoạn mã đã bị mã hoá
    cipher = convert_string_to_tuple_list(data)
    
    try:
        for c in cipher:
            y1, y2 = c
            r_inv = mod_inverse(pow_modulo(y1, a, p), p)  # Tính nghịch đảo của r^x (mod p)
            plain_text.append((y2 * r_inv) % p)
        text_decrypt_ban_ro.delete(0, END)
        text_decrypt_ban_ro.insert(END, numbers_to_text(plain_text))
    except IOError:
        print('Không thể giải mãi!')


def random_key():
    p = generate_random_prime(9000, 900000)
    Alpha = generate_random_prime(2, 200)
    a = generate_random_prime(200, 8999)
    text_P.delete(0, END)
    text_P.insert(END, str(p))
    text_Alpha.delete(0, END)
    text_Alpha.insert(END, str(Alpha))
    text_a.delete(0, END)
    text_a.insert(END, str(a))
    
    # Lấy dữ liệu tham số từ người dùng nhập
    p = int(text_P.get())
    Alpha = int(text_Alpha.get())
    a = int(text_a.get())
    
    # Tính Beta
    beta = pow_modulo(Alpha, a, p)
    
    # Tạo khoá
    private_key = (p, a)
    public_key = (p, Alpha, beta)
    
    # Chèn kết quả khoá vào ô
    text_private_key.delete(0, END)    
    text_private_key.insert(END, str(private_key))
    text_public_key.delete(0, END)
    text_public_key.insert(END, str(public_key))
    print('Đã tạo khoá thành công!')

def create_key():
    if have_random_key:
        p = generate_random_prime(9000, 900000)
        Alpha = generate_random_prime(2, 200)
        a = generate_random_prime(200, 8999)
        text_P.delete(0, END)
        text_P.insert(END, str(p))
        text_Alpha.delete(0, END)
        text_Alpha.insert(END, str(Alpha))
        text_a.delete(0, END)
        text_a.insert(END, str(a))
    
    # Lấy dữ liệu tham số từ người dùng nhập
    p = int(text_P.get())
    Alpha = int(text_Alpha.get())
    a = int(text_a.get())
    
    # Tính Beta
    beta = pow_modulo(Alpha, a, p)
    
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
    text_decrypt_ban_ma.delete(0, END)
    text_decrypt_ban_ma.insert(END, text_encrypt_ban_ma.get())
    
    
def read_text_file_encrypt(file_path=None):
    file_path = str(text_path_encrypt_ban_ro.get())
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = ''.join(file.read())
            text_encrypt_ban_ro.delete(0, END)
            text_encrypt_ban_ro.insert(0, text)
            print(text_encrypt_ban_ro.get())
    except IOError:
        print("Không thể đọc file.")


def save_text_file_encrypt():
    encrypt = text_encrypt_ban_ma.get()
    try:
        with open(Duong_dan_ban_ma, 'w') as file:
            file.write(encrypt)
        print("Ghi file thành công.")
    except IOError:
        print("Không thể ghi file.")


def read_text_file_decrypt():
    file_path = str(text_path_decrypt_ban_ma.get())
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_decrypt_ban_ma.delete(0, END)
            text_decrypt_ban_ma.insert(END, text)
    except IOError:
        print("Không thể đọc file.")
        
        
def save_text_file_decrypt():
    encrypt = str(text_decrypt_ban_ro.get())
    try:
        with open(Duong_dan_ban_ro, 'w', encoding='utf-8') as file:
            file.write(encrypt)
        print("Ghi file thành công.")
    except IOError:
        print("Không thể ghi file.")


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
but_Delete_key = Button(root, text = 'Tạo khoá ngẫu nhiên',bg='Cyan',width = '10', command=random_key)
but_Delete_key.place(x= 130, y=430)

# Mã hoá
title_Encrypt = Label(root,text = 'Mã hoá', font=('Arial Black',14))
title_Encrypt.place(x=350,y=60)

label_path_encrypt_ban_ro = Label(root,text= 'Đường dẫn')
label_path_encrypt_ban_ro.place(x= 350,y=100)
text_path_encrypt_ban_ro = Entry(root)
text_path_encrypt_ban_ro.place(x= 420 , y= 100, width=220, height=20)

but_File_text = Button(root, text = 'Tệp văn bản',bg='Cyan',width = '10', command=read_text_file_encrypt)
but_File_text.place(x= 650,y=100)

label_encrypt_ban_ro = Label(root,text= 'Bản rõ')
label_encrypt_ban_ro.place(x= 350,y=170)
text_encrypt_ban_ro = Entry(root)
text_encrypt_ban_ro.place(x= 420 , y= 150, width=220, height=100)

but_Encrypt = Button(root, text = 'Mã hoá',bg='Cyan',width = '10', command=encrypt)
but_Encrypt.place(x= 470,y=280)

label_encrypt_ban_ma = Label(root,text= 'Bản mã')
label_encrypt_ban_ma.place(x= 350, y= 330)
text_encrypt_ban_ma = Entry(root)
text_encrypt_ban_ma.place(x= 420 , y= 360, width=220, height=100)

but_push = Button(root, text= 'Chuyển', bg = 'Cyan', width = '10', command=push_code)
but_push.place(x= 650 , y = 360 )

but_store_encrypt = Button(root, text= 'Lưu', bg = 'Cyan', width = '10', command=save_text_file_encrypt)
but_store_encrypt.place(x= 650 , y = 390 )


# Giải mã
title_Decrypt = Label(root, text ='Giải mã',font=('Arial Black',14))
title_Decrypt.place(x= 770,y=60)

label_path_decrypt_ban_ma = Label(root,text= 'Đường dẫn')
label_path_decrypt_ban_ma.place(x= 770,y=100)
text_path_decrypt_ban_ma = Entry(root)
text_path_decrypt_ban_ma.place(x= 840 , y= 100, width=220, height=20)

but_File_encrypt = Button(root, text = 'Tệp mã hoá',bg='Cyan',width = '10', command=read_text_file_decrypt)
but_File_encrypt.place(x= 1070,y=100)

label_decrypt_ban_ma = Label(root,text= 'Bản mã')
label_decrypt_ban_ma.place(x= 770,y=170)
text_decrypt_ban_ma= Entry(root)
text_decrypt_ban_ma.place(x= 840 , y= 150, width=220, height=100)

but_Decrypt= Button(root, text = 'Giải mã', bg= "Cyan", width= '10 ', command=decrypt)
but_Decrypt.place(x= 890, y = 280)

label_decrypt_ban_ro = Label(root,text= 'Bản rõ')
label_decrypt_ban_ro.place(x= 770, y= 330)
text_decrypt_ban_ro = Entry(root)
text_decrypt_ban_ro.place(x= 840 , y= 360, width=220, height=100)

label_store_decrypt = Button(root,text = 'Lưu', bg = "Cyan", width = '10', height = '2', command=save_text_file_decrypt)
label_store_decrypt.place(x= 1070, y = 360)


root.mainloop()