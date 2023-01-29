import os

from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen

from backend.settings import BASE_DIR

PATH_MODEL = os.path.join(BASE_DIR.absolute(), "model", 'model_dir')
FILE_NAME = "input.txt"


class PromptModel:
    def __init__(self):
        self.modelName = "EleutherAI/gpt-neo-350M"
        self.model = None
        self.tokenizer_file = "aitextgen.tokenizer.json"

    def buildModel(self):
        train_tokenizer(FILE_NAME)
        config = GPT2ConfigCPU()
        TokenDataset(FILE_NAME, tokenizer_file=self.tokenizer_file)
        self.model = aitextgen(model=self.modelName, tokenizer_file=self.tokenizer_file, config=config)
        self.model.train(
            FILE_NAME,
            num_steps=1000,
            num_workers=0,
            line_by_line=True,
            generate_every=100,
            save_every=500,
            save_gdrive=False,
            learning_rate=1e-3,
            batch_size=64
        )

    def saveModel(self, path):
        self.model.save(path)

    def predictModel(self, path_to_model, prompt):
        self.model = aitextgen(model_folder=PATH_MODEL, tokenizer_file=self.tokenizer_file, )
        description = self.model.generate(n=50, prompt=prompt, return_as_list=True)
        return description[0]
