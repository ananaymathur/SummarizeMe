# SummarizeMe App

The SummarizeMe App is an interactive desktop application built using Python and `tkinter` that provides users with the ability to summarize Medium articles, web articles from URLs, and custom text input. Utilizing the SpaCy NLP library for extractive summarization, the app helps users quickly digest large amounts of text by highlighting the most important information.

## Features

- **Medium Article Summarization**: Browse and summarize a curated list of Medium articles directly within the app. Users can read the summary or expand to view the full content.
- **URL Article Summarization**: Input any web article URL to generate a concise summary. The app fetches the article content, summarizes it, and displays the original text alongside the summary.
- **Custom Text Summarization**: Input any text directly into the app to receive a summarized version, allowing for quick analysis of reports, essays, or other large text blocks.
- **User-Friendly Interface**: The application provides an intuitive graphical interface with easy navigation, ensuring a smooth user experience.

## Project Structure

```plaintext
summarizer-app/
│
├── gui.py                # Main GUI script for the application
├── summarizer.py         # Core summarization logic using SpaCy
├── requirements.txt      # Required dependencies for the project
├── articles.csv          # Kaggle dataset of Medium articles in .csv format
└── README.md             # Project documentation
```

## Setup and Installation

### Prerequisites

Ensure you have Python 3.8 or higher installed. It is recommended to use a virtual environment for managing dependencies.

### Setting Up the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ananaymathur/SummarizeMe.git
    cd SummarizeMe
    ```

2. **Create a Virtual Environment (Optional but recommended):**

    ```bash
    python -m venv myenv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:

        ```bash
        .\myenv\Scripts\activate
        ```

    - On Mac:

        ```bash
        source myenv/bin/activate
        ```

4. **Install Required Packages using `requirements.txt`:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Download the SpaCy English Language Model:**

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Using the Application

To start the application, run the `gui.py` file:

```bash
python gui.py
```

Upon launching, the main menu will display three options:

1. **Open List of Medium Articles:**
    - Browse and select articles to summarize directly from a predefined list of Medium articles.

2. **Enter URL of an Article:**
    - Input the URL of any web article, and the app will fetch, summarize, and display the content.

3. **Enter Custom Text:**
    - Input custom text to receive a summarized version of the entered content.

## Application Components

### `summarizer.py`

- This script contains the core summarization functionality using SpaCy.
- The summarizer analyzes the input text, calculates word frequencies, scores sentences, and selects the top sentences to form the summary.

### `gui.py`

- Implements the graphical user interface using `tkinter`.
- Contains classes for different application windows and functionalities:
    - **MainMenu**: The main navigation menu of the app.
    - **ListOfArticles**: Handles displaying and summarizing Medium articles.
    - **URLofArticle**: Allows users to input URLs and summarize the fetched content.
    - **CustomText**: Enables users to input and summarize custom text.

## Completion and Achievements

- Successfully developed a user-friendly interface integrating Medium article summarization, URL input summarization, and custom text summarization.
- Implemented efficient data cleaning and text extraction techniques using SpaCy.
- Enhanced the app with additional features beyond the initial scope, including URL-based summarization and a flexible custom text summarizer.
- Validated summarization performance on various text inputs, optimizing for speed and accuracy.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Your Name**  
Email: [ananaymathur@gmail.com](mailto:ananaymathur@gmail.com)  

## Acknowledgments

- [SpaCy](https://spacy.io/) for natural language processing capabilities.
- [Python](https://www.python.org/) for providing a flexible programming environment.
- Libraries such as `tkinter` and `newspaper3k` for enhancing the application's user interaction and web content extraction capabilities.


