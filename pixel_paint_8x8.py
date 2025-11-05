from colorama import Back

# если добавлять новые функции по типу "fill" и они состоят из 2-х слов то надо проверять оба слова как слитное одно
# типа "fill square" -> "fillsquare", т.к. удаление на пробелов

line = [f'{Back.BLUE}  ', 
        f'{Back.GREEN}  ', 
        f'{Back.LIGHTBLUE_EX}  ', 
        f'{Back.LIGHTGREEN_EX}  ', 
        f'{Back.WHITE}  ',
        f'{Back.WHITE}  ',
        f'{Back.LIGHTGREEN_EX}  ', 
        f'{Back.LIGHTGREEN_EX}   {Back.RESET}']


yellow = 'yellow'

# print(yellow)

def paint(color):
    if int(pixel_list[0]) == len(line):
        img[int(pixel_list[1])-1][int(pixel_list[0])-1] = f'{Back.__getattribute__(color.upper())}   ' + f'{Back.RESET}'
    else:
        img[int(pixel_list[1])-1][int(pixel_list[0])-1] = f'{Back.__getattribute__(color.upper())}  '

def fill(color, img):
    for i in range(1, len(line)+1):
        if i == len(line):
            line[i-1] = f'{Back.__getattribute__(color.upper())}   ' + f'{Back.RESET}'
        else:
            line[i-1] = f'{Back.__getattribute__(color.upper())}  '
    img = [line[:], line[:], line[:], line[:], line[:], line[:], line[:], line[:]]
    return img



img = [line[:],
       line[:],
       line[:],
       line[:],
       line[:],
       line[:],
       line[:],
       line[:]]


while True:
    for line in img:
        print(*line, end='\n')

    changed_pixel = input("Запишите пиксель(x y color): ")
    if changed_pixel == "exit":
        break

    try:
        color = changed_pixel[changed_pixel.rindex(" ")+1:]
    except ValueError:
        continue

    xy_pixel = changed_pixel[:changed_pixel.rindex(" ")]

    if xy_pixel == "fill":
        match color:
            case "red":
                img = fill(color,img)
            case "yellow":
                img = fill(color,img)
            case "black":
                img = fill(color,img)
            case "blue":
                img = fill(color,img)
            case "green":
                img = fill(color,img)
            case "magenta":
                img = fill(color,img)
            case "cyan":
                img = fill(color,img)
            case "white":
                img = fill(color,img)
    
    else:
        pixel_list = list(xy_pixel) # убирает все лишнии пробелы в любой строке
        for i in pixel_list:
            if i == " ":
                pixel_list.remove(i)

        pixel_str = ""

        for i in pixel_list:
            pixel_str += i

        xy_pixel = pixel_str

        try:
            int(xy_pixel)
        except ValueError:
            continue
        else:
            match color:
                case "yellow":
                    fill(color)
                case "white":
                    fill(color)
                case "black":
                    fill(color)
                case "blue":
                    fill(color)
                case "red":
                    fill(color)
                case "green":
                   fill(color)
                case "magenta":
                    fill(color)
                case "cyan":
                   fill(color)