import os
import google.generativeai as genai
import PIL.Image

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# for models in genai.list_models():
#     print(models)
    
# for models in genai.list_models():
#     if 'generateContent' in models.supported_generation_methods:
#         print (models.name)
  
model= genai.GenerativeModel('gemini-1.5-flash',generation_config={"response_mime_type": "text/plain"})

# response = model.generate_content("What is the meaning of life?")
# print(response.text)

import PIL.Image
img = PIL.Image.open('engine.png')

response=model.generate_content(img)

# Print the extracted text
print(response.text)

