import streamlit as st
st.title("Project Discussion")

from tensorflow.keras.models import load_model

# model=load_model("rnn1.keras",compile=False)
# new_review=st.text_area("Text to translate")

# st.write(model.summary())
# from tensorflow.keras.preprocessing.text import Tokenizer
# tk=Tokenizer()
# tk.fit_on_texts(new_review)
# seq=tk.texts_to_sequences(new_review)
# pad=pad_sequences(seq,maxlen=50,padding="post")
# model.predict(pad)
