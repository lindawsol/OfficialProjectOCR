import os
import pytesseract
try:
	import Image
except ImportError:
	from PIL import Image


def dirToList(directory):
	dirname = os.listdir(directory)
	for file in dirname:
		file_path = os.path.abspath(file)
		return file_path


def resize_image(x, y):
	size = (x, y)
	for file in os.listdir('.'):
		i = image.open(file)
		fn, fext = os.path.slitext(file)
		i.thumbnail(size)
		i.save('{}/{}_{}.{}'.format(x, fn, x, fext))


def parse(file):
	with open(file, 'r') as content_file:
		content = content_file.read()
		'add file name to beginning of list'
		parse_new_line = content.split("\n\n")
		file_with_ext = os.path.basename(file)
		file_name = os.path.splitext(file_with_ext)[0]
		parse_new_line.insert(0,file_name)
	return parse_new_line


def crop_image(file, left, top, right, bottom):
	for f in [f for f in os.listdir(file) if not f.startswith('.')]:
		i = Image.open(f)
		crop_i = i.crop((left, top, right, bottom))
		fn, fext = os.path.splitext(f)
		crop_i.save(os.path.join(file, '{}_crop.png'.format(fn, fext)))


def rotate_image(file,rotate_degree):
	for f in [f for f in os.listdir(file) if not f.startswith('.')]:
		i = Image.open(f)
		rotate_i = i.rotate(rotate_degree)
		fn, fext = os.path.splitext(f)
		rotate_i.save(os.path.join(file, '{}{}'.format(fn, fext)))


def ocr(directory):
	for f in [f for f in os.listdir(directory) if not f.startswith('.')]:
		input = os.path.join(directory, f)
		fn, fext = os.path.splitext(f)
		output = fn
		cmd = 'tesseract -l eng+fra {} {}'.format(input, output)
		os.system(cmd)

def jdefault(o):
    return o.__dict__
