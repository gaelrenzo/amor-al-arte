import os
import re
import subprocess
import shutil

# Target Google Colab Link
colab_link = "https://colab.research.google.com/github/gaelrenzo/amor-al-arte/blob/main/notebook_svar.ipynb"

def update_tex_file(file_path):
    print(f"Updating LaTeX file: {file_path}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace author-block placeholder
    old_author_placeholder = r'\texttt{[enlace al Google Colab]}'
    new_author_text = rf'\url{{{colab_link}}}'
    content = content.replace(old_author_placeholder, new_author_text)
    
    # Replace under-title link placeholder
    old_href_placeholder = r'\href{https://colab.research.google.com/drive/}{[Enlace al archivo de Google Colab]}'
    new_href_text = rf'\href{{{colab_link}}}{{Enlace al archivo de Google Colab}}'
    content = content.replace(old_href_placeholder, new_href_text)
    
    # Also handle alternate spellings or cases just in case
    content = re.sub(r'\[[Ee]nlace al Google Colab\]', colab_link, content)
    content = re.sub(r'\[[Ee]nlace al archivo de Google Colab\]', colab_link, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("LaTeX file updated.")
    return True

def update_docx_file(file_path):
    print(f"Updating Word file: {file_path}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
        
    import docx
    doc = docx.Document(file_path)
    replaced = False
    
    # Iterate through paragraphs
    for p in doc.paragraphs:
        if "[enlace al archivo de Google Colab]" in p.text:
            p.text = p.text.replace("[enlace al archivo de Google Colab]", colab_link)
            replaced = True
            print(f"Replaced in paragraph: {p.text[:60]}...")
            
        # Try checking for case variations
        elif "[Enlace al archivo de Google Colab]" in p.text:
            p.text = p.text.replace("[Enlace al archivo de Google Colab]", colab_link)
            replaced = True
            print(f"Replaced in paragraph: {p.text[:60]}...")
            
    doc.save(file_path)
    print("Word file saved.")
    return replaced

def compile_latex(file_path, output_dir="."):
    print(f"Compiling LaTeX file: {file_path}")
    # Run pdflatex. We run it twice to resolve references/citations.
    try:
        # Run pdflatex
        subprocess.check_call(["pdflatex", "-interaction=nonstopmode", file_path], cwd=os.path.dirname(file_path) or ".")
        subprocess.check_call(["pdflatex", "-interaction=nonstopmode", file_path], cwd=os.path.dirname(file_path) or ".")
        print("LaTeX compiled successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")
        return False

if __name__ == "__main__":
    # 1. Update LaTeX files
    update_tex_file("articulo_scopus.tex")
    update_tex_file("articulo 1/articulo_scopus.tex")
    
    # 2. Update Word files
    update_docx_file("articulo_scopus.docx")
    update_docx_file("informe_articulo.docx")
    update_docx_file("articulo 1/informe_articulo.docx")
    
    # 3. Compile LaTeX in root and copy to articulo 1
    if compile_latex("articulo_scopus.tex"):
        # Copy compiled PDF to 'articulo 1'
        if os.path.exists("articulo_scopus.pdf"):
            shutil.copy("articulo_scopus.pdf", "articulo 1/articulo_scopus.pdf")
            print("Copied compiled PDF to 'articulo 1/articulo_scopus.pdf'")
            
            # Also overwrite main.pdf in root since the user has main.pdf?
            # Wait, main.pdf was the EV conversion report! Let's NOT overwrite it unless needed.
            # But wait, in our git list, there was 'main.pdf' which was about the EV conversion.
            # Let's keep main.pdf as is, and keep 'articulo_scopus.pdf' as the SVAR article.
