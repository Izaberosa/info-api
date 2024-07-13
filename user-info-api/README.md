# User Info API

## Descrição
API para obter informações de usuários aleatórios utilizando Random User API.

## Funcionalidades:
GET /users: Retorna uma lista de usuários aleatórios

## Instalação
1. Clone o repositório:
git clone <repo-url>

2. Navegue até o diretório:
cd user-info-api

3. Construa o container Docker:
docker build -t user-info-api .

4. Execute o container:
docker run -p 5001:5000 user-info-api

## Endpoints
- `GET /users`