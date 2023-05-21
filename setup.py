# -*- coding: utf-8 -*-
import requests

from pathlib import Path
from tqdm import tqdm

####################
# GPT4All Model
####################

# This is the path where the model will be downloaded to.
gpt4all_path = './models/ggml-gpt4all-j-v1.3-groovy.bin'

Path(gpt4all_path).parent.mkdir(parents=True, exist_ok=True)

# Check https://github.com/nomic-ai/gpt4all for the latest models.
gpt4all_url = 'http://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin'

# Send a GET request to the URL to download the file. Stream since it's large
response = requests.get(gpt4all_url, stream=True)

# Open the file in binary mode and write the contents of the response to it in chunks
# This is a large file, so be prepared to wait.
with open(gpt4all_path, 'wb') as f:
  for chunk in tqdm(response.iter_content(chunk_size=8192)):
    if chunk:
      f.write(chunk)

####################
# Llama Model
####################

# This is the path where the model will be downloaded to.
llama_path = './models/ggml-model-q4_0.bin'

Path(llama_path).parent.mkdir(parents=True, exist_ok=True)

# LLama 7b model encoded in 4bits.
llama_url = 'https://huggingface.co/Pi3141/alpaca-native-7B-ggml/resolve/main/ggml-model-q4_0.bin'

# Send a GET request to the URL to download the file. Stream since it's large
response = requests.get(llama_url, stream=True)

# open the file in binary mode and write the contents of the response to it in chunks
# This is a large file, so be prepared to wait.
with open(llama_path, 'wb') as f:
  for chunk in tqdm(response.iter_content(chunk_size=8192)):
    if chunk:
      f.write(chunk)
