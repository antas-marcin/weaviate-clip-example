import ipyplot
from base64 import b64encode
import requests


def display_book_results(res):
    _plot_images(res, "cover_image", "title")


def display_amazon_results(res):
    _plot_images(res, "image_url", "name")


def _plot_images(res, image_property: str, label_property: str):
    images = []
    captions = []
    for o in res.objects:
        images.append(o.properties[image_property])
        captions.append(o.properties[label_property])

    ipyplot.plot_images(images, custom_texts=captions, img_width=150, show_url=False)


def get_image_blob(url: str) -> str:
    resp = requests.get(url)
    if resp.status_code == 200:
        return b64encode(resp.content).decode("utf-8")
    return ""


def get_first_n_elements(weaviate_data, n: int):
    data=[]
    for i, d in enumerate(weaviate_data):
        if i > n - 1:
            break
        else:
            data.append(d)
    return data
