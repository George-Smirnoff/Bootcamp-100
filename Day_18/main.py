import colorgram as cg

def getColor(imagePath):
    color_list = cg.extract(imagePath, 2 ** 32)
    color_palette = []

    for count in range(len(color_list)):
        rgb = color_list[count]
        color = rgb.rgb
        color_palette.append(color)
    return color_palette

def main():
    print(getColor("hirst.png")[12].r)

if __name__ == '__main__':
    main()