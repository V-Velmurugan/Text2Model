from llama_cpp import Llama
import os

# Path to your DeepSeek GGUF model
MODEL_PATH = os.path.join("model", "deepseek-llm-7b-chat.Q4_K_M.gguf")

llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=8,verbose=False)

def Prompt_extract(user_input: str) -> str:
    """
    Extract minimal structured keywords from user input without expansion.
    """
    system_prompt = (
        "You are a visual keyword extractor for image generation.\n"
        "Your ONLY task is to copy all key visual elements from the user prompt.\n"
        "- Do NOT add mood, color, or setting unless they are explicitly mentioned.\n"
        "- DO NOT be creative or expand anything.\n"
        "- JUST return a cleaned-up version of the prompt as-is.\n\n"
        "Examples:\n"
        "Prompt: a laptop on a desk → Output: laptop on a desk\n"
        "Prompt: sadness → Output: human showing sadness\n\n"
        "Prompt:"
    )

    full_prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{user_input}\n<|assistant|>"

    response = llm(full_prompt, stop=["<|user|>", "<|system|>"], temperature=0.2, max_tokens=100)

    return response["choices"][0]["text"].strip()