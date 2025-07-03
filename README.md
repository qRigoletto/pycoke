# pycoke


# 🧹 Renomeador de Arquivos e Diretórios Inconsistentes

Este script Python renomeia arquivos e pastas com nomes inválidos, problemáticos ou confusos em sistemas de arquivos Linux/Windows. Ele aplica regras conservadoras para garantir compatibilidade, legibilidade e evitar erros futuros.

---

## ✨ Funcionalidades

- Detecta e remove caracteres **ilegais** (`< > : " / \ | ? *`, etc.)
- Corrige:
  - Espaços múltiplos
  - Espaços no início ou fim do nome
  - Pontos no início ou fim do nome
  - Caracteres indesejados (como `💥`, `%`, `@`, etc.)
- Garante nomes válidos e limpos para arquivos e diretórios
- Renomeia automaticamente e exibe um relatório com as alterações

---

## 📦 Requisitos

- Python **3.7** ou superior
- Nenhuma biblioteca externa é necessária (usa apenas a biblioteca padrão)

---

## 🚀 Como usar

1. **Clone ou baixe** este repositório:

   ```bash
   git clone https://github.com/qRigoletto/pycoke.git
   cd pycoke
