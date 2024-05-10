import streamlit as st
import re
from wordcloud import WordCloud
from janome.tokenizer import Tokenizer
st.sidebar.text("config")
width = st.sidebar.slider("width", 0, 1200, 800, 10)
height = st.sidebar.slider("height",0, 1200, 500, 10)
min_text_size = st.sidebar.slider("min_text_size", 0, 50, 15, 1)
max_text_size = st.sidebar.slider("max_text_size", 0, 300, 110, 1)
theme = st.sidebar.selectbox("theme", ["YlOrRd","gray","YlGnBu", "cool"])
omit_words = st.sidebar.text_input("除外したいテキスト(スペース区切り)")
st.title("Word Cloud Maker")
text = st.text_input("ワードクラウドにしたい文章を入れてね。（500文字以上推奨。）")
# omit_words_list = omit_words.split(" ")
omit_words_list = re.split(r'[ 　]+', omit_words) #半角スペース、全角スペースいずれも同じに扱う。
def nouns_maker(text):
    tokenizer = Tokenizer()
    noun_list = []
    for token in tokenizer.tokenize(text):
        p = token.part_of_speech.split(",")
        if p[0] == "名詞":
            if token.surface not in omit_words_list:
                noun_list.append(token.surface)
    nouns = " ".join(noun_list)
    return nouns


if st.button("Create WordCloud"):
    wc = WordCloud(width=width, height=height, font_path="ipaexg.ttf", min_font_size=min_text_size, max_font_size=max_text_size,
                   collocations =False,colormap=theme)
    wc.generate(nouns_maker(text))
    wc.to_file('result.png')
    st.image("result.png")
