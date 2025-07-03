# 🧹 PyCoke – Renomeador de Arquivos e Diretórios Inconsistentes

**PyCoke** é um script Python que renomeia arquivos e pastas com nomes inválidos, confusos ou problemáticos em sistemas de arquivos Linux/Windows. Ele aplica regras **conservadoras e seguras** para garantir compatibilidade, legibilidade e evitar erros futuros ao lidar com nomes de arquivos.

---

## ✨ Funcionalidades

- 🚫 Remove **caracteres ilegais** (`< > : " / \ | ? *`, entre outros)
- 🔧 Corrige:
  - Espaços **múltiplos**
  - Espaços no **início ou fim** do nome
  - Pontos no **início ou fim** do nome
  - Caracteres **indesejados** (como `💥`, `%`, `@`, etc.)
- 🧼 Garante nomes **limpos e compatíveis** para arquivos e diretórios
- 📝 Renomeia automaticamente e exibe um **relatório detalhado** das alterações

---

## 📦 Requisitos

- Python **3.7 ou superior**
- Nenhuma biblioteca externa (usa apenas a **biblioteca padrão** do Python)

---

## 🚀 Como usar

1. **Clone ou baixe** este repositório:

   ```bash
   git clone https://github.com/qRigoletto/pycoke.git
   cd pycoke
   ```

2. **Execute o script**:

   ```bash
   python3 script.py
   ```

3. **Informe o caminho completo da pasta** que deseja verificar e corrigir quando solicitado.

---

## ✅ Exemplo de uso

```bash
$ python3 script.py
Digite o caminho completo da pasta a ser verificada e corrigida: /home/usuario/Downloads

🔧 Renomeando entradas em: /home/usuario/Downloads

📝 Renomeado: "nome 💥 estranho.txt" → "nome estranho.txt"
📝 Renomeado: " arquivo.txt " → "arquivo.txt"
❌ Falha ao renomear "aberto.txt": [Errno 16] Device or resource busy

✅ Concluído! 2 itens renomeados, 1 erro
```

---

## 🔒 Licença

Distribuído sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

Desenvolvido por [Rigoletto (qRigoletto)](https://github.com/qRigoletto)
