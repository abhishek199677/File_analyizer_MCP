conda create -n openai python=3.10 -y

conda activate openai

pip install -r requirements.txt

uv init .

uv add "mcp[cli]"

pip install mcp mcp[cli]

uv run mcp