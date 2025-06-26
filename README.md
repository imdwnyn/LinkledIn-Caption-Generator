# 🔗 LinkedIn Project Caption Generator

A sleek, GenAI-powered Streamlit app that crafts captivating LinkedIn captions for your technical projects using **LLaMA3-70B** via **GroqCloud** and **LangChain**.

> ✨ Stop staring at a blank text box. Let AI write your next project caption.

## 🚀 Features
- 🔥 Uses LLaMA3-70B from Groq — ultra-fast and high-quality generation
- 🧠 Built with LangChain for composable chains
- 📋 One-click caption generation and copy
- ✨ Emojis, hashtags, and multiple tone styles
- 💾 Local session state: generate + regenerate smoothly
- 🧼 Clean and responsive Streamlit UI

## 🧱 Tech Stack
- [Streamlit](https://streamlit.io/) — UI
- [LangChain](https://www.langchain.com/) — chaining LLM + prompt
- [GroqCloud](https://console.groq.com/) — blazing-fast LLaMA3 inference
- Python (`.env`, `os`, `dotenv`) — config and env management

## 📁 Folder Structure
```
linkedin-caption-generator/
├── app.py              # Streamlit frontend
├── llama_chain.py      # LangChain + Groq model logic
├── .env                # Your Groq API key (not committed)
├── requirements.txt    # Project dependencies
└── README.md           # Project overview and setup
```

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/linkedin-caption-generator.git
cd linkedin-caption-generator
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# Or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API Key
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=gsk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## ▶️ Run the App
```bash
streamlit run app.py
```

## 🧪 Example Inputs
| Field         | Example                                                                 |
|---------------|-------------------------------------------------------------------------|
| Title         | LinkedIn Caption Generator                                              |
| Description   | A web app that crafts AI-powered LinkedIn captions using LLaMA3 & Groq |
| Tech Stack    | Streamlit, LangChain, LLaMA3, GroqCloud                                 |
| Outcome       | Automated content creation with a professional touch                    |
| Reflection    | Learned how to combine GenAI tools into a production-level project      |
| Tone          | Enthusiastic                                                            |

## 📝 Output Example
```
🚀 Introducing the LinkedIn Project Caption Generator! 💻✨
This game-changing tool uses cutting-edge GenAI technology to craft captivating captions for your technical projects, saving you time and elevating your personal brand. 📈

Built using Streamlit, LangChain, and LLaMA3 via GroqCloud, it makes your project updates shine on LinkedIn. 🌐

Try it now and take your content to the next level! 💥

#GenAI #LinkedInTips #Innovation #ContentCreation #LLM
```

## ✅ Todo / Enhancements
- [ ] Add real clipboard copy support (e.g. via `pyperclip`)
- [ ] Support custom hashtag presets
- [ ] Store caption history
- [ ] Optional RAG context injection (ChromaDB)

## 🙋‍♂️ Why I Built This
As a developer, I’ve often struggled to describe my projects in an engaging way. This app helps solve that, turning raw project inputs into polished LinkedIn content. Built using only open-source + free tools, it’s fast, lightweight, and extendable.

## 📄 License
MIT License © Dwinayan
