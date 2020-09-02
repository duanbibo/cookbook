import qrcode    #生成二维码  qrcode :二维码
import  barcode  #生成条形码  barcode :条形码



# img=qrcode.make("some date here")
# img.save("Some.png")
# img.show()
'''
设置生成二维码的参数，
   version：尺寸 
   err_correction :控制生成二维码的误差，LMQH 从低到高，低时误差率低
   box_size: 控制二维码中每个单元格有多少像素
   border: 控制每条边有多少个单元格，默认是4，这是最小值
   二维码知识：二维码的数据主要保存在图片的四个角上，所以在二维码中间放一个小图标对二维码
   的识别是不会产生多大的影响的。图标大小不超过二维码长和宽的1/4
'''
qr=qrcode.QRCode(
      version=2,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=1
)
qr.add_data("hello word")
qr.make(fit=True)
img=qr.make_image()
img.save("helloword.png")


'''
生成条形码：
    条形码知识：条形码的标准有多重，pybarcode9种
    执行后会生成SVG格式的条形码文件 ，SVG格式的文件，其实类似XML，W3C规定的，每个条形间隔都是一个节点。
'''
#设置条形码标准，第一个参数是条形码的类型 ，第二个参数是条形码的数据
ean=barcode.get('ean13','6959641900334')
print(ean.get_fullcode())           #打印生成的条形码的参数数据
filename=ean.save('ean13')           #把生成的条形码保存在当前文件中
print(filename)

from barcode.writer import ImageWriter
eanpng=barcode.get('ean13','6959641900334',writer=ImageWriter())
filename2=eanpng.save('en13png')
print(filename2)
