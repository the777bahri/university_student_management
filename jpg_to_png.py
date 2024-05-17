from PIL import Image
class PicConvert:
    def __init__(self):
        self.name = 'why'

    def convert_jpg_to_png(self,jpg_file_path, png_file_path):
        # Open the JPEG image file
        img = Image.open(jpg_file_path)
        print(f"open {jpg_file_path}")
        # Save the image as PNG
        img.save(png_file_path, 'PNG')
        print(f"saved {jpg_file_path}")


    def run(self):
        # Usage example
        self.convert_jpg_to_png(f"images\\UTS building 11.jpg",f"images\\{self.name}.jpg")
    
