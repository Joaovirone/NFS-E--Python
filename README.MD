Ao clicar no docker-compos.yml será visto as credenciais do banco, expostas mesmo, pra simplificar o aprendizado. A priori poderemos 
ir escalando o projeto conforme adquirirmos o aprendizado.

gostaria de utilizar as seguines portas

banco de dados = 4005

app web = 4000

ambas as portas estão sujeitas as mudanças


Pode ser necessário criar ambiente virtual ou venv




# No Windows/macOS/Linux
python -m venv venv

# Se for linux - ativação - no terminal rodar esse comando
.venv/bin/activate

# Se for windows - ativação - no terminal rodar esse comando
.\.venv\Scripts\activate.bat


pip install fastapi uvicorn[standard] pydantic[email] sqlalchemy alembic psycopg2-binary python-dotenv

pip install erpbrasil.base==2.4.1 nfelib==2.5.1