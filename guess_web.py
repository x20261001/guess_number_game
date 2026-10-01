import streamlit as st
import random
st.title("力力专属小游戏🎮-20261001")
if st.session_state.get("celebrate",False):
    st.balloons()
    st.session_state.celebrate = False
st.write("电脑已经想好了一个1到100之间的数字,快来猜猜看!")
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1,100)
    st.session_state.message = "游戏开始,输入你的猜测吧!"
    st.session_state.attempts = 0
st.info(st.session_state.message)
with st.form(key="guess_form",clear_on_submit=False):
    col1,col2 = st.columns([3,1])
    with col1:
        guess = st.number_input("请输入你猜的数字:",min_value=1,max_value=100,value=50)
    with col2:
        st.write("")
        submit_button = st.form_submit_button(label="提交猜测")
if st.button("重新开始游戏🎮"):
    st.session_state.secret_number = random.randint(1,100)
    st.session_state.message = "游戏🎮已重置,电脑重新想了个新的数字,继续猜吧!"
    st.session_state.attempts = 0
    st.rerun()
if submit_button:
    st.session_state.attempts += 1
    if guess == st.session_state.secret_number:
        st.session_state.message = f"恭喜你,猜对啦!!你总共猜了{st.session_state.attempts}次!游戏已重置,电脑重新想了个数字,继续猜吧!"
        st.session_state.secret_number = random.randint(1,100)
        st.session_state.attempts = 0
        st.session_state.celebrate = True
    elif guess > st.session_state.secret_number:
        st.session_state.message = "猜大了,往小了猜猜看!"
    else:
        st.session_state.message = "猜小了,往大了猜猜看!"
    st.rerun()
        
