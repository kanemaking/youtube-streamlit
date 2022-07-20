import streamlit as st
import time
st.title('Streamlit 入門')

st.write('ブログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i +1)
    time.sleep(0.01)

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
       right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ１')
expander1.write('問い合わせの回答内容を書く')
expander2 = st.beta_expander('問い合わせ２')
expander2.write('問い合わせ２の内容を書く')
expander3 = st.beta_expander('問い合わせ３')
expander3.write('問い合わせ３の内容を書く')
#if st.checkbox('Show Image'):
 #   img = Image.open('sample.jpg')
 #   st.image(img, caption='Kohei Imanishi', use_column_width=True)

