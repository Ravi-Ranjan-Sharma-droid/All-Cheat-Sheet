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
    {"role": "system", "content": "You're a helpful tutor"},
    {"role": "user", "content": "Explain Newton's third law"}
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
