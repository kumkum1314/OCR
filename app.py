import gradio as gr
from PIL import Image
import pytesseract

# OCR function using Pytesseract
def ocr_process(image):
    text = pytesseract.image_to_string(image, lang='eng+hin')  # Extract text from image
    return text

# Function to search keywords
def search_text(extracted_text, keyword):
    return "Keyword found!" if keyword in extracted_text else "Keyword not found."

# Build the interface
with gr.Blocks() as demo:
    # Upload image for OCR
    image_input = gr.Image(type="pil", label="Upload Image")

    # Keyword input to search in the extracted text
    keyword_input = gr.Textbox(label="Enter keyword to search")

    # Display extracted text
    output_text = gr.Textbox(label="Extracted text")

    # Display search result (whether keyword is found or not)
    search_result = gr.Label(label="Search result")

    # Button to submit and process the image and keyword
    btn = gr.Button("Submit")

    # Define what happens when the button is clicked
    def process(image, keyword):
        extracted_text = ocr_process(image)  # Perform OCR
        search_res = search_text(extracted_text, keyword)  # Search for the keyword
        return extracted_text, search_res

    # Link button click to the processing function
    btn.click(process, inputs=[image_input, keyword_input], outputs=[output_text, search_result])

# Launch the Gradio app
demo.launch(share=True)
