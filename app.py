import streamlit as st
import random
import time

WIDTH, HEIGHT = 20, 10
EMPTY = " "
SNAKE_CHAR = "🟩"
STAR_CHAR = "⭐"

# 초기화
if "snake" not in st.session_state:
    st.session_state.snake = [(WIDTH // 2, HEIGHT // 2)]
    st.session_state.direction = (1, 0)
    st.session_state.star = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    st.session_state.score = 0
    st.session_state.game_over = False

def move_snake():
    head_x, head_y = st.session_state.snake[0]
    dx, dy = st.session_state.direction
    new_head = (head_x + dx, head_y + dy)

    # 충돌 체크
    if (
        not (0 <= new_head[0] < WIDTH)
        or not (0 <= new_head[1] < HEIGHT)
        or new_head in st.session_state.snake
    ):
        st.session_state.game_over = True
        return

    st.session_state.snake.insert(0, new_head)

    # 별 먹기
    if new_head == st.session_state.star:
        st.session_state.score += 1
        while True:
            st.session_state.star = (
                random.randint(0, WIDTH - 1),
                random.randint(0, HEIGHT - 1),
            )
            if st.session_state.star not in st.session_state.snake:
                break
    else:
        st.session_state.snake.pop()

def render_board():
    board = ""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pos = (x, y)
            if pos == st.session_state.star:
                board += STAR_CHAR
            elif pos in st.session_state.snake:
                board += SNAKE_CHAR
            else:
                board += EMPTY
        board += "\n"
    return board

st.title("🐍 Snake Game with Streamlit")
st.markdown("Use the buttons below to control the snake.")

# 방향 조작 버튼
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️ Left"):
        if st.session_state.direction != (1, 0):
            st.session_state.direction = (-1, 0)
with col2:
    if st.button("⬆️ Up"):
        if st.session_state.direction != (0, 1):
            st.session_state.direction = (0, -1)
    if st.button("⬇️ Down"):
        if st.session_state.direction != (0, -1):
            st.session_state.direction = (0, 1)
with col3:
    if st.button("➡️ Right"):
        if st.session_state.direction != (-1, 0):
            st.session_state.direction = (1, 0)

# 게임 진행
if not st.session_state.game_over:
    move_snake()
    st.text(render_board())
    st.write(f"Score: {st.session_state.score}")
    time.sleep(0.2)
    st.experimental_rerun()
else:
    st.error("💀 Game Over!")
    st.write(f"Final Score: {st.session_state.score}")
    if st.button("Restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
