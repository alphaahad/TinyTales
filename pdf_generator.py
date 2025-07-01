from fpdf import FPDF
import textwrap
import os
from datetime import datetime
import unicodedata

def clean_text(text):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

def create_pdf(story_text, filename=None):
    class SimplePDF(FPDF):
        def add_story(self, title, text):
            self.add_page()
            self.set_font("Times", 'B', 16)
            self.cell(0, 10, title, ln=True, align='C')
            self.ln(10)
            self.set_font("Times", '', 12)
            wrapped_text = textwrap.wrap(text, width=100)
            for line in wrapped_text:
                self.multi_cell(0, 8, line)
                self.ln(0.5)

    story_text = clean_text(story_text)

    title = story_text.split(".")[0].strip()
    if len(title) > 60 or len(title) < 5:
        title = "A TinyTales Story"

    pdf = SimplePDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_story(title, story_text)

    if not filename:
        filename = f"tinytales_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    save_path = os.path.join("output", filename)
    os.makedirs("output", exist_ok=True)
    pdf.output(save_path)

    return save_path
