import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="논술 수업 학기말 자기평가", page_icon="✍️")

st.title("✍️ 논술 수업 학기말 학생 자기평가")
st.write("한 학기 동안의 논술 수업을 돌아보고 솔직하게 작성해 주세요.")

st.divider()

name = st.text_input("이름")
class_name = st.text_input("반")
number = st.text_input("번호")

st.subheader("1. 자기평가")

effort = st.slider("수업에 성실하게 참여했나요?", 1, 5, 3)
writing = st.slider("글쓰기 실력이 성장했다고 느끼나요?", 1, 5, 3)
discussion = st.slider("토론과 발표에 적극적으로 참여했나요?", 1, 5, 3)
homework = st.slider("과제와 제출물을 성실히 완성했나요?", 1, 5, 3)

st.subheader("2. 서술형 회고")

growth = st.text_area("이번 학기 논술 수업에서 가장 성장한 점은 무엇인가요?")
difficulty = st.text_area("가장 어려웠던 점은 무엇인가요?")
goal = st.text_area("다음 학기에는 어떤 점을 더 노력하고 싶나요?")

if st.button("제출하기"):
    if not name or not class_name or not number:
        st.warning("이름, 반, 번호를 모두 입력해 주세요.")
    else:
        data = {
            "제출시각": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "반": class_name,
            "번호": number,
            "이름": name,
            "성실도": effort,
            "글쓰기 성장": writing,
            "토론 참여": discussion,
            "과제 완성": homework,
            "성장한 점": growth,
            "어려웠던 점": difficulty,
            "다음 목표": goal,
        }

        df = pd.DataFrame([data])
        file_path = "responses.csv"

        if os.path.exists(file_path):
            df.to_csv(file_path, mode="a", header=False, index=False, encoding="utf-8-sig")
        else:
            df.to_csv(file_path, index=False, encoding="utf-8-sig")

        st.success("제출이 완료되었습니다. 성실하게 작성해 줘서 고마워요!")
