# Echo

> **Offline AI Desktop Assistant**
>
> A privacy-first, modular AI assistant that runs locally using open-source models and tools.

---

## ✨ Overview

Echo is an offline AI desktop assistant built entirely in Python. It combines local speech recognition, natural language understanding, and local large language models to deliver a fast, private, and extensible AI experience.

Unlike traditional cloud-based assistants, Echo keeps your interactions on your own machine, making it ideal for users who value privacy, low latency, and complete control over their AI assistant.

Echo is designed with a modular architecture so that new skills, automation capabilities, memory systems, and AI models can be added without changing the core system.

---

## 🎯 Why Echo?

Most AI assistants today depend heavily on cloud services and internet connectivity.

Echo was built to explore a different approach.

### Core Principles

- 🔒 Privacy First
- 💻 Offline First
- ⚡ Fast Response Time
- 🧩 Modular Architecture
- 🚀 Easily Extendable
- 🛠️ Developer Friendly

The long-term goal is to build an intelligent desktop assistant capable of understanding natural language, remembering context, automating tasks, and interacting with the desktop—all while running locally.

---

## 🚀 Current Features

- 🎤 Offline Speech Recognition using Faster Whisper
- 🔊 Offline Text-to-Speech using Piper
- 🧠 Local LLM Integration using Ollama
- 🗣️ Natural Language Command Parsing
- 🔀 Context-Aware Skill Routing
- 📋 Session Management
- 🌐 Browser Search
- 🖥️ Application Launcher
- 📂 Modular Skill System
- ⚙️ Easily Expandable Architecture

---

## 🏗️ System Architecture

```text
                 User
                   │
                   ▼
        Speech Recognition
          (Faster Whisper)
                   │
                   ▼
             Command Parser
                   │
                   ▼
           Session Manager
                   │
                   ▼
             Skill Router
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 Applications   Browser     Future Skills
                   │
                   ▼
              Ollama (LLM)
                   │
                   ▼
             Piper Text-to-Speech
```

---

## 📂 Project Structure

```text
Echo/
│
├── assets/
│   ├── demo/
│   ├── logo/
│   └── screenshots/
│
├── core/
│   ├── brain.py
│   ├── commands.py
│   ├── memory.py
│   ├── parser.py
│   ├── router.py
│   ├── session.py
│   ├── stt.py
│   ├── tts.py
│   ├── utils.py
│   └── voice.py
│
├── data/
├── docs/
│   ├── architecture.md
│   ├── changelog.md
│   └── roadmap.md
│
├── logs/
├── models/
├── piper/
├── skills/
│   ├── applications.py
│   ├── browser.py
│   ├── coding.py
│   └── files.py
│
├── sounds/
├── tests/
│
├── config.py
├── main.py
├── version.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🛠️ Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Speech Recognition | Faster Whisper |
| Voice Activity Detection | Silero VAD |
| Text-to-Speech | Piper |
| Local LLM | Ollama (Qwen) |
| Version Control | Git & GitHub |

---

## ⚡ Getting Started

### Clone the repository

```bash
git clone https://github.com/Smit-Bhatkar/Echo.git

cd Echo
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Echo

```bash
python main.py
```

---

## 🎤 Example Commands

```text
Open YouTube

Search Python tutorials

Open VS Code

Open Calculator

Open Notepad

Search GitHub

Open LinkedIn
```

---

## 🧠 How Echo Works

1. User speaks a command.
2. Faster Whisper converts speech to text.
3. The Parser identifies the user's intent.
4. Session Manager remembers context.
5. Skill Router selects the appropriate module.
6. The selected skill performs the requested action.
7. Echo responds using Piper Text-to-Speech.

---

## 📈 Roadmap

### ✅ Completed

- Offline Speech Recognition
- Offline Text-to-Speech
- Local LLM Integration
- Intent Parser
- Skill Router
- Session Manager
- Context Awareness
- Professional Project Structure

### 🚧 In Progress

- Browser Automation
- Long-Term Memory
- Agent Workflows
- GUI
- Plugin System
- Vision Capabilities

---

## 🤝 Contributing

At the moment, Echo is a personal flagship project and contributions are not being accepted.

If you're interested in collaboration or have suggestions, feel free to open an issue or contact the author.

---

## 📜 License

This project is licensed under the **Echo AI Assistant License v1.0**.

The source code is provided for educational and personal learning purposes.

Commercial use, redistribution, and republishing are prohibited without written permission from the author.

See the `LICENSE` file for complete details.

---

## 👨‍💻 Author

**Smit Bhatkar**

Computer Engineering Student  
Specialization: AI/ML & Data Science

GitHub: https://github.com/Smit-Bhatkar

---

## ⭐ Future Vision

Echo is more than just a voice assistant.

The vision is to build a modular, offline AI platform capable of understanding natural language, remembering conversations, automating workflows, interacting with applications, and assisting users in their daily tasks—all while keeping privacy at the center of the experience.

This project represents an ongoing journey in AI engineering, software architecture, and intelligent automation.

---

> **"Build AI that works for you—not one that depends on the cloud."**
