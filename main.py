# -*- coding: utf-8 -*-
import logging
from aiogram import Bot, Dispatcher, executor, types
from deeppavlov import configs, build_model
import nn_models

API_TOKEN = '1946554521:AAEVXzv9YHmwn9X5o0M9YqAFStIagMbh7uc'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)


@dp.message_handler(commands=['start'])
async def greetings(message: types.Message):
    await message.answer("Hi! I'm all yours to get tags you badly needed.")


@dp.message_handler()
async def echo(message: types.Message):
    answer = nn_models.ner_tagging_ret(message.text, model)
    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
