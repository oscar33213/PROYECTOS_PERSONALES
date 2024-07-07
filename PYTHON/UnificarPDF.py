import streamlit as st
from PyPDF2 import PdfMerger

def merge_pdf(output_path, pdf_documents):
    pdf_merger = PdfMerger()
    
    for pdf_document in pdf_documents:
        pdf_merger.append(pdf_document)
        
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

def main():
    st.header('Unir PDFs')
    st.subheader('Adjunte archivos .pdf')
    
    attached_pdfs = st.file_uploader(label='', accept_multiple_files=True, type='pdf')
    
    merge_button = st.button(label='Unir PDFs')
    
    if merge_button:
        if not attached_pdfs or len(attached_pdfs) <= 1:
            st.warning('Adjunte más PDFs')
        else:
            output_pdf = 'pdf_final.pdf'
            merge_pdf(output_pdf, attached_pdfs)
            st.success('Los archivos se han unido correctamente')
            
            with open(output_pdf, 'rb') as file:
                pdf_data = file.read()
            st.download_button(label='Descargar PDF', data=pdf_data, file_name='pdf_final.pdf')

if __name__ == '__main__':
    main()

