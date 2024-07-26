import os
import PyPDF2

#print(os.getcwd())  #Isso imprime o diretório de trabalho atual

#Função para extrair texto de um arquivo PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

#Caminho da pasta contendo os arquivos PDF
folder_path = ''

#Caminho do arquivo de texto de saída
output_txt_path = ''

#Inicializa uma string para armazenar todo o texto
all_text = ''

#Itera por todos os arquivos na pasta
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        print(f'Extraindo texto de: {pdf_path}')
        text = extract_text_from_pdf(pdf_path)
        all_text += text + '\n'

#Salva todo o texto extraído em um único arquivo .txt
with open(output_txt_path, 'w', encoding='utf-8') as output_file:
    output_file.write(all_text)

print(f'Todo o texto foi salvo em {output_txt_path}')