from flask import Blueprint, render_template, request
from functions import save_data_to_json
import logging

UPLOAD_FOLDER = "uploads/images/"

loader = Blueprint('loader', __name__, template_folder='templates', static_folder='static')


@loader.route("/post_form")
def page_post_form():
    return render_template('post_form.html')


@loader.route("/post_uploaded", methods=["POST"])
def page_post_upload():
    try:
        dict_results = {}

        # Создаем множество расширений
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

        # Получаем файл
        picture = request.files.get("picture")

        # Получаем контент
        content = request.form['content']
        if picture and content:
            # Получаем имя файла у загруженного файла
            filename = picture.filename.strip().replace(" ", "_")

            # Получаем расширение файла
            extension = filename.split(".")[-1]

            if extension in ALLOWED_EXTENSIONS:
                picture.save(f'{UPLOAD_FOLDER}{filename}')
                path = f'{UPLOAD_FOLDER}{filename}'
                dict_results['pic'] = "/" + path
                dict_results['content'] = content
                save_data_to_json(dict_results)
                return render_template('post_uploaded.html', path=path, content=content)
            else:
                logging.info(f"Тип файлов {extension} не поддерживается")
                return f"Тип файлов {extension} не поддерживается"
        else:
            return "Ошибка загрузки"
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return "<h1>Файл не найден</h1>"
