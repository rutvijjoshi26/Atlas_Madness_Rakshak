import os
import nltk

# Set the absolute path for download directory
download_dir = "/tmp/nltk_data"

# Download the necessary NLTK data
nltk.download('punkt', download_dir=download_dir)
nltk.download('wordnet', download_dir=download_dir)
nltk.download('averaged_perceptron_tagger', download_dir=download_dir)
