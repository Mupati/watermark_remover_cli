from PIL import Image, ImageEnhance
from tempfile import TemporaryDirectory
from pdf2image import convert_from_path
# from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError


class WatermarkRemover:

    def __init__(self, file_path, file_type=''):
        self.file_path = file_path
        # optional file_type passed from cli
        # create a validation method later on
        self.file_type = file_type

    def pdf_to_images(self) -> list:
        with TemporaryDirectory() as path:
            pil_images = convert_from_path(self.file_path, output_folder=path)
            return pil_images

    def enhance_image(self, pil_image):
        img = ImageEnhance.Contrast(pil_image).enhance(2.8)
        enhanced_image = img.convert('RGBA')
        return enhanced_image

    def clear_watermark(self, pil_images: list):
        image_store = []
        for img in pil_images:
            im = self.enhance_image(img)
            R, G, B = im.convert('RGB').split()
            r = R.load()
            g = G.load()
            b = B.load()
            w, h = im.size

            # Convert non-black pixels to white
            for i in range(w):
                for j in range(h):
                    if(r[i, j] > 100 or g[i, j] > 100 or b[i, j] > 100):
                        r[i, j] = 255  # Just change R channel

            # Merge just the R channel as all channels
            im = Image.merge('RGB', (R, R, R))
            image_store.append(im)
        return image_store

    def imgs_to_pdf(self, pil_images: list) -> None:
        pil_images[0].save('processed_file.pdf', save_all=True,
                           append_images=pil_images[1:])
