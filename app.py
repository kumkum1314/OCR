import gradio as gr
from PIL import Image
import pytesseract

# OCR function using Pytesseract
def ocr_process(image):
    text = pytesseract.image_to_string(image, lang='eng+hin')  # Extract text from image
    return text

# Function to search keywords
def search_text(extracted_text, keyword):
    return keyword in extracted_text

# Build the interface
with gr.Blocks() as demo:
    image = gr.Image(type="pil")  # Upload image
    keyword = gr.Textbox(label="Enter keyword to search")  # Keyword input
    output_text = gr.Textbox(label="Extracted text")  # Show extracted text
    search_result = gr.Label(label="Search result")  # Search result

    def process(image, keyword):
        text = ocr_process(image)  # Extract text
        found = search_text(text, keyword)  # Search for the keyword
        return text, "Keyword found!" if found else "Keyword not found."

    btn = gr.Button("Submit")
    btn.click(process, inputs=[image, keyword], outputs=[output_text, search_result])

demo.launch(server_port=7863, share = True)  
