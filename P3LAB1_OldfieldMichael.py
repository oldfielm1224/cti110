red = int(input())
green = int(input())
blue = int(input())
smallestnumber = 0

if (red < green) and (red < blue):
    smallestnumber = red

elif (green < red) and (green < blue):
    smallestnumber = green

else:
    smallestnumber = blue

nograyred = red - smallestnumber
nograygreen = green - smallestnumber
nograyblue = blue - smallestnumber

print(f'{nograyred} {nograygreen} {nograyblue}')
