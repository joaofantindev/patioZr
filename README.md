# Zella Patio

Projeto de estudos de integração entre balança, leitor de crachá e cadastro de caminhões em um pátio.

## O que faz

Fluxo básico: ler crachá → identificar placa → registrar peso → salvar no banco.

## Stack

- Python + Flask
- SQLite

## Endpoints

| Método | Rota              | Descrição                        |
|--------|-------------------|----------------------------------|
| GET    | `/`               | Confirmação de que o servidor está no ar |
| GET    | `/api/status`     | Estado do sistema                |
| POST   | `/api/cracha`     | Valida crachá e retorna a placa  |
| POST   | `/api/pesagem`    | Valida e registra um peso        |
| POST   | `/api/caminhao`   | Registra caminhão completo (crachá + peso) no banco |

## Rodando

```bash
pip install -r requirements.txt
python app.py
```

## Estrutura

```
app.py           # rotas HTTP
logic/           # regras de negócio (cracha, balanca, caminhao)
database/        # conexão e tabelas SQLite
services/        # leitura serial e logs (em breve)
templates/       # interface simples
```
