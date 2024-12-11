from openai import OpenAI
import streamlit as st

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
client = OpenAI(api_key=OPENAI_API_KEY)

st.title('🎁 제품 홍보 포스터 생성기')

keyword = st.text_input("키워드를 입력하세요.")
if st.button("생성하기"):
    with st.spinner("열심히 작성하고 있어요!"):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system",
                 "content": "입력받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 만들어줘"
                 },
                {"role": "user",
                 "content": keyword
                 }
            ]
        )
        st.success(response.choices[0].message.content)

        # 제품 홍보 포스터 생성
        with st.spinner("열심히 생성하고 있어요!"):
            image_response = client.images.generate(
                model="dall-e-3",
                prompt=f'{keyword}에 대한 효과적인 제품 홍보 포스터를 그려줘',
                size="1024x1024",
                n=1,
            )
        image_url = image_response.data[0].url
        st.image(image_url)  # 생성된 포스터 출력