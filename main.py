# -*- coding: utf-8 -*-
from deeppavlov import configs, build_model


def ner_tagging(array_output):
    model_output = model(array_output)
    array_output = []
    for ind,elem in enumerate(model_output[1][0]):
        if elem != 'O':
            array_output.append(model_output[0][0][ind])
            array_output.append('(' + elem + ')')
        else:
            array_output.append(model_output[0][0][ind])
    with open(r"C:\Users\Максим\PycharmProjects\BERT_with_CUDA\text.txt", "a", encoding="utf-8") as file:
        file.write(' '.join(array_output))
        file.write('<SEPARATE>' + '\n')

model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)
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

print("Done!")