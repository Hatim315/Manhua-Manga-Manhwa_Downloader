from PIL import Image
import os
def PdfMaker(Imagepath,PdfPath,Name):
    """This function will make Pdf's of images"""
    print(f"Creating Pdf of {Name} ...")
    images=[Image.open(Imagepath+'/'+f) for f in sorted(os.listdir(Imagepath),key=lambda x:int(x.replace("Image","")))]
    Path_To_Pdf=f"{PdfPath}/{Name}.pdf"
    images[0].save(Path_To_Pdf,resolution=100.0,save_all=True,append_images=images[1:])


