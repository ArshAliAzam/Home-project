import streamlit as st
import random



st.title("🐍 Welcome to Arsh Web")
st.header("""First
          Ramadan mubarak💝 to all of U
          """)
st.write("What is Your name????")
name = st.text_input("Enter your name: ")

agree = st.checkbox("Agree")
if agree:
    st.write("Great!😀")

if st.button("Confrim"):
    st.write(f"Welcome Miss/Sir {name} to Arsh Streamlit🥳")

st.title("Counter😶‍🌫️")
st.header("welcome to Counter")
if "count" not in st.session_state:
    # st.session_state["count"] = 0
    st.session_state.count = 0

count = 0
st.header(st.session_state.count)

col1, col2 = st.columns(2)
print("count>>>",st.session_state.count)
with col1: 
    if st.button("increment"):
        st.session_state.count = st.session_state.count + 1

with col2:
    if st.button("decrement"):
        st.session_state.count = st.session_state.count - 1

st.title("Arsh GitHub")
st.write("U want to open Arsh's GitHub")
if st.button("Yes"):
    st.write("https://github.com/ArshAliAzam")
elif st.button("No"):
    st.write("Thanks for visiting🥰")

if st.camera_input("Camra"):
    st.write("U are SO Beautifull🥰")


st.title("Games🎮")
st.header("🕹️Tic Tac Toe")

# Initialize board
if 'board' not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i*3 + j
        if cols[j].button(st.session_state.board[idx] or " ", key=idx):
            if st.session_state.board[idx] == "":
                st.session_state.board[idx] = st.session_state.turn
                winner = check_winner(st.session_state.board)
                if winner:
                    st.success(f"{winner} wins!" if winner != "Draw" else "It's a draw!")
                else:
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

st.button("Reset Game", on_click=reset_game)

st.title("Roll Dice🎲")
if st.button("Roll Dice"):
    st.write(f"You rolled: {random.randint(1, 10)}")

from streamlit_drawable_canvas import st_canvas
import streamlit as st

st.title("🎨 Drawing Canvas")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=5,
    background_color="#eee",
    height=300,
    drawing_mode="freedraw",
)

if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)


if st.button("yes"):
    st.success("Welldone! Thanks Foe Visting🥳🥳")
    st.balloons()
    st.snow()
elif st.button("no"):
    st.write("Ok Thanks bye")
    





