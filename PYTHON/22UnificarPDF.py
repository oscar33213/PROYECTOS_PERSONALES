import streamlit as st 
import PyPDF2

def merge_pdf(output_path, pdf_documents):
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf_document in pdf_documents:
        pdf_merger.append(pdf_document)
        
    with open (output_path, 'wb') as output_file:
        pdf_merger.write(output_file)


def main():
    
    st.header('Unir PDFs')
    st.subheader('Adjunte archivos .pdf')
    
    attached_pdfs = st.file_uploader(label='', accept_multiple_files=True)
    
    merge_button = st.button(label='Unir PDFs')
    
    
    if merge_button:
        if len(attached_pdfs) <= 1:
            st.warning('Adjunte mas PDFs')
        else:
            output_pdf = 'pdfs/pdf_final.pdf'
            merge_pdf(output_pdf, attached_pdfs)
            st.success('Los archivos se han unido correctamente')
            
            with open (output_pdf, 'rb') as file:
                pdf_data = file.read()
            st.download_button(label='Descaragar PDF', data=pdf_data, file_name='pdf_final.pdf')



if __name__ == '__main__':
    main()