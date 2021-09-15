import utils
from deeppavlov import configs, build_model

#model = build_model(configs.squad.squad, download=True)
model = build_model(configs.squad.squad_ru_bert, download=True)


def answer(text, question):
    print(question.strip('\n'))
    print(model([text,], [question,])[0][0])
    print(model([text, ], [question, ]))


def get_texts(filepath):
    texts = []
    text = []
    buf = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if '<SEPARATE>' in line:
                for question in buf:
                    text.append(question)
                texts.append(text)
                text = []
                buf = []
            elif '<QUESTIONS>' in line:
                text.append(''.join(buf))
                buf = []
            else:
                buf.append(line)
    return texts


texts = get_texts(r"C:\Users\Максим\PycharmProjects\BERT_with_CUDA\text_QA.txt")

for text in texts:
    print("\nТЕКСТ:\n" + text[0].strip("\n"))
    for question in text[1:]:
        print("ВОПРОС:")
        answer(text[0], question)
