import streamlit as st
from processing_module import preprocess_review
from processing_module import count_word

# string pre_processor textbox
review_string = st.text_input("inpute review string")
pre_proccessed_string = preprocess_review(review_string)
# output
st.write(pre_proccessed_string)

# word_counter textbox
find_word = st.text_input("search for word")
count_time = count_word(pre_proccessed_string, find_word)
# output
st.write(f"The word '{find_word}' appears {count_time} times")
