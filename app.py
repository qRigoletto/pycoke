import os
import re
import unicodedata
from typing import List, Tuple

# Caracteres realmente ilegais em sistemas de arquivos
STRICT_ILLEGAL_CHARS = r'[<>:"/\\|?*\x00-\x1F]'
STRICT_ILLEGAL_RE = re.compile(STRICT_ILLEGAL_CHARS)

# Caracteres indesejados (mas tecnicamente permitidos)
UNDESIRABLE_CHARS = r'[#%&{}\[\]$!\'@+`=💥]'
UNDESIRABLE_RE = re.compile(UNDESIRABLE_CHARS)

def nome_invalido(nome: str) -> List[str]:
    """Identifica problemas no nome do arquivo/diretório de forma mais conservadora."""
    motivos = []
    
    if STRICT_ILLEGAL_RE.search(nome):
        motivos.append("caractere ilegal no sistema de arquivos")
    
    if nome.startswith(' ') or nome.endswith(' '):
        motivos.append("espaço no início/fim")
    
    if nome.startswith('.') or nome.endswith('.'):
        motivos.append("ponto no início/fim")
    
    if re.search(r'\s{2,}', nome):
        motivos.append("espaços múltiplos")
    
    return motivos

def normalizar_nome(nome: str) -> str:
    """Normaliza o nome preservando o máximo possível do original."""
    original = nome
    
    # 1. Remove apenas caracteres estritamente ilegais
    nome = STRICT_ILLEGAL_RE.sub('', nome)
    
    # 2. Normaliza espaços (mas preserva um único espaço)
    nome = re.sub(r'\s{2,}', ' ', nome.strip())
    
    # 3. Remove pontos problemáticos (início/fim)
    nome = nome.strip('. ')
    
    # 4. Trata extensões de arquivo
    base, ext = os.path.splitext(nome)
    if ext:  # Se tem extensão
        base = base.strip('. ')  # Limpa base
        nome = f"{base}{ext}" if base else f"arquivo{ext}"
    else:  # Para diretórios ou arquivos sem extensão
        nome = base if base else "pasta"
    
    # 5. Remove caracteres indesejados (opcional)
    if UNDESIRABLE_RE.search(nome):
        nome = UNDESIRABLE_RE.sub('', nome)
        nome = nome.strip() or "arquivo"
    
    # Se normalização foi muito agressiva, mantém o original modificado minimamente
    if nome == "arquivo" or nome == "pasta":
        nome = re.sub(STRICT_ILLEGAL_CHARS, '', original)
        nome = re.sub(r'\s{2,}', ' ', nome.strip())
        nome = nome.strip('. ') or "arquivo"
    
    return nome

def renomear_entradas(raiz: str) -> Tuple[int, int]:
    """Renomeia arquivos e diretórios de forma mais conservadora."""
    print(f"\n🔧 Renomeando entradas em: {raiz}\n")
    alteracoes = 0
    erros = 0

    for dirpath, dirnames, filenames in os.walk(raiz, topdown=False):
        for nome in filenames + dirnames:
            caminho_antigo = os.path.join(dirpath, nome)
            nome_corrigido = normalizar_nome(nome)
            
            if nome_corrigido != nome:
                caminho_novo = os.path.join(dirpath, nome_corrigido)
                try:
                    os.rename(caminho_antigo, caminho_novo)
                    print(f"📝 Renomeado: \"{nome}\" → \"{nome_corrigido}\"")
                    alteracoes += 1
                except OSError as e:
                    print(f"❌ Falha ao renomear \"{nome}\": {e}")
                    erros += 1

    return alteracoes, erros

if __name__ == "__main__":
    pasta = input("Digite o caminho completo da pasta a ser verificada e corrigida: ").strip()

    if not os.path.isdir(pasta):
        print("❌ Caminho inválido ou inexistente.")
    else:
        alteracoes, erros = renomear_entradas(pasta)
        print(f"\n✅ Concluído! {alteracoes} itens renomeados, {erros} erros")
