from PIL import Image


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):  # 将256灰度映射到70个字符上,rgb值转函数
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


im = Image.open('放入图片路径')
w, h = im.size

txt = ""

for i in range(h):
    for j in range(w):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'

print(txt)
