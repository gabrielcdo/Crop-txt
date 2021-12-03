import cv2
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', dest='img_type', help="tipo imagem", default="png")
parser.add_argument('-p', '--path', dest='img_path', help="path das imagens", default="")
parser.add_argument('-d', '--dest', dest='dest_path', help="path destino imagens cropadas", default="")
args = parser.parse_args()

img_path  = args.img_path
img_type= args.img_type 
dest_path = args.dest_path

print(img_path+'/*.'+img_type)
files = glob.glob(img_path+'/*.'+img_type)
conterro=0
print("total imgs = ",len(files))
total_imgs=0
conterro=0

for file in files:
    img = cv2.imread(file)
    if( img is None):
        continue
    img_height , img_width , dims = img.shape 
    c = []
    path , rest = file.split('.')
    with open(path+".txt", "r") as f:
        itens = [plate for plate in f.readlines()]
    for item in itens:
        class_name , x , y , w , h = map(float,item.split(' '))
        w = w*img_width
        h = h*img_height
        x = x*img_width
        y = y*img_height
        class_name=int(class_name)
        x = int(x)
        y = int(y)
        w = int(w/2)
        h = int(h/2)
        y0 = y-h
        yf = y+h
        x0 = x-w
        xf = x+w
        if(y0<0):
            y0=0
        if(yf>img_height):
            yf=img_height
        if(x0<0):
            x0 = 0
        if(xf>img_width):
            xf=img_width
        img2 = img[y0:yf,x0:xf]
        try:
            cv2.imwrite(dest_path+'/img'+str(total_imgs)+'.'+img_type,img2)
            total_imgs = total_imgs+1
        except Exception as e:
            conterro=conterro+1
            print("Erros: ",conterro)



