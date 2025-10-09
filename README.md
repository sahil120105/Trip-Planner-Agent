uv --version

uv init Trip-Planner-Agent
cd Trip-Planner-Agent

uv python list
uv venv venv --python cpython-3.12.8-windows-x86_64-none
venv\Scripts\activate
uv pip list
uv pip install langchain
