from database.DB_connect import DBConnect

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    def __init__(self):
        pass

    def get_all_filiali(self):
        conn = DBConnect.get_connection()
        query = "SELECT nome FROM filiale"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row["nome"] for row in data]

    def get_data(self, amount):
        conn = DBConnect.get_connection()
        query = """select LEAST(f1.nome, f2.nome) as nomeP, GREATEST(f1.nome,f2.nome) as nomeD, AVG(importo) as media from filiale f1 inner join bonifico b 
                    on f1.id  = b.id_filiale_origine inner join filiale f2 on f2.id = b.id_filiale_destinazione 
                    group by nomeP, nomeD having media >= %s"""

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (amount,))

        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data