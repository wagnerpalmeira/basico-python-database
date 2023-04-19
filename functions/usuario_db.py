def insert(conexao, dados):
    cursor = conexao.cursor()

    sql = f'INSERT INTO usuarios(usuario_name, usuario_senha) VALUES (?, ?)'
    cursor.execute(sql, dados)
    conexao.commit()
    
    return True

def listar(conexao):
    cursor = conexao.cursor()
    sql = f'SELECT * FROM usuarios'
    cursor.execute(sql)
    dados = cursor.fetchall()

    return dados
