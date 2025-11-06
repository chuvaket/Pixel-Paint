from colorama import Back

# if you add new functions like "fill" and they consist of two words, you need to check both words as a single word
# like "fill square" -> "fillsquare", because removing spaces

line = [f'{Back.BLUE}  ', 
        f'{Back.GREEN}  ', 
        f'{Back.LIGHTBLUE_EX}  ', 
        f'{Back.LIGHTGREEN_EX}  ', 
        f'{Back.WHITE}  ',
        f'{Back.WHITE}  ',
        f'{Back.LIGHTGREEN_EX}  ', 
        f'{Back.LIGHTGREEN_EX}   {Back.RESET}']



def paint(color):
    painted_pixel = f'{Back.__getattribute__(color.upper())}  '

    if int(pixel_list[0]) == len(line):
        img[int(pixel_list[1])-1][int(pixel_list[0])-1] = painted_pixel + f' {Back.RESET}'
    else:
        img[int(pixel_list[1])-1][int(pixel_list[0])-1] = painted_pixel

def fill(color, image):
    area = input("Specify the fill borders (x x y y) (press Enter to fill all): ")

    area_pos = list(area) # removes all extra spaces in any line
    for i in area_pos:
        if i == " ":
            area_pos.remove(i)

    area_pos_x = area_pos[:2]
    area_pos_y = area_pos[2:]

    if area == "":
        painted_pixel = f'{Back.__getattribute__(color.upper())}  '

        for i in range(1, len(line)+1):
            if i == len(line):
                line[i-1] = painted_pixel + f' {Back.RESET}'
            else:
                line[i-1] = painted_pixel
        image = [line[:], line[:], line[:], line[:], line[:], line[:], line[:], line[:]]
    else:
        if ((1 <= int(area_pos_x[0]) <= len(line)) & (1 <= int(area_pos_x[1]) <= len(line))) & ((1 <= int(area_pos_y[0]) <= len(line)) & (1 <= int(area_pos_y[0]) <= len(line))):
            for  i in range(int(area_pos_y[0]), int(area_pos_y[1])+1):
                if int(area_pos_x[1]) == len(line):
                    image[i-1][int(area_pos_x[0])-1:int(area_pos_x[1])] = [f'{Back.__getattribute__(color.upper())}  '] * (int(area_pos_x[1]) - int(area_pos_x[0]))
                    image[i-1][int(area_pos_x[1]):] = [f'{Back.__getattribute__(color.upper())}  ' + f' {Back.RESET}']
                else:
                    image[i-1][int(area_pos_x[0])-1:int(area_pos_x[1])] = [f'{Back.__getattribute__(color.upper())}  '] * (int(area_pos_x[1]) + 1 - int(area_pos_x[0]))
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
    for line in img:
        print(*line, end='\n')

    changed_pixel = input("Enter the pixel(x y color):")
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
        pixel_list = list(xy_pixel) # removes all extra spaces in any line
        for i in pixel_list:
            if i == " ":
                pixel_list.remove(i)

        if (1 <= int(pixel_list[0]) <= len(line)) & (1 <= int(pixel_list[1]) <= len(line)):

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
                        paint(color)
                    case "white":
                        paint(color)
                    case "black":
                        paint(color)
                    case "blue":
                        paint(color)
                    case "red":
                        paint(color)
                    case "green":
                        paint(color)
                    case "magenta":
                        paint(color)
                    case "cyan":
                        paint(color)
        else: 
            continue
