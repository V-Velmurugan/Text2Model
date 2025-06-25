# Text2Model

Text2Model is a web application that allows users to enter natural language prompts and receive AI-generated 3d model. The system stores the prompt history and extracted LLM data using Redis and visualizes the result in a clean chatbot-style interface. It also includes functionality to reconstruct a 3D mesh from the generated image using depth estimation and Open3D.

---

## Features

- Natural language prompt input
- AI-generated image using Hugging Face Inference API (`stabilityai/stable-diffusion-xl-base-1.0`)
- Chat-style UI with full conversation history stored in Redis
- Prompt extraction via custom LLM logic
- Direct image download from UI
- Image-to-3D point cloud + mesh reconstruction using DepthCrafter + Open3D

---

## Tech Stack

| Category      | Technologies Used                           |
|---------------|---------------------------------------------|
| Language      | Python, JavaScript, HTML, CSS               |
| Backend       | FastAPI                                     |
| Frontend      | Vanilla JS, HTML, CSS                       |
| Database      | Redis (for storing prompt and responses)    |
| AI Tools      | HuggingFace Inference API, Transformers     |
| 3D Engine     | Open3D, DepthCrafter (GLPN model)           |

---

## Project Structure

prompt-to-3d/
├── app/
│ ├── main.py
│ └── LLM.py
├── static/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── model/
├── requirements.txt
├── .gitignore
└── README.md

---

## How to Run

### 1. Clone the repo

git clone https://github.com/your-username/prompt-to-3d.git
cd prompt-to-3d


2. Create and activate a virtual environment

python -m venv .venv
.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Set your HuggingFace API key

HF_TOKEN=...

5. Download the model and place inside model folder

https://huggingface.co/TheBloke/deepseek-llm-7B-chat-GGUF/resolve/main/deepseek-llm-7b-chat.Q4_K_M.gguf?download=true

5. Start Redis server (must be installed)

redis-server

6. Run the FastAPI server

uvicorn app.main:app --reload
Visit http://localhost:8000 in your browser.


# Outcome

Learned to integrate LLMs and prompt engineering with web apps.

Built a complete AI image and 3D mesh generation pipeline.

Applied Redis for persistent chat history and fast in-memory storage.

Gained experience with FastAPI, frontend/backend integration, and Open3D.


License
This project is licensed under the MIT License.
