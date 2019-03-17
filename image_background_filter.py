from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("image_noise.jpg") #input image
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('image_clear.jpg') #ouput image