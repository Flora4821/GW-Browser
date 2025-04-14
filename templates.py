def retrieve_columns(tables:list[str], columns:list[str], ids=None):
    query = "SELECT"
    for c in columns:
        query += f" {c},"
    query = query[:-1] + f" FROM {tables[0]}"
    
    if len(tables) > 1:
        for i in range(1, len(tables)):
            query += f" INNER JOIN {tables[i]} ON {ids[(i*2)-2]} = {ids[(i*2)-1]}"

    return query

def add_condition(query:str, condition:str):
    query += condition
    return query