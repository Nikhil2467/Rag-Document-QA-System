# ----- Old code -----
import fitz  # PyMuPDF

def extract_text_chunks_from_pdf(pdf_path, chunk_size=500,overlap=150): #500 new added overlap
    """
    Returns a list of tuples: (chunk_text, page_number)
    """
    chunks = []
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc):
        text = page.get_text()
        # split page text into chunks
        for i in range(0, len(text), chunk_size):
            chunk_text = text[i:i+chunk_size]
            chunks.append((chunk_text, page_num + 1))  # page_num +1 for human-friendly
    return chunks


