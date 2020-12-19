
from PIL import Image
from resizeimage import resizeimage


fd_img = open('image/khunglong.jpg', 'r', encoding="utf8")
print(fd_img)
img = Image.open(fd_img)
print(img)
# img = resizeimage.resize_width(img, 200)
# img.save('test-image-width.jpg', img.format)
# fd_img.close()