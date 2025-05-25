# Solves — Subscription Management Microservice

**Solves** é um microserviço assíncrono de gerenciamento de assinaturas, focado em performance, escalabilidade e segurança.  
Desenvolvido com **FastAPI**, **Tortoise ORM**, **Celery**, **RabbitMQ**, e uma CLI poderosa usando **Typer**.

---

## 🚀 Tecnologias

- **FastAPI** — API web assíncrona e performática
- **Tortoise ORM + asyncpg** — ORM 100% async com PostgreSQL
- **Celery + RabbitMQ** — Processamento assíncrono de tarefas
- **Typer** — Interface de linha de comando elegante
- **Aerich** — Migrações para Tortoise ORM
- **JWT** — Autenticação segura
- **Pydantic v2** — Validações de dados modernas e robustas

---

## 📁 Estrutura do Projeto

```bash
.
├── app/                    # Código principal da aplicação
│   ├── models/            # Modelos Tortoise ORM
│   ├── schemas/           # Esquemas Pydantic
│   ├── tasks/             # Tarefas Celery
│   ├── dependencies/      # Dependências personalizadas
│   ├── services/          # Regras de negócio
│   ├── api/               # Rotas da API
│   ├── middlewares/       # Middlewares customizados
│   ├── services/          # Serviços auxiliares
│   ├── core/              # Configurações, constantes, utilitários
│   ├── .env               # Arquivo de variáveis de ambiente
│   └── main.py            # Ponto de entrada da API FastAPI
├── migrations/            # Migrações Tortoise ORM
├── cli.py                 # CLI usando Typer
├── celery_worker.py       # Worker Celery
├── docker-compose.yml     # Configuração do Docker Compose
└── requirements.txt       # Dependências


### Configurando variáveis de ambiente
Gere uma chave secreta segura:
```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"




# Rodar o servidor (modo dev com reload)
python cli.py runserver

# Rodar o worker do Celery
celery -A celery_worker.celery_app worker --loglevel=info

# Aplicar migrações do banco
aerich upgrade

