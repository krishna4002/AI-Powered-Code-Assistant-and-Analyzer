# 🤖 AI-Powered Code Assistant & Analyzer

This project is an all-in-one *intelligent programming assistant* built using open-source tools and models. It allows anyone — from beginners to developers — to easily:
- **Generate code**
- **Fix bugs**
- **Explain existing code**
- **Analyze uploaded programs**

All this is done interactively using a simple *Streamlit web interface* powered by an advanced AI model hosted on *OpenRouter*.

---

## Project Structure

```
├── app.py                    # Streamlit frontend
├── connect_with_llm.py      # Backend API calls to OpenRouter
├── requirements.txt         # Python dependencies
├── .env                     # Your API key (not committed)
└── README.md                # This file
```

---

## What Can This Do?

### 1. Chat Code Assistant
You can talk to the AI just like you would with ChatGPT or Copilot and say things like:
- “Write Python code for a calculator”
- “Fix this C++ loop error”
- “Explain what this Java method does”

It responds with actual working code examples in your selected language.

---

### 2. Code File Analyzer
You can upload your existing .py, .js, .cpp, or .java code file and the app will:
- **Explain the code** in human-readable steps
- **Find bugs**
- **Suggest refactoring**
- **Add meaningful comments**

All without needing to write any prompt manually!

---

## Why This Is Useful

- No need to Google “how to fix bug X”
- Makes learning code easier by generating clean, commented examples
- Helps you understand someone else's code
- Works both with text prompts and full files

Whether you're learning programming, debugging an assignment, or exploring codebases at work — this assistant is your smart companion.

---

## Technologies Used

| Tool            | Purpose                                     |
|------------------|----------------------------------------------|
| Streamlit      | For building the interactive UI              |
| OpenRouter     | To access free open-source large language models (LLMs) |
| olympiccoder-32b | The open-source AI model used to generate code |
| .env + requests | Secure communication with the OpenRouter API |

---

## How to Set It Up and Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/AI-Powered-Code-Assistant-and-Analyzer.git
   cd AI-Powered-Code-Assistant-and-Analyzer
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\\Scripts\\activate on Windows
   ```

3. **Install required libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your API Key from OpenRouter.ai**

   - Sign up at [https://openrouter.ai](https://openrouter.ai)
   - Go to your settings → API key
   - Create a `.env` file and paste:
     ```
     OPENROUTER_API_KEY=your_key_here
     ```

5. **Run the assistant**
   ```bash
   streamlit run app.py
   ```

Done! The assistant will open in your browser.

---

## Examples to Try

### Chat Prompt Examples
Try typing the following in the chat:
- Generate a Python function to find prime numbers
- Explain this JavaScript code with async/await
- Fix this code that crashes when the input is zero

### File Analysis Examples
1. Upload a .py or .cpp file
2. Select one of the analysis options (e.g., "Add comments")
3. The assistant will return an updated explanation or fixed version

---

## Environment Variable

| Variable             | Description                             |
|----------------------|-----------------------------------------|
| OPENROUTER_API_KEY | Your API key from [openrouter.ai](https://openrouter.ai) |

---

## About the Project

This project was designed to help anyone interact with programming knowledge *without needing complex tools or deep experience. Whether you're a student, hobbyist, or developer, it makes AI code generation and understanding **easy and accessible.*

---
