from todolistfuncs import write_todos, get_todos
import streamlit as st

todos = get_todos()

def add_todo():
    todo = st.session_state['user_input'] + '\n'
    todos.append(todo)
    write_todos(todos)
    st.session_state['user_input'] = ""

def complete_todo():
    for i , todo in enumerate(todos):
        if st.session_state[str(i)] == True:
            todos.pop(i)
            st.session_state[str(i)] = False
    write_todos(todos)
    

st.set_page_config(
    page_title="Wael's Todo App",   # <-- this is the tab name
    page_icon="✅"              # optional, the tab icon
)

            

st.title("Todo App")

for i,todo in enumerate(todos):
    st.checkbox(todo.strip('\n'),
                key=i,
                on_change=complete_todo,
                value=False)


st.text_input(label="",
              placeholder="add a todo",
              on_change=add_todo,
              key='user_input')
