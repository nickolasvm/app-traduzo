from flask import Blueprint, request, render_template
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        translated = GoogleTranslator(translate_from, translate_to).translate(
            text_to_translate
        )

        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )
    else:
        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate="",
            translate_from="pt",
            translate_to="en",
            translated="Tradução",
        )


@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    translated = GoogleTranslator(
        source=request.form.get("translate-to"),
        target=request.form.get("translate-from"),
    ).translate(request.form.get("text-to-translate"))

    text_to_translate = GoogleTranslator(
        source=request.form.get("translate-from"),
        target=request.form.get("translate-to"),
    ).translate(translated)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=request.form.get("translate-to"),
        translate_to=request.form.get("translate-from"),
        translated=translated,
    )
