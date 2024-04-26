import streamlit as st
from wordcloud import WordCloud
from janome.tokenizer import Tokenizer
st.title("Word Cloud Maker")
text = st.text_input("ワードクラウドにしたい文章を入れてね。（500文字以上推奨。）")
def nouns_maker(text):
    tokenizer = Tokenizer()
    noun_list = []
    for token in tokenizer.tokenize(text):
        p = token.part_of_speech.split(",")
        if p[0] == "名詞":
            noun_list.append(token.surface)
    nouns = " ".join(noun_list)
    return nouns
if st.button("Create WordCloud"):
    wc = WordCloud(width=740, height=520,font_path="ipaexg.ttf",min_font_size=15,max_font_size=60,colormap="YlGn")
    wc.generate(nouns_maker(text))
    wc.to_file('result.png')
    st.image("result.png")