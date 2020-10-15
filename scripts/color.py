def hex_to_rgb(hex, isRounding = True, digits = 2):
    hex = hex.lstrip('#')
    hlen = len(hex)
    rgb = tuple(int(hex[i:i+hlen//3], 16) / 255 for i in range(0, hlen, hlen//3))

    if (isRounding):
        rgbList = list(rgb)

        for i, e in enumerate(rgbList):
            rgbList[i] = round(e, digits)

        rgb = tuple(rgbList)

    return rgb

hex = "#408080"
rgb = hex_to_rgb(hex)
print(rgb)