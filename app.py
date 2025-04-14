from flask import Flask, render_template, request
from markupsafe import escape
from functionality import *

app = Flask(__name__)

@app.route("/posts")
def posts_overview():
    
    translated = request.args.get("translated", "false").lower() == "true"
    full_data = get_post_display(translated)
    page = int(request.args.get('page', 1))
    per_page = 1000
    offset = (page - 1) * per_page
    total_pages = (len(full_data) + per_page - 1) // per_page

    paged_data = full_data[offset: offset + per_page]
    return render_template("post_overview.html", data=paged_data, page=page, total_pages=total_pages, translated=translated)

@app.route("/posts/<int:post_id>")
def post(post_id):
    translated = request.args.get("translated", "false").lower() == "true"
    data = get_post(post_id, translated)
    return render_template("post.html", data=data, translated=translated, post_id=post_id)

@app.route("/users/<user>")
def user_posts(user):
    translated = request.args.get("translated", "false").lower() == "true"
    full_data = get_post_display(translated, f" WHERE U.naverID = \'{user}\'")
    page = int(request.args.get('page', 1))
    per_page = 1000
    offset = (page - 1) * per_page
    total_pages = (len(full_data) + per_page - 1) // per_page

    paged_data = full_data[offset: offset + per_page]
    return render_template("post_overview.html", data=paged_data, page=page, total_pages=total_pages, translated=translated)