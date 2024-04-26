from janome.tokenizer import Tokenizer
text = "私の名前は古川格です。"
tokenizer = Tokenizer()
noun_list = []
for token in tokenizer.tokenize(text):
    p = token.part_of_speech.split(",")
    if p[0] == "名詞":
        noun_list.append(token.surface)
print(noun_list)
