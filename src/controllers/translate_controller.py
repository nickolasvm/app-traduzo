from flask import Blueprint, request, render_template
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()

    if request.method == "POST":
        source = request.form.get("translate-from")
        target = request.form.get("translate-to")
        text_to_translate = request.form.get("text-to-translate")
        translated = GoogleTranslator(source, target).translate(
            text_to_translate
        )

        return render_template(
            "index.html", languages=languages, translated=translated
        )
    else:
        return render_template(
            "index.html",
            languages=languages,
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
