# Xây dựng chương trình mã hoá và giải mã Elgamal
# Chú ý tìm nghịch đảo phải theo ơ clit mở rộng
# Ma trận bản mã = Ma trận Bản rõ * Ma trận khoá
# Ma trận bản rõ = Ma trận Bản mã * Ma trận nghịch đảo

import numpy as np


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
def encrypt(plain_text, public_key):
    p, g, y = public_key
    k = np.random.randint(1, p - 1)  # Chọn số ngẫu nhiên k
    cipher = []
    for i in range(len(plain_text)):
        r = pow(g, k, p)
        s = (plain_text[i] * pow(y, k, p)) % p
        cipher.append((r, s))
    return cipher

# Hàm giải mã Elgamal
def decrypt(cipher, private_key):
    p, x = private_key
    plain_text = []
    for c in cipher:
        r, s = c
        r_inv = mod_inverse(pow(r, x, p), p)  # Tính nghịch đảo của r^x (mod p)
        plain_text.append((s * r_inv) % p)
    return plain_text

# Khởi tạo khóa công khai và khóa bí mật
p = 9973  # Số nguyên tố lớn
g = 2   # Số nguyên tố nguyên thủy
x = 345  # Khóa bí mật
y = pow(g, x, p)  # Khóa công khai

public_key = (p, g, y)
private_key = (p, x)

# Mã hoá và giải mã
data_input = input('Hãy nhập văn bản bạn muốn mã hoá: ')
plain_text = text_to_numbers(data_input)  # Bản rõ
cipher_text = encrypt(plain_text, public_key)
decrypted_text = decrypt(cipher_text, private_key)
data_output = numbers_to_text(decrypted_text)

print("Bản rõ:", plain_text)
print("Bản mã:", cipher_text)
print("Giải mã:", decrypted_text)
print("Văn bản giải mã:", data_output)