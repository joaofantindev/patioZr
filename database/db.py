
import sqlite3


def conectar():
    conexao = sqlite3.connect("zella_patio.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS pesagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cracha TEXT NOT NULL,
            placa TEXT NOT NULL,
            peso REAL NOT NULL,
            unidade TEXT NOT NULL DEFAULT 'kg',
            data_hora TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_pesagem(cracha, placa, peso):
    conexao = conectar()

    conexao.execute(
        """
        INSERT INTO pesagens (cracha, placa, peso, unidade)
        VALUES (?, ?, ?, ?)
        """,
        (cracha, placa, float(peso), "kg")
    )

    conexao.commit()
    conexao.close()
