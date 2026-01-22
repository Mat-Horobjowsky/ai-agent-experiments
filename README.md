# AI Text File Agent
Small AI agents for document analysis, research, and automation

---

## Features
- Scan a folder of text files and count words
- Generate previews of each file
- Save results as JSON for further analysis
- Configurable input and output folders
- Automatically creates missing output folders
- Handles multiple files in a folder

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Mat-Horobjowsky/ai-agent-experiments.git

## Run the agent with:
python agent.py <input_folder> <output_folder>

Example:
python agent.py my_inputs my_outputs

The agent will scan all .txt files in my_inputs
Results are saved in results.json inside my_outputs

Sample Input

my_inputs/doc1.txt:

AI agents help teams automate repetitive tasks and save time.


my_inputs/doc2.txt:

Python is commonly used to build automation scripts and tools.

Sample Output

my_outputs/results.json:

[
  {
    "file": "my_inputs/doc1.txt",
    "word_count": 10,
    "preview": "AI agents help teams automate..."
  },
  {
    "file": "my_inputs/doc2.txt",
    "word_count": 10,
    "preview": "Python is commonly used to build..."
  }
]

Notes

Ensure input folders exist; agent will create output folders automatically

Works with multiple text files

Future improvements: support PDFs, DOCX, or CSV files, more advanced analytics
