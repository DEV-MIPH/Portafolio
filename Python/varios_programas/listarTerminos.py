def ListarTerminos (**terminos):
    for llave,valor in terminos.items():
        print(f'{llave}: {valor}')
        
ListarTerminos(IDE = 'Integrated Development Environment',PK= 'Primary Key')
ListarTerminos(DBMS= 'Database Management System')
