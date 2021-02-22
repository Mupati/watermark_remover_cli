import argparse

from watermark_remover_cli.Watermarkremover import WatermarkRemover

# Create the parser
parser = argparse.ArgumentParser(
    description='Remove Watermarks from PDFs and Images')

# Add the arguments
parser.add_argument("-f", "--file", type=str,
                    help='The path to the PDF or Image file')

# Execute the parse_args() method
args = vars(parser.parse_args())

# Get the path supplied into the CLI
file_path = args['file']

# Do input validation


def main():

    print('Processing file...')
    remover = WatermarkRemover(file_path=file_path)

    pil_images = remover.pdf_to_images()
    cleared_images = remover.clear_watermark(pil_images=pil_images)
    remover.imgs_to_pdf(pil_images=cleared_images)

    print('Processing complete! check the current directory for processed_file.pdf')


if __name__ == '__main__':
    main()
