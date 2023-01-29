from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen

# The name of the downloaded Shakespeare text for training
file_name = "input.txt"

# Train a custom BPE Tokenizer on the downloaded text
# This will save one file: `aitextgen.tokenizer.json`, which contains the
# information needed to rebuild the tokenizer.
train_tokenizer(file_name)
tokenizer_file = "aitextgen.tokenizer.json"

# GPT2ConfigCPU is a mini variant of GPT-2 optimized for CPU-training
# e.g. the # of input tokens here is 64 vs. 1024 for base GPT-2.
config = GPT2ConfigCPU()
data = TokenDataset(file_name, tokenizer_file=tokenizer_file, line_by_line=True)

# Instantiate aitextgen using the created tokenizer and config
ai = aitextgen(model="EleutherAI/gpt-neo-125M", tokenizer_file=tokenizer_file, config=config)

# You can build datasets for training by creating TokenDatasets,
# which automatically processes the dataset with the appropriate size.

# Train the model! It will save pytorch_model.bin periodically and after completion to the `trained_model` folder.
# On a 2020 8-core iMac, this took ~25 minutes to run.
ai.train(file_name,
         num_steps=10000,
         num_workers=0,
         line_by_line=True,
         generate_every=100,
         save_every=500,
         save_gdrive=False,
         learning_rate=1e-3,
         batch_size=1)

# Generate text from it!
ai.generate(10, prompt="ROMEO:")

# With your trained model, you can reload the model at any time by
# providing the folder containing the pytorch_model.bin model weights + the config, and providing the tokenizer.
ai2 = aitextgen(model_folder="trained_model",
                tokenizer_file="aitextgen.tokenizer.json")

ai2.generate(10, prompt="Apple:")
