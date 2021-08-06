import utils


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
