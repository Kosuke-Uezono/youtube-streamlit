import streamlit as st
import time

st.title("streamlit")

left_col, right_col = st.columns(2)
button = left_col.button("右カラムに文字を表示")
if button:
    right_col.write("ここは右カラム")

expander1 = st.expander("問い合わせ")
for i in range(4):
    expander1.write("問い合わせ内容を書く")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ内容を書く")
expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ内容を書く")

option = st.sidebar.text_input("あなたの趣味を教えてください。")
condition = st.sidebar.slider("あなたの調子は？", 0, 100, 50, 10)



"あなたの趣味：", option
"コンディション：", condition

# if st.checkbox("Show Image"):
#     img = Image.open(r"C:\\Users\\kosuke.u\\OneDrive\\デスクトップ\\IMG_0606.jpg")
#     st.image(img, caption="Image", use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

# option