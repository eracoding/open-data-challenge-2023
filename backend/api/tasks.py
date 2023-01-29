import datetime
import os.path

from aitextgen.tokenizers import train_tokenizer

from api.networkModels import PromptModel
from api.search import SearchText, ValuesFromWiki
from backend.settings import BASE_DIR
from core.models import Category, Status, WikiKeys

from celery import shared_task
from datetime import datetime

PATH_MODEL = os.path.join(BASE_DIR.absolute(), "model")

FILE_NAME = "input.txt"


def createDirectoryForModel():
    path = os.path.join(PATH_MODEL, "model_dir")
    os.mkdir(path)
    return path


@shared_task(name="learnFromCategory")
def learnFromCategory():
    Status.objects.first().learn()
    values = ValuesFromWiki()
    all_values = values.resultValueFromWiki()
    str_file = "\n".join(all_values)
    file = open(FILE_NAME, "a+")
    file.write(str_file)
    model = PromptModel()
    model.buildModel()
    # path = createDirectoryForModel()
    model.saveModel(os.path.join(PATH_MODEL, "model_dir"))
    Status.objects.first().finish()
# model = PromptModel
# model.buildModel()
# model.trainModel(filename) # укажи путь на filename
# model.saveModel()
# description = model.predictModel(filepath, prompt)
# imageModel = ImageModel()
# image = imageModel.generate(description)
