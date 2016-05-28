import os
import pytesseract
try:
	import Image
except ImportError:
	from PIL import Image


def load():
	dirname = os.listdir('/Users/stephane.sol/Documents/GitHub/sol-data-science/frenchocr/Input/')

	for file in dirname:
		file_path = os.path.abspath(file)
		return file_path


def resize_image():
	size_300 = (300, 300)
	for file in os.listdir('.'):
		i = image.open(file)
		fn, fext = os.path.slitext(file)
		i.thumbnail(size_300)
		i.save('300/{}_300.png'.format(fn, fext))


def parse():
	with open('/Users/stephane.sol/Documents/GitHub/sol-data-science/frenchocr/out.txt', 'r') as content_file:
		content = content_file.read()
		parse_new_line = content.split("\n\n")
	print(parse_new_line)


def crop_image(file):
	for f in [f for f in os.listdir(file) if not f.startswith('.')]:
		i = Image.open(f)
		left = 0
		top = 100
		right = 3100
		bottom = 2000
		crop_i = i.crop((left, top, right, bottom))

		fn, fext = os.path.splitext(f)
		crop_i.save(os.path.join(file, '{}_crop.png'.format(fn, fext)))

def rotate_image(file,degree):
	for f in [f for f in os.listdir(file) if not f.startswith('.')]:
		i = Image.open(f)
		rotate_i = i.rotate(degree)

		fn, fext = os.path.splitext(f)
		rotate_i.save(os.path.join(file,'{}{}'.format(fn, fext)))


def ocr(file):
	os.chdir(file)
	for f in [f for f in os.listdir(file) if not f.startswith('.')]:
		input = os.path.join(path,f)
		fn, fext = os.path.splitext(f)
		output = fn
		cmd = 'tesseract -l eng+fra {} {}'.format(input, output)
		os.system(cmd)