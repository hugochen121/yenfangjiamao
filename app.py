


### the imports
import streamlit as st
import time
#import cv2



st.markdown("# Make your wish")
st.write("-"*100)

st.markdown("### 1. upload the files")
st.file_uploader('Upload the files', accept_multiple_files=True)
st.write("-"*100)


st.markdown("### 2. computing")
with st.spinner(text='In progress'):
	time.sleep(2)
	st.success('Done')
st.write("-"*100)



st.markdown("### 3. download output")
with open("0802幹部出勤表.PNG", "rb") as file:
    btn = st.download_button(
        label="幹部出勤表",
        data=file,
        file_name="0802幹部出勤表.png",
        mime="image/png"
    )


st.write(f'{"-"*30} 地球雙獅牌 嚴防假冒 {"-"*30}')