from templates import *
from database import *

def get_post_id(postnumber:str):
    tables = ["posts"]
    columns = ["postID"]
    return execute_query(add_condition(retrieve_columns(tables, columns), f" WHERE postnumber = {postnumber}"))[0][0]

def get_post_info(post_id:str, translated:bool=False):
    tables = ["posts AS P", "texts AS T", "users AS U"]
    columns = ["P.title", "T.content", "T.date", "U.naverID"]
    if translated:
        columns[0] = "P.translated"
        columns[1] = "T.translated"
    ids = ["P.textID", "T.textID", "T.userID", "U.userID"]
    return execute_query(add_condition(retrieve_columns(tables, columns, ids), f" WHERE postID = {post_id}"))[0]

def get_comments(post_id:str, translated:bool=False):
    tables = ["comments AS C", "texts AS T", "users AS U"]
    columns = ["T.content", "T.date", "U.naverID"]
    if translated: columns[0] = "T.translated"
    ids = ["C.textID", "T.textID", "T.userID", "U.userID"]
    return execute_query(add_condition(retrieve_columns(tables, columns, ids), f" WHERE postID = {post_id}"))

def get_images(post_id:str):
    tables = ["images"]
    columns = ["image"]
    return [image[0] for image in execute_query(add_condition(retrieve_columns(tables, columns), f" WHERE postID = {post_id}"))]

def get_post_display(translated:bool=False, condition=None):
    tables = ["posts AS P", "texts AS T", "users AS U"]
    columns = ["P.postnumber", "P.title", "T.date", "U.naverID"]
    if translated: columns[1] = "P.translated"
    ids = ["P.textID", "T.textID", "T.userID", "U.userID"]
    query = retrieve_columns(tables, columns, ids)
    if condition:
        query += condition
    print(query)
    return execute_query(query)

def get_post(postnumber, translated:bool=False):
    post_id = get_post_id(postnumber)
    raw_post_info = get_post_info(post_id, translated)
    raw_comments = get_comments(post_id, translated)
    raw_images = get_images(post_id)
    post_info = {
        "Title": raw_post_info[0],
        "Content": raw_post_info[1],
        "Date": raw_post_info[2],
        "NaverID": raw_post_info[3],
        "Comments": [{
            "Content": comment[0],
            "Date": comment[1],
            "NaverID": comment[2]
        } for comment in raw_comments],
        "Images": raw_images
    }

    return post_info
