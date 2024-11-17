import os
import PyPDF2

def get_valid_input(prompt, validation_type='path'):
    """
    Get and validate user input for paths
    """
    while True:
        user_input = input(prompt).strip()
        
        if validation_type == 'folder':
            if os.path.isdir(user_input):
                return user_input
            print("Error: Invalid folder path. Please enter a valid directory path.")
        
        elif validation_type == 'output':
            try:
                # Check if the directory of the output file exists
                output_dir = os.path.dirname(user_input)
                if output_dir and not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                return user_input
            except Exception as e:
                print(f"Error: Invalid output path. {str(e)}")

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return ""

def main():
    # Get input folder path
    folder_path = get_valid_input(
        "Enter the folder path containing PDF files: ",
        validation_type='folder'
    )
    
    # Get output file path
    output_txt_path = get_valid_input(
        "Enter the output text file path (e.g., output.txt): ",
        validation_type='output'
    )
    
    # Start string to save text
    all_text = ''
    pdf_count = 0
    
    # Iteration for all files in the folder path
    print("\nStarting PDF text extraction...")
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            print(f'Extracting text from: {filename}')
            
            text = extract_text_from_pdf(pdf_path)
            if text:  # Only add text if extraction was successful
                all_text += f"\n--- {filename} ---\n{text}\n"
                pdf_count += 1
    
    # Save text only if there's content to save
    if all_text:
        try:
            with open(output_txt_path, 'w', encoding='utf-8') as output_file:
                output_file.write(all_text.strip())
            print(f'\nSuccess! Text from {pdf_count} PDFs was saved to {output_txt_path}')
        except Exception as e:
            print(f"Error saving the output file: {str(e)}")
    else:
        print("\nNo PDF files were successfully processed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")