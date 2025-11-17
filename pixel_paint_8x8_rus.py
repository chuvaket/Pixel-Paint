from colorama import Back
import os 

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



def paint(color, image):
    painted_pixel = f'{Back.__getattribute__(color.upper())}  '

    image[int(xy_pixel[1])-1][int(xy_pixel[0])-1] = painted_pixel + f' {Back.RESET}' if int(xy_pixel[0]) == len(line) else painted_pixel

def fill(color, image):
    painted_pixel = f'{Back.__getattribute__(color.upper())}  '
    area = input("Укажите границы заливки(x x y y) (нажмите Enter - закрасить все): ").split() # если нажать enter --> []

    if area == []:
        area = ""

    area_pos_x = area[:2]
    area_pos_y = area[2:]

    if area == "":
        for i in range(1, len(line)+1):
            line[i-1] = painted_pixel + f' {Back.RESET}' if i == len(line) else painted_pixel
        image = [line[:], line[:], line[:], line[:], line[:], line[:], line[:], line[:]]
    else:
        try:
            area_pos_x[0]
            area_pos_x[1]
            area_pos_y[0]
            area_pos_y[1]
        except IndexError:
            return image
        else:
            if ((1 <= int(area_pos_x[0]) <= len(line)) & (1 <= int(area_pos_x[1]) <= len(line))) & ((1 <= int(area_pos_y[0]) <= len(line)) & (1 <= int(area_pos_y[1]) <= len(line))):
                for  i in range(int(area_pos_y[0]), int(area_pos_y[1])+1):
                    if int(area_pos_x[1]) == len(line):
                        image[i-1][int(area_pos_x[0])-1:int(area_pos_x[1])] = [painted_pixel] * (int(area_pos_x[1]) - int(area_pos_x[0]))
                        image[i-1][int(area_pos_x[1]):] = [painted_pixel + f' {Back.RESET}']
                    else:
                        image[i-1][int(area_pos_x[0])-1:int(area_pos_x[1])] = [painted_pixel] * (int(area_pos_x[1]) + 1 - int(area_pos_x[0]))
            else: 
                return image
    return image


img = [line[:],
       line[:],
       line[:],
       line[:],
       line[:],
       line[:],
       line[:],
       line[:]]


while True:
    os.system('cls')
    for line in img:
        print(*line, end='\n')

    changed_pixel = input("Запишите пиксель(x y color): ").split()
    if changed_pixel == "exit":
        break

    color = changed_pixel[-1]

    xy_pixel = changed_pixel[:changed_pixel.index(color)]

    pixel_str = ""
    for i in xy_pixel:
        pixel_str += i

    xy_pixel = pixel_str

    if xy_pixel == "fill":
        match color:
            case "red":
                img = fill(color, img)
            case "yellow":
                img = fill(color, img)
            case "black":
                img = fill(color, img)
            case "blue":
                img = fill(color, img)
            case "green":
                img = fill(color, img)
            case "magenta":
                img = fill(color, img)
            case "cyan":
                img = fill(color, img)
            case "white":
                img = fill(color, img)
    
    else:
        if (1 <= int(xy_pixel[0]) <= len(line)) & (1 <= int(xy_pixel[1]) <= len(line)):

            pixel_str = ""

            for i in xy_pixel:
                pixel_str += i

            xy_pixel = pixel_str

            try:
                int(xy_pixel)
            except ValueError:
                continue
            else:
                match color:
                    case "yellow":
                        paint(color, img)
                    case "white":
                        paint(color, img)
                    case "black":
                        paint(color, img)
                    case "blue":
                        paint(color, img)
                    case "red":
                        paint(color, img)
                    case "green":
                        paint(color, img)
                    case "magenta":
                        paint(color, img)
                    case "cyan":
                        paint(color, img)
        else: 
            continue

