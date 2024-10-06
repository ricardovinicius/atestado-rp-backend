# Aplicação FastAPI

## Como rodar a aplicação

### Pré-requisitos

- **Python 3.7+** instalado
- **Pip** para gerenciar pacotes
- **Virtualenv** (opcional, mas recomendado)

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Rodando a aplicação

1. Execute o servidor FastAPI:

   ```bash
   fastapi dev app/app.py
   ```

   - A aplicação estará disponível em `http://127.0.0.1:8000`.

2. Acesse a documentação interativa da API:

   - Swagger UI: `http://127.0.0.1:8000/docs`
   - Redoc: `http://127.0.0.1:8000/redoc`

### Testes (opcional)

Para rodar os testes, execute:

```bash
pytest
```
