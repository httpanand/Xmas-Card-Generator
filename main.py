from PIL import Image, ImageDraw, ImageFont , ImageOps , ImageColor

__author__ = 'Http Anand'
__contributer___ = 'K A R T H I K'

text_color = input('Enter text color : ')
bord_color = input('Enter border color : ')
canva_color = input('Enter canvas color: ')
to =  input('Enter name of the receiver : ')
to_msg = (f'Dear {to}')

image = Image.new('RGB', (250,400), canva_color)
image = ImageOps.expand(image,border=2,fill= bord_color)

draw = ImageDraw.Draw(image)
icons = '''
	1) Santa Hat 
	2) Xmas Tree 
	3) Xmas Bell
	4) Xmas Boy
	5) Xmas Girl
	6) Xmas Gift
    7) Santa with Deer
    8) Decorate with Family
    9) Tree with Couples
    
'''
ic = input(f'Enter ICON for header\nAvailable Icons\n {icons} Enter option : ')

if(ic == '1'):
	icon = Image.open('assets/hat.png')
	icon = icon.resize((60, 60))
	image.paste(icon ,(102,20), icon)
elif(ic == '2'):
	icon = Image.open('assets/tree.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
elif(ic == '3'):
	icon = Image.open('assets/bell.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
elif(ic == '4'):
	icon = Image.open('assets/boy.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
elif(ic == '5'):
	icon = Image.open('assets/girl.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
elif(ic == '6'):
	icon = Image.open('assets/gift.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
elif(ic == '7'):
	icon = Image.open('assets/santa-deer.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
elif(ic == '8'):
	icon = Image.open('assets/decorate-family.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
elif(ic == '9'):
	icon = Image.open('assets/tree-couple.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,20), icon)
else:
	print('No valid option found')

ficons = f'''
	1) Xmas Train
	2) Xmas Sledge
    3) Santa on Chair
    4) Merry Christmas Logo
    
'''

fic = input(f'Enter ICON for footer\nAvailable Icons\n {ficons} Enter option : ')
if(fic == '1'):
	icon = Image.open('assets/train.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,300), icon)
elif(fic == '2'):
	icon = Image.open('assets/sledge.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,300), icon)
elif(fic == '3'):
	icon = Image.open('assets/santa-chair.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,300), icon)
elif(fic == '4'):
	icon = Image.open('assets/merry-christmas.png')
	icon = icon.resize((70, 70))
	image.paste(icon ,(98,300), icon)
else:
	print('No valid option found')

wish = '''\n
May the true 
spirit of Christmas
shine in your
heart and light
your path. Merry
Christmas and a 
Happy New Year !
'''

#font = ImageFont.truetype(r'font\monalisa.ttf', 13)
#draw.text((25,120),to_msg,text_color,font=font)
#draw.text((60,120),wish,text_color,font=font)

font = ImageFont.truetype(r'font\nexa_bold.otf', 13)
draw.text((25,120),to_msg,text_color,font=font)
draw.text((60,120),wish,text_color,font=font)

frm = input("Enter author name : ")
frm_msg = (f'From {frm :}')
draw.text((25,280),frm_msg,text_color,font=font)

file = input("enter file name : ")
image.save(f'{file}.png')
