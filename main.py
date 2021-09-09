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