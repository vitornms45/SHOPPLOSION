import json
import os
from flask import Flask, render_template, redirect, url_for, abort

app = Flask(__name__)

# Mapeia os códigos de idioma para os arquivos de tradução
SUPPORTED_LANGUAGES = ['pt', 'en', 'es']

def get_text_data(lang_code):
    """Carrega os dados de texto do arquivo JSON correspondente (versão corrigida)."""
    if lang_code not in SUPPORTED_LANGUAGES:
        lang_code = 'pt'  # Idioma padrão
    
    # --- INÍCIO DA MUDANÇA ---
    # Encontra o caminho absoluto para o diretório onde o script está
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Cria o caminho completo para o arquivo de tradução
    file_path = os.path.join(script_dir, 'translations', f'{lang_code}.json')
    # --- FIM DA MUDANÇA ---
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, aborta com um erro 404
        abort(404, description=f"Language file not found for '{lang_code}' at path: {file_path}")

@app.route('/')
def index():
    """Redireciona para o idioma padrão (português)."""     
    return redirect(url_for('serve_page', lang_code='pt'))


@app.route('/<lang_code>/')
def serve_page(lang_code):
    """Serve a página principal com o idioma selecionado."""
    if lang_code not in SUPPORTED_LANGUAGES:
        # Se o idioma na URL não for suportado, redireciona para o padrão
        return redirect(url_for('serve_page', lang_code='pt'))
    
    text_data = get_text_data(lang_code)
    
    return render_template(
        'index.html', 
        texts=text_data, 
        current_lang=lang_code,
        supported_langs=SUPPORTED_LANGUAGES
    )


if __name__ == '__main__':
    app.run(debug=True)   