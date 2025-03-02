import os
import shutil

def organize_pdfs(directory):
  
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
   
    pdf_folder = os.path.join(directory, "PDFs")
    os.makedirs(pdf_folder, exist_ok=True)  
   

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path) and file.lower().endswith(".pdf"):
            shutil.move(file_path, os.path.join(pdf_folder, file))
            print(f"Moved: {file} -> {pdf_folder}")
    
    print("PDF organization complete.")


directory = "/Users/benedictdebrah/Documents/DevOps BootCamp/TechWorld with Nana - DevOps Bootcamp 2024-12"  # Change this to your target directory
organize_pdfs(directory)
