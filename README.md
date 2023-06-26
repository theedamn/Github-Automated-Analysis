# Github Automated Repo Analysis

This project is a Python application that leverages the Github API to automate the analysis of repositories based on a user's Github URL. It performs tasks such as web scraping, data cloning, data cleaning, and analysis of the repositories to find cyclomatic complexity of the repositories adn it will return the most complex open.

## Features

- Web scraping of repositories from a user's Github URL.
- Cloning of repositories locally for further analysis.
- Cleaning of repository data by removing unnecessary files.
- Analysis of the repositories using code complexity metrics.
- Python analysis: Identifies the most complex repository based on code complexity scores.
- GPT Evaluation: Generates a response using GPT (Generative Pre-trained Transformer) based on the analysis results.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the application using the command `python main.py`.
4. Access the application via the provided URL in the console.

## Usage

1. Enter the Github URL of the user you want to analyze.
2. Select the desired option: "Python Analysis" or "GPT Evaluation".
3. Click the "Submit" button to start the automated analysis process.
4. Wait for the analysis to complete.
5. View the generated response in the text area.

## Dependencies

- streamlit: 0.87.0 or higher
- requests: 2.26.0 or higher
- bs4: 0.0.1 or higher
- nbconvert: 6.2.0 or higher
- langchain
- gpt4all
- huggingface_hub
- huggingface
- radon
- 

## To access the project in cloud

[Hugging Space Server 1](https://huggingface.co/spaces/halfdevil/Github-Automated-Analysis)

[hugging Space Server 2](https://huggingface.co/spaces/halfdevil/d3modocker)

## Video Demonstration

[Youtube](https://youtu.be/CZ1aOlJTJmo)


## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

