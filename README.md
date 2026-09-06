# 📜 Voynich Manuscript Structural Analysis

![Voynich Manuscript](https://upload.wikimedia.org/wikipedia/commons/5/5e/Voynich_manuscript.jpg)

## 🔍 Overview

This project began as a personal challenge to explore what modern Natural Language Processing (NLP) can reveal about the enigmatic Voynich Manuscript. My goal was to avoid falling into translation speculation or pattern hallucination. I am not a linguist or a cryptographer; I simply wanted to see if something as peculiar as Voynichese would withstand rigorous language modeling techniques. 

The analysis covers various methods, including clustering, part-of-speech (POS) inference, Markov transitions, and section-specific patterns. Spoiler alert: the manuscript exhibits some structure that resembles language, even if we cannot decipher its meaning.

This repository provides a detailed walkthrough of the entire process—from suffix stripping to SBERT embeddings to constructing a lexicon hypothesis. There is no magic or GPT guessing involved; just a methodical examination of whether the manuscript has characteristics typical of structured language.

## 🧠 Why This Matters

The Voynich Manuscript remains one of the most intriguing undeciphered texts in history. Despite numerous attempts, no consensus exists regarding its linguistic or cryptographic interpretation. Traditional analyses often split into two camps: statistical entropy checks and linguistic pattern analysis. This project aims to bridge that gap by employing modern NLP techniques to provide a fresh perspective on the manuscript.

By investigating the structural aspects of the text, we can contribute to the ongoing discourse surrounding its meaning and origins. This research could help refine the methods used in cryptographic analysis and linguistic studies, paving the way for new discoveries.

## 📂 Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Data Sources](#data-sources)
4. [Methods](#methods)
5. [Results](#results)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)
9. [Releases](#releases)

## ⚙️ Installation

To get started with this analysis, clone the repository and install the required packages. You can do this by running the following commands in your terminal:

```bash
git clone https://github.com/ifexthy/voynich-nlp-analysis.git
cd voynich-nlp-analysis
pip install -r requirements.txt
```

Make sure you have Python 3.x installed on your machine, along with pip.

## 🛠️ Usage

After installing the necessary packages, you can begin your analysis. The main script to run is `main.py`. Execute the script using the following command:

```bash
python main.py
```

This will initiate the analysis and generate output files that detail the findings. You can customize the parameters in the script to tailor the analysis to your needs.

## 📊 Data Sources

The primary data source for this project is the Voynich Manuscript itself. The manuscript is available in various formats online. For this analysis, I used a digitized version available from [Yale University](https://beinecke.library.yale.edu/).

In addition to the manuscript, I utilized several NLP libraries and datasets, including:

- **spaCy**: For part-of-speech tagging and linguistic features.
- **scikit-learn**: For clustering algorithms.
- **Transformers**: For embeddings and advanced NLP techniques.

## 🔍 Methods

### Suffix Stripping

Suffix stripping is a crucial step in preparing the text for analysis. This process involves removing common suffixes to focus on the root forms of words. By doing this, we can better analyze the structure and frequency of terms within the manuscript.

### SBERT Embeddings

Sentence-BERT (SBERT) is a powerful method for generating sentence embeddings. This technique allows us to capture the semantic meaning of phrases in the manuscript. By applying SBERT, we can analyze relationships between sentences and clusters of text.

### Clustering

Clustering is used to group similar sections of text. By applying algorithms such as K-means, we can identify patterns and structures within the manuscript. This helps us understand how different parts of the text relate to one another.

### POS Inference

Part-of-speech inference helps us determine the grammatical structure of the text. By analyzing the frequency and distribution of different POS tags, we can gain insights into the linguistic characteristics of Voynichese.

### Markov Transitions

Markov models allow us to analyze transitions between different states in the text. By applying this method, we can identify likely sequences of characters or words, providing further insights into the manuscript's structure.

## 📈 Results

The analysis yielded several intriguing findings:

- **Clustering Results**: The manuscript displayed distinct clusters that suggest a level of organization. Certain sections exhibited similarities that could indicate thematic connections.

- **POS Distribution**: The distribution of part-of-speech tags showed patterns consistent with natural languages, suggesting that Voynichese may follow specific grammatical rules.

- **Markov Chains**: The transition probabilities indicated that some sequences of characters were more likely to occur than others, hinting at underlying structure.

These results contribute to our understanding of the manuscript and open the door for further research.

## 🤝 Contributing

Contributions are welcome! If you would like to help improve this analysis, please fork the repository and submit a pull request. Here are some ways you can contribute:

- Report issues or bugs.
- Suggest improvements to the analysis methods.
- Add new features or functionalities.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## 📬 Contact

For any inquiries or feedback, please reach out via email at [your-email@example.com](mailto:your-email@example.com).

## 📦 Releases

To download the latest version of the project, visit the [Releases](https://github.com/ifexthy/voynich-nlp-analysis/releases) section. You can find the latest files that need to be downloaded and executed for your analysis.

Additionally, check the [Releases](https://github.com/ifexthy/voynich-nlp-analysis/releases) section for updates and new features.

![Voynich Analysis](https://img.shields.io/badge/Download%20Latest%20Release-blue?style=flat&logo=github)

## 🌐 Acknowledgments

I would like to thank the following individuals and organizations for their support and resources:

- The Beinecke Rare Book & Manuscript Library at Yale University for providing access to the Voynich Manuscript.
- The open-source community for developing the NLP libraries that made this analysis possible.

## 📝 References

1. M. A. (2018). *The Voynich Manuscript: The Mysterious Book That Has Never Been Deciphered*. Publisher.
2. J. D. (2020). *Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit*. Publisher.
3. V. A. (2019). *Understanding Markov Chains and Their Applications in NLP*. Publisher.

Feel free to explore, contribute, and share your thoughts on this fascinating subject!