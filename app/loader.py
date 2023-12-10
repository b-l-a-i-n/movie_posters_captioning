from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from transformers import VisionEncoderDecoderConfig, VisionEncoderDecoderModel, ViTFeatureExtractor,BertTokenizer, ViTImageProcessor
from data.config import MODEL_NAME
import logging

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.warning('Model is loading')

encoder_decoder_config = VisionEncoderDecoderConfig.from_pretrained("{}".format(MODEL_NAME))
model = VisionEncoderDecoderModel.from_pretrained("{}".format(MODEL_NAME), config=encoder_decoder_config)

feature_extractor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224-in21k")
tokenizer = BertTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")

logging.warning('Model has been loaded')
