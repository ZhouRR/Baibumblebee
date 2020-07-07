# Baibumblebee
Project Baibumblebee
environment:
1. install git
2. install conda

&. conda activate Baibumblebee
&. git clone https://github.com/ZhouRR/Baibumblebee

run: uvicorn route:app --reload --host 0.0.0.0 --port 8000 &

&. conda deactivate