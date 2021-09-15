import utils
from deeppavlov import configs, build_model


def ner_tagging_ret(message, model):
    """
    Function performs NER-markup.
    :param message: object of types.Message type from aiogram.
    :param model: NER-model from deeppavlov.
    :return: object of str type with NER-tagging.
    """
    model_output = model([message])
    array_output = utils.grouping(list(utils.unpacking(model_output)))
    return ' '.join(utils.unpacking(array_output))


def ner_tagging(array_output):
    model_output = model(array_output)
    array_output = []
    for ind, elem in enumerate(model_output[1][0]):
        if elem != 'O':
            array_output.append(model_output[0][0][ind])
            array_output.append('(' + elem + ')')
        else:
            array_output.append(model_output[0][0][ind])
    with open(r"C:\Users\Максим\PycharmProjects\BERT_with_CUDA\text.txt", "a", encoding="utf-8") as file:
        file.write(' '.join(array_output))
        file.write('<SEPARATE>' + '\n')


model = build_model(configs.ner.ner_rus_bert, download=False)
buf = []
array_output = []
with open(r"C:\Users\Максим\PycharmProjects\BERT_with_CUDA\Unprocessed.txt", "r", encoding = "utf-8" ) as file:
    for line in file:
        if '<SEPARATE>' in line:
            array_output.append(''.join(buf))
            ner_tagging(array_output)
            array_output = []
            buf = []
        else:
            buf.append(line)

text_1 = 'DeepPavlov is library for NLP and dialog systems.'

text_2 = 'Развитие фотосинтеза позволило живым организмам использовать солнечную энергию напрямую. \
Это привело к наполнению кислородом атмосферы, начавшемуся примерно 2,5 млрд лет назад, а в верхних слоях — к формированию озонового слоя. \
Симбиоз мелких клеток с более крупными привёл к развитию сложных клеток — эукариот. \
Примерно 2,1 млрд лет назад появились многоклеточные организмы, которые продолжали приспосабливаться к окружающим условиям. \
Благодаря поглощению губительного ультрафиолетового излучения озоновым слоем жизнь смогла начать освоение поверхности Земли'

#answer(text_1, ('What is DeepPavlov?',))
#answer(text_2, ('Когда началось наполнение атмосферы кислородом?', 'Когда началось наполнение кислородом атмосферы?'))