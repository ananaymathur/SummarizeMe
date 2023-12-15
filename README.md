# CS410_finalproject

## Proposal

Team member - Ananay Mathur

Team captain - Ananay Mathur

I plan on building a text summarization model to help summarize lengthy Medium articles. I will be making an interface where the user can select which Medium article they want to be summarized. For this project, I will be using a Kaggle dataset of Medium articles and will summarize them on demand using my text summarization model. I think this is a fascinating use case as these articles can get pretty lengthy sometimes and getting a gist of what the article says can help readers decide if they want to commit to reading the entire thing. This can be extended in the future to directly get articles from Medium, instead of relying on a dataset of articles. I will maily be utilizing SpaCy Python library to do the text summarization. The output should be a short summarization of the article and I will compare the contents of the two and see if the summarization is valid. 

I plan on using Python for this project.

Main tasks and time cost:

1. Cleaning and extracting data from the dataset - 6 hours
2. Building an user-friendly interface - 5 hours
3. Building a summarizer - 6 hours
4. Testing the results - 3 hours

Total time - 20 hours

## Progress Report

Tasks Completed:

1. Cleaning and extracting data from the dataset
2. Building an user-friendly interface

Tasks to be completed:

1. Building a summarizer
2. Testing the results

Challenges currently facing:

1. Building an effective summarizer

## Final documentation

### Setting up the project

1. Create a Virtual Environment (Optional but recommended):

   ```
   python -m venv myenv
   ```

2. Activate the Virtual Environment:

   On Windows:
   
   ```
   .\myenv\Scripts\activate
   ```

   On Mac:

   ```
   source myenv/bin/activate
   ```
3. Using requirements.txt to install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Download spaCy English Language Model (en_core_web_sm):

   ```
   python -m spacy download en_core_web_sm
   ```

### Using the application

To use the application, run the gui.py file. This will open a user interface through which all the application features can be used. The application opens on a main menu which has 3 buttons leading to the features:

1. Medium Articles:

   This was the original feature planned. This feature displays a list of titles of Medium articles. Clicking on any of these article titles opens a new window where you can read the summary of that article. There is also a button to show the full article if you want to read the whole thing. Closing this summary window takes you back to the list of Medium articles and there is a button to take you back to the main menu.

2. Article link:

   This is a new feature that I added to the project. This feature allows you to enter the URL of a web article into a text box, clicking submit then opens a new window which displays the summary of the article and also has an option to show the entire article in case you want to look at it too. Closing the summary window brings you back to the link summarizer page where you can paste other links or click the button to return to the main menu.

3. Custom summarize:

   This is a new feature I added to the project. This feature allows you to input any text into the text box, clicking the submit button then summarize the text entered. In the summary window you can see the summarized version as well as the original text entered. Closing the summary window brings you back to the custom summarizer page where you can enter other text or click the button to return to the main menu.






