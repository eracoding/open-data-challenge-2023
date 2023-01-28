import json
import os
from datetime import datetime

import numpy as np
import pathlib

from aitextgen import aitextgen
from backend.settings import BASE_DIR
from core.models import GptNeo


class PromptModel:
    def __init__(self):
        self.modelName = "EleutherAI/gpt-neo-125M"
        self.model = None

    def buildModel(self):
        self.model = aitextgen(model=self.modelName, to_gpu=True)

    def trainModel(self, filename):
        self.model.train(filename,
                         line_by_line=True,
                         from_cache=False,
                         num_steps=500,
                         generate_every=100,
                         save_every=500,
                         save_gdrive=False,
                         learning_rate=1e-3,
                         fp16=False,
                         batch_size=1,
                         )

    def saveModel(self, path):
        self.model.save(path)
        GptNeo.objects.create(path=path)

    def predictModel(self, path_to_model, prompt):
        self.model = aitextgen(model_folder=path_to_model, to_gpu=True)
        description = self.model.generate(prompt=prompt)
        return description
