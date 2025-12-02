import cv2
import numpy as np
from matplotlib import pyplot as plt

def load_image(path):
    """Load an image from a file path."""
    return cv2.imread(path)

def show_image(img, title="Image"):
    """Display an image using matplotlib."""
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

