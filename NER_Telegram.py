# -*- coding: utf-8 -*-
import logging
from aiogram import Bot, Dispatcher, executor, types
from deeppavlov import configs, build_model


def ner_tagging_ret(message): #generator
    model_output = model([message])
    print(model_output)
    array_output = []
    for ind, elem in enumerate(model_output[1][0]):
        if elem != 'O':
            array_output.append(model_output[0][0][ind])
            array_output.append('(' + elem + ')')
        else:
            array_output.append(model_output[0][0][ind])
    return ' '.join(array_output)


API_TOKEN = '1946554521:AAEVXzv9YHmwn9X5o0M9YqAFStIagMbh7uc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def greetings(message: types.Message):
    await message.answer("Hi! I'm all yours to get tags you badly needed.")


@dp.message_handler()
async def echo(message: types.Message):
    answer = ner_tagging_ret(message.text)
    await message.answer(answer)


model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)