from PIL import Image

# use pillow for image processing instead of opencv, just because it saves memory...
im = Image.open('test.jpg')
print(im.format,im.size,im.mode)
# im.show()
output = im.resize((64,64))
# output.show()
output.save('result.jpg')
