# 🧠 AI Mental Health Assistant for Lebanon



> **Note:** This project was developed as a proof-of-concept during a 12-hour hackathon. Its purpose is to showcase the potential of AI in mental health assessment. It is not intended to be a substitute for professional medical or psychological advice, diagnosis, or treatment.

---

### 🌟 Project Overview

This project is an **AI-powered mental health assessment chatbot** designed to provide an accessible and private space for individuals to express their thoughts and feelings. Built during a fast-paced hackathon, the application leverages the power of **Llama 3**, released the very same week, combined with an agent-based architecture to conduct an interactive, voice-driven mental health assessment.

A key feature is its **localization to the Lebanese context**. The system was trained with insights from Lebanese psychiatrists and psychologists to better understand and address the specific nuances and cultural factors related to mental health in the region.

### 🚀 Key Features

* **Interactive Chatbot:** Engages users in a supportive and conversational dialogue to assess their mental state.
* **Voice & Text Input:** Users can communicate with the chatbot using either speech or text, offering a flexible and natural interaction experience.
* **Intelligent Agent System:** Utilizes a **CrewAI** framework to create specialized agents:
    * **Follow-Up Questioner:** An agent that analyzes user responses and generates targeted, insightful follow-up questions to gather deeper context.
    * **Mental Health Classifier:** An agent that assesses the user's overall responses and provides a supportive summary, along with relevant mental health resources in Lebanon if significant concerns are identified.
* **Real-time Assessment:** The system provides on-the-spot feedback, offering an immediate and private way for users to gain initial insights into their well-being.
* **Llama 3 Integration:** Implements the then-recently-released Llama 3 model to power the conversational logic and assessment capabilities.

---

### ⚙️ Technologies Used

* **Large Language Model:** Llama 3
* **AI Framework:** CrewAI
* **Speech-to-Text:** `speech_recognition`
* **Text-to-Speech:** `pyttsx3`
* **Python Libraries:** `langchain_community`, `os`, `sys`

---

### 🛠️ How it Works

The application operates in a conversational loop:

1.  **Greeting:** The chatbot greets the user and asks an initial question.
2.  **Input:** The user responds via voice, which is converted to text using the `speech_recognition` library.
3.  **Analysis (Agent 1):** The `Follow-Up Questioner` agent analyzes the user's response and generates a new, context-aware question.
4.  **Output (Agent 2):** The new question is converted to speech using `pyttsx3` and played back to the user.
5.  **Final Assessment:** After a series of questions, the `Mental Health Classifier` agent analyzes the entire conversation transcript and provides a final, supportive message. This message can also include suggestions for local Lebanese mental health NGOs if needed.

---

### 💻 Getting Started

This project requires a few dependencies and a specific setup.

#### Prerequisites

* Python 3.8+
* An API key from a provider that offers access to the Llama 3 model (e.g., Groq).

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[Your-Username]/[Your-Repo-Name].git
    cd [Your-Repo-Name]
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Note: You will need to create a `requirements.txt` file from the project's dependencies.)

3.  **Set up your API key:**
    Open `main.py` and replace the placeholder with your secret API key.
    ```python
    os.environ["OPENAI_API_KEY"] = 'YOUR_SECRET_API_KEY'
    ```

#### Running the Application

To start the mental health assistant, run the `main.py` file:
```bash
python main.py
