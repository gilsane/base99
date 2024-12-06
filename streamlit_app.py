#기본적인 Streamlit 페이지 예제

# streamlit_app.py
import streamlit as st
import pandas as pd

# 1. 제목
st.title("장원재의 스트림릿 서비스")

# 2. 부제목
st.subheader("와우!!! 다양한 서비스!!!!")

st.title("만두는 최고야!!!!")

# 3. 판다스 데이터프레임 기반 표 출력
df = pd.DataFrame({
    "이름": ["장원재", "조용수", "Charlie"],
    "나이": [70, 99, 29],
    "나라": ["Korea", "USA", "UK"]
})
st.write("데이터프레임 예제")
st.dataframe(df)

# 4. HTML 활용 예제
st.write("HTML 예제")
st.markdown(
    """
    <div style="color: blue; font-size: 20px;">
        HTML을 활용한 예시 텍스트입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 5. HTML과 CSS 활용 예제
st.write("HTML과 CSS 예제")
st.markdown(
    """
    <style>
    .styled-box {
        padding: 20px;
        margin: 5px;
        background-color: lightgreen;
        border-radius: 5px;
        color: darkgreen;
    }
    </style>
    <div class="styled-box">
        HTML과 CSS를 함께 사용하여 스타일링한 박스입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 6. 이미지 표시
st.write("이미지 표시 예제")
st.image("https://i.namu.wiki/i/BQKa8GCZMjCRCDBzbCF7uBtPO_aHoflLZOreUGY7WOlL16HwLqJpxZv9IoAI2lviaDIgGJWf0iR_QR-rA9gGAQ.webp", caption="Streamlit 로고")

# 7. 유튜브 링크 (썸네일 표시)
st.write("유튜브 동영상 예제")
st.video("https://www.youtube.com/watch?v=aHNsrx8H21g")


st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3])
st.write_stream(my_generator)
st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("_Markdown_")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.html("<p>Hi!</p>")
