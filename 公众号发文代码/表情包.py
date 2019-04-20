from PIL import Image, ImageDraw, ImageFont

img = Image.open("C:\\Users\\黎涛\\Pictures\\Camera Roll\\]CVJ31WIYVO(_(HS2`I@723.png")
img.resize((500, 500),Image.ANTIALIAS)
jgz = Image.open("C:\\Users\\黎涛\\Pictures\\Camera Roll\\]CVJ31WIYVO(_(HS2`I@723.png")
img.paste(jgz,(105,95))
img.show()

draw = ImageDraw.Draw(img)
print(draw)
ttfront = ImageFont.truetype('simhei.ttf', 24)
draw.text((72, 20),"361装逼卫士",fill=(238,92,13), font=ttfront)
draw.text((40, 220),"让你多一度安全装逼",fill=(0,0,0), font=ttfront)
img.show()
img.save("361装逼卫视表情包.gif")