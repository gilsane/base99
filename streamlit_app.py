import streamlit as st

# 페이지 데이터 정의 (이미지 URL과 YouTube 영상 URL)
pages = {
    "Page 1": {
        "images": [
            "https://via.placeholder.com/150",
            "https://via.placeholder.com/150",
            "https://via.placeholder.com/150",
            "https://via.placeholder.com/150",
        ],
        "videos": [
            "https://www.youtube.com/embed/dQw4w9WgXcQ",
            "https://www.youtube.com/embed/3JZ_D3ELwOQ",
            "https://www.youtube.com/embed/2Vv-BfVoq4g",
            "https://www.youtube.com/embed/L_jWHffIx5E",
        ],
    },
    "Page 2": {
        "images": [
            "https://via.placeholder.com/150/FF0000",
            "https://via.placeholder.com/150/00FF00",
            "https://via.placeholder.com/150/0000FF",
            "https://via.placeholder.com/150/FFFF00",
        ],
        "videos": [
            "https://www.youtube.com/embed/XqZsoesa55w",
            "https://www.youtube.com/embed/JGwWNGJdvx8",
            "https://www.youtube.com/embed/hT_nvWreIhg",
            "https://www.youtube.com/embed/2vjPBrBU-TM",
        ],
    },
    # 추가 페이지 정의 가능
}

# 사이드바에서 페이지 선택
st.sidebar.title("Page Selector")
selected_page = st.sidebar.selectbox("Select a page:", list(pages.keys()))

# 선택된 페이지 데이터 가져오기
page_data = pages[selected_page]
images = page_data["images"]
videos = page_data["videos"]

# 레이아웃 생성
col1, col2 = st.columns(2)

# 이미지 표시
with col1:
    st.header("Images")
    for i in range(0, len(images), 2):
        cols = st.columns(2)
        for j, img in enumerate(images[i:i+2]):
            cols[j].image(img, use_column_width=True)

# YouTube 동영상 표시
with col2:
    st.header("Videos")
    for i in range(0, len(videos), 2):
        cols = st.columns(2)
        for j, vid in enumerate(videos[i:i+2]):
            cols[j].markdown(
                f'<iframe width="200%" height="400" src="{vid}" frameborder="0" allowfullscreen></iframe>',
                unsafe_allow_html=True,
            )
