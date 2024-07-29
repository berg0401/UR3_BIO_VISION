from image_fetcher import ImageFetcher
from text_reader import TextReader
from os import path

script_dir = path.dirname(path.abspath(__file__))
images_folder = path.join(script_dir,r"..\images_ecran")
#INIT THE SERVER
ImageFetcher = ImageFetcher(images_folder)
text_reader = TextReader()

#GET THE IMAGE AFTER THE CAPTURE
images_content = ImageFetcher.fetch()
for content in images_content:
    texts = text_reader.read(content)
    state_menu = text_reader.guess_menu(texts)
    text_reader.show_result(state_menu)
