# Ollama cheat sheet

## 1. What is Ollama?

**Ollama** is a command-line tool that allows you to **Large Language Models (LLMs) locally.** Interact with team via CLI, API, or apps, and builds customized models with simple configurations.

- **Private:** Runs offline.
- **Fast:** Supports quantized models.
- **Customizable:** Support _Modelfile_ for modifying base models.
- **API-ready:** Built-in local REST API for integration.

---

## 2. System Requirements

### Minimum

- 8 GB RAM (basics models like TineLlama)
- 2-core CPU

### Recommended

- 16+ GB RAM
- Modern GPU (for fast generation, optional)
- 30+ GB disk (some models are large)

---

## 3. Installation

### macOS/Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Windows

- [Click me for download](https://ollama.com/download)
- run in background as a service

### Optional (Docker)

```bash
docker run --gpus all -p 11434: 11434 ollama/ollama
```

---

## 4. Core CLI Commands

| Commands                            | Descriptions                              |
| ----------------------------------- | ----------------------------------------- |
| `ollama run <model-name>`           | Start a chat session                      |
| `ollama list`                       | Show all installed models                 |
| `ollama pull <model-name>`          | Download a models from the Ollama library |
| `ollama create <name> -f Modelfile` | Build a custom model                      |
| `ollama serve`                      | Run Ollama as a background daemon         |

### Example:

```bash
ollama run llama3
```

---

## 5. Running Prompts

### Interactive Prompts

```bash
ollama run mistral
```

You'll get an interactive shell where you can type prompts.

### One-shot Prompting

```bash
ollama run llama3 --prompt "summarize this text ..."
```

### Streaming Output

```bash
ollama run mistral --stream --prompt "What is linear accelerator I'm 12..."
```
---


## 6. Parameter Reference

| Parameter        | Type   | Description                                    |
| ---------------- | ------ | ---------------------------------------------- |
| `temperature`    | Float  | Creativity (0.0 = deterministic, 1.0 = random) |
| `top_k`          | Int    | Limit choices to top K tokens                  |
| `top_p`          | Float  | Nucleus sampling (0.9 = top 90% prob.)         |
| `num_predict`    | Int    | Max tokens to predict                          |
| `stop`           | Array  | Stop sequences                                 |
| `repeat_penalty` | Float  | Penalize repetition                            |
| `seed`           | Int    | Reproducible generations                       |
| `system`         | String | System prompt for behavior definition          |

### Example

```bash
ollama run mistral --temperature 0.3 --top_k 50 --stop "<END>"
```

## 7. Modelfile (custom model)

A Modelfile lets create personalized models.

### Basic Template

```Dockerfile
FROM llama3
SYSTEM "You are a math tutor."
PARAMETER temperature 0.2
```

### Add File to the Model

```Dockerfile
FROM mistral
ADAPTER ./mydata.txt
```

### Build it

```bash
ollama create tutor -ai -f Modelfile
```

## 7. API Usage (RESTful)

Default server run at http://localhost:11434

### Generate (Stateless)

```bash
curl http://localhost:11434/api/generate -d '{
"model": "llama3",
"prompt": "Write a short poem"
}'
```

### Chat (Stateful)

```bash
curl http://localhost:11434/api/generate -d '{
"model": "llama3",
"message": [
    {"role": "system", "content": "You are a helpful tutor"},
    {"role": "user", "content": "Explain Newtons third law"}
  ]
}'
```

### API Endpoint

| Endpoint      | Description           |
| ------------- | --------------------- |
| /api/generate | Stateless generation  |
| /api/chat     | stateful dialogue     |
| /api/tags     | List installed models |
| /api/pull     | Pull a model          |
| /api/delete   | Delete model          |

## 9. Advance Uses

### Run in background

```bash
ollama serve
```

### Run on Custom Port

```bash
OLLAMA_HOST=127.0.0.1:11435 ollama serve
```

### Set Model Directory

```bash
OLLAMA_HOST=/path/to/models
```

### Export Model Configuration

```bash
ollama show llama3
```
## 10. Model Types & Size

| Model        | Use Case                  | Size      | Strength       |
|--------------|----------------------------|-----------|----------------|
| `llama3`     | General-purpose            | 4–8 GB    | Balanced       |
| `mistral`    | Chat / reasoning           | 4 GB      | Very fast      |
| `gemma`      | Science / logic            | 3.8 GB    | Clean output   |
| `phi`        | Code-heavy / low RAM       | 2–4 GB    | Lightweight    |
| `codellama`  | Code generation            | 6–12 GB   | Dev-friendly   |
| `tinyllama`  | Minimal system             | ~1 GB     | Low-resource   |

Quantized model variants include:

- `q4_0`, `q4_K_M`, `q8_0` *(smaller to larger sizes)*


## 11. Frontend & Tools

| Tool                    | Description                                 |
|-------------------------|---------------------------------------------|
| Open WebUI              | Web interface for Ollama                    |
| LM Studio               | GUI for model management                    |
| Faraday.dev             | Beautiful local UI                          |
| LangChain / LlamaIndex  | AI framework integration                    |
| Text Generation WebUI   | Multi-backend GUI frontend                  |
| Oobabooga               | Multi-model runner (supports Ollama)        |

### 12. Use Cases

- **Offline chatbots**
- **Custom agents** (coding assistant, tutor, etc.)
- **Private data analysis**
- **Local GPT-4-like applications**
- **Voice-to-AI via Whisper + Ollama**
- **Integrate with automation tools** (like Node-RED, Zapier, etc.)

---

### 13. Optimization Tips

- Use `repeat_penalty` ~1.2 to avoid repetition.
- Keep `temperature` 0.2–0.6 for coherent outputs.
- Use smaller quantized models (`q4_0`) if low on RAM.
- Enable **GPU acceleration** if possible (Ollama uses Metal on macOS).
- Try **Mixtral** for ensemble responses (mixture of experts).
