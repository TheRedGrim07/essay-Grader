# AI Essay Grader 🤖

This project is a web-based application that uses a fine-tuned Transformer model to automatically grade essays and provide grammatical feedback. Users can paste their text into a simple interface and receive a score from 0 to 100, along with suggestions for improvement.

## ✨ Features

-   **AI-Powered Scoring:** Utilizes a DistilBERT model fine-tuned on the ASAP-AES dataset to predict essay scores.
-   **Automated Grammar Feedback:** Integrates LanguageTool to provide real-time suggestions for grammatical errors.
-   **Simple Web Interface:** A clean and straightforward frontend built with Flask, HTML, and JavaScript for ease of use.
-   **Scaled Scoring:** Converts the model's raw output into an intuitive 0-100 score.



## 🛠️ Tech Stack

-   **Backend:** Python, Flask
-   **Machine Learning:** PyTorch, Hugging Face Transformers
-   **Grammar Engine:** `language-tool-python` (using a local LanguageTool v6.3 server)
-   **Frontend:** HTML, CSS, JavaScript

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   Python 3.8+
-   Java 8+ (required by LanguageTool)
-   Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the venv
    python -m venv venv

    # Activate it (Windows)
    .\venv\Scripts\activate

    # Activate it (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download and set up the LanguageTool server:**
    -   Download LanguageTool v6.3 from this link: [LanguageTool-6.3.zip](https://www.languagetool.org/download/LanguageTool-6.3.zip)
    -   Create a folder named `lt` in the main project directory.
    -   Unzip the download and move the inner `LanguageTool-6.3` folder into the `lt` folder. Your final path should look like: `lt/LanguageTool-6.3/languagetool-server.jar`.

### Running the Application

1.  With your virtual environment active, run the Flask application using this command:
    ```bash
    python -m flask run
    ```
2.  Open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

## 📂 Project Structure

├── my_essay_grader_model/  # Stores the fine-tuned Transformer model
├── lt/                     # Stores the manual LanguageTool server
│   └── LanguageTool-6.3/
├── templates/
│   └── index.html          # Frontend HTML file
├── app.py                  # Main Flask application logic
├── train_model.py          # Script for training the AI model
├── requirements.txt        # Python dependencies
└── README.md               # You are here!


## 📈 Future Improvements

-   Train a more powerful model (like BERT or RoBERTa) on the complete dataset for higher accuracy.
-   Implement scoring on multiple criteria (e.g., structure, vocabulary, clarity).
-   Use a generative AI model to provide more specific, context-aware feedback instead 
