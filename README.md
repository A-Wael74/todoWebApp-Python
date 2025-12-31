# Simple Streamlit Todo App 📝

A minimal **Todo web application** built with [Streamlit](https://streamlit.io/) while learning Python.

The app lets you:

- View your current todo list
- Add new todos from a text input
- Mark todos as complete using checkboxes
- Persist the list using a small helper module that reads/writes todos to a local file

---

## Features

- ✅ Clean, minimal UI powered by Streamlit
- ✅ Todos are loaded at startup from a helper function `get_todos()`
- ✅ New todos are added via an input field and saved with `write_todos()`
- ✅ Each todo appears as a checkbox; checking it removes it from the list
- ✅ State management using `st.session_state` so UI interactions feel responsive

---

## Tech Stack

- **Language:** Python 3
- **UI framework:** Streamlit
- **Persistence:** Simple file-based storage via `todolistfuncs.py` (functions `get_todos` / `write_todos`)

---

## Project Structure

An example project layout:

```text
.
├── web.py              # Main Streamlit app
├── todolistfuncs.py    # Helper functions: get_todos(), write_todos()
└── todos.txt           # (Optional) Text file used to store todos
