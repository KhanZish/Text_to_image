# -*- coding: utf-8 -*-
"""Text To Image Generation .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ySBKIP1ptcNgPkGjOW-UtWlbC6mwdiNG
"""

! pip install torch diffusers matplotlib transformers accelerate

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

authorization_token = ""
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=authorization_token)
pipe.to(device)

with autocast(device):
  textprompt = str(input("Enter your prompt: "))

  image = pipe(textprompt, guidance_scale=8.5).images[0]

  imgplot = plt.imshow(image)

with autocast(device):
  textprompt = str(input("Enter your promt: "))

  image = pipe(textprompt, guidance_scale=8.5).images[0]

  imgplot = plt.imshow(image)

with autocast(device):
  textprompt = str(input("Enter your promt: "))

  image = pipe(textprompt, guidance_scale=8.5).images[0]

  imgplot = plt.imshow(image)

with autocast(device):
  textprompt = str(input("Enter your promt: "))

  image = pipe(textprompt, guidance_scale=8.5).images[0]

  imgplot = plt.imshow(image)

with autocast(device):
  textprompt = str(input("Enter your promt: "))

  image = pipe(textprompt, guidance_scale=8.5).images[0]

  imgplot = plt.imshow(image)

with autocast(device):
  textprompt = str(input("Enter your promt: "))

  image = pipe(textprompt, guidance_scale=8.5).images[0]

  imgplot = plt.imshow(image)