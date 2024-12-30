import streamlit.web.bootstrap as bootstrap
from bible_app import create_app

if __name__ == "__main__":
    create_app()
    bootstrap.run(
        main_script_path="main.py",
        command_line=[],
        args=[],
        flag_options={},
    )