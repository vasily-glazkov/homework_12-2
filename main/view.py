from flask import Blueprint, render_template, request
from config import PATH
from functions import load_data, search_content
import logging

main = Blueprint('main', __name__, template_folder='templates')
data = load_data(PATH)


@main.route('/')
def main_page():
    return render_template('index.html')


@main.route('/post_list/')
def search_page():
    search_data = request.args.get('s')
    logging.info(f'Слово для поиска {search_data}')
    if search_data:
        items = search_content(search_data)
        if type(items) == list:
            return render_template("post_list.html", items=items, items_len=len(items), len_s=len(search_data),
                                   search_data=search_data)
        else:
            return render_template("post_list.html", n="Ничего не найдено", items_len=0, len_s=len(search_data),
                                   search_data=search_data)
    else:
        return render_template("post_list.html", n="Пустой ввод", items_len=0, len_s=len(search_data))
