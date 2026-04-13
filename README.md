# 🔬 Multi-Agent AI Research System with LangChain

A sophisticated multi-agent AI system that collaborates to conduct in-depth research on any topic. Four specialized AI agents work together to search, scrape, analyze, and critique information to produce polished research reports.

## 🎯 Project Overview

This system leverages **LangChain** to orchestrate multiple AI agents that perform distinct roles in a research pipeline:

1. **Search Agent** 🔍 - Finds recent, reliable information via web search
2. **Reader Agent** 📄 - Scrapes and extracts deep content from relevant URLs
3. **Writer Agent** ✍️ - Drafts comprehensive, structured research reports
4. **Critic Agent** 🧐 - Reviews reports and provides constructive feedback

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    User Input (Research Topic)                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
          ┌──────────────────────────────────┐
          │   1️⃣  SEARCH AGENT 🔍            │
          │   ├─ Tavily Search Tool          │
          │   ├─ Find recent information     │
          │   └─ Return URLs + snippets      │
          └──────────────┬───────────────────┘
                         │
                         ▼
          ┌──────────────────────────────────┐
          │   2️⃣  READER AGENT 📄            │
          │   ├─ Web Scraping Tool           │
          │   ├─ Extract deep content        │
          │   └─ Parse relevant information  │
          └──────────────┬───────────────────┘
                         │
                         ▼
          ┌──────────────────────────────────┐
          │   3️⃣  WRITER CHAIN ✍️             │
          │   ├─ Combine search + scraped    │
          │   ├─ Structure research report   │
          │   └─ Format with markdown        │
          └──────────────┬───────────────────┘
                         │
                         ▼
          ┌──────────────────────────────────┐
          │   4️⃣  CRITIC CHAIN 🧐            │
          │   ├─ Evaluate report quality     │
          │   ├─ Provide score & feedback    │
          │   └─ Suggest improvements        │
          └──────────────┬───────────────────┘
                         │
                         ▼
          ┌──────────────────────────────────┐
          │    📋 Final Research Report      │
          │    ├─ Structured markdown        │
          │    ├─ Critic feedback            │
          │    └─ Download as .md file       │
          └──────────────────────────────────┘
```

## 🚀 Features

- ✅ **Multi-Agent Architecture** - Specialized agents for different tasks
- ✅ **Asynchronous Processing** - Efficient sequential pipeline
- ✅ **Web Search Integration** - Real-time information retrieval via Tavily
- ✅ **Web Scraping** - Extract detailed content from URLs
- ✅ **Streamlit UI** - Beautiful, interactive web interface
- ✅ **CLI Pipeline** - Command-line interface for batch processing
- ✅ **Local LLM Support** - Ollama integration (no API costs)
- ✅ **Report Generation** - Markdown-formatted downloadable reports
- ✅ **Critic Feedback** - Automatic quality evaluation with scores

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM Framework** | LangChain + LangGraph |
| **Local LLM** | Ollama (Mistral) |
| **Web Search** | Tavily API |
| **Web Scraping** | BeautifulSoup4 |
| **Web UI** | Streamlit |
| **HTTP Client** | Aiohttp |
| **Data Processing** | Pandas |

## 📋 Requirements

- Python 3.8+
- Ollama (for local LLM)
- Tavily API key (for web search)

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/IshaNayal/Multi-Agent-AI-Research-System-with-LangChain.git
cd Multi-Agent-AI-Research-System-with-LangChain
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama
Download from [ollama.ai](https://ollama.ai)

### 5. Pull LLM Model
```bash
ollama pull mistral
ollama serve  # Start Ollama server
```

### 6. Configure Environment
Create a `.env` file:
```
TAVILY_API_KEY=your_tavily_api_key_here
OPENAI_API_KEY=your_openai_key_here  # Optional, uses Ollama if not set
```

## 🎮 Usage

### Web UI (Recommended)
```bash
streamlit run app.py
```
Then open http://localhost:8501

### CLI Pipeline
```bash
python pipeline.py
# Enter research topic when prompted
```

## 📁 Project Structure

```
├── agents.py           # LLM agents configuration (Search, Reader, Writer, Critic)
├── tools.py            # Tavily search & web scraping tools
├── pipeline.py         # CLI-based research pipeline
├── app.py              # Streamlit web application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys)
├── debug_env.py        # Debugging script for environment
└── README.md           # This file
```

## 🔄 How It Works

### Step 1: Search Agent
- Accepts research topic
- Uses Tavily to search the web
- Returns top 3 relevant results with URLs and snippets

### Step 2: Reader Agent
- Receives search results
- Selects most relevant URL
- Scrapes content using BeautifulSoup
- Extracts and cleans text

### Step 3: Writer Agent
- Combines search results + scraped content
- Generates structured report with:
  - Introduction
  - Key Findings (3+ points)
  - Conclusion
  - Sources listed

### Step 4: Critic Agent
- Evaluates report quality
- Provides score (X/10)
- Lists strengths and areas for improvement
- Gives one-line verdict

## 📊 Example Output

**Input:** "Transformers Architecture"

**Output:**
```
Score: 8/10

Strengths:
- Comprehensive coverage of attention mechanisms
- Clear explanation of multi-head attention
- Well-sourced from recent papers

Areas to Improve:
- Add more implementation details
- Include complexity analysis

Verdict: 
Solid technical overview with good structure; needs deeper mathematical insights.
```

## 🔐 API Keys

### Tavily API
- Sign up: https://tavily.com/
- Get free tier for 1000 searches/month

### OpenAI API (Optional)
- Only needed if using GPT instead of Ollama
- Sign up: https://platform.openai.com/
- Check quota and billing

## ⚡ Performance Tips

- Uses `@st.cache_resource` for agent caching
- Incremental state updates (no full page reruns)
- Sequential processing optimized for reduce latency
- Ollama runs locally (no network delays for LLM)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push to GitHub
5. Open a pull request

## 📝 License

MIT License - Feel free to use this project for research and development

## 🎓 What You'll Learn

- Multi-agent systems with LangChain
- Building Streamlit applications
- Web scraping with BeautifulSoup
- LLM orchestration patterns
- State management in AI pipelines
- Production-ready Python development

## 🚀 Future Enhancements

- [ ] Add PDF report generation
- [ ] Support for images in reports
- [ ] Multi-language support
- [ ] Database for research history
- [ ] Team collaboration features
- [ ] API endpoint for REST integration
- [ ] Advanced filtering for search results
- [ ] Custom agent configurations

## 📞 Support

For issues, questions, or suggestions:
1. Open an GitHub issue
2. Check existing discussions
3. Review the documentation

---

**Made with ❤️ by the LangChain community**