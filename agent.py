import os
import json
import sys

class TextFileAgent:
    def __init__(self, input_dir="inputs", output_dir="outputs"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.results = []

    def scan_inputs(self):
        if not os.path.exists(self.input_dir):
            print(f"Input folder '{self.input_dir}' does not exist.")
            return []
        
        files = []
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".txt"):
                files.append(os.path.join(self.input_dir, filename))
        return files

    def process_file(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        words = text.split()
        return {
            "file": filepath,
            "word_count": len(words),
            "preview": " ".join(words[:10]),    
            "file_size": os.path.getsize(filepath)
    }

    def run(self):
        print(f"Scanning folder: {self.input_dir}")
        files = self.scan_inputs()

        for file in files:
            result = self.process_file(file)
            self.results.append(result)

        os.makedirs(self.output_dir, exist_ok=True)

        output_path = os.path.join(self.output_dir, "results.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2)

        print("Processing complete.")

if __name__ == "__main__":
    input_dir = sys.argv[1] if len(sys.argv) > 1 else "inputs"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "outputs"

    agent = TextFileAgent(input_dir=input_dir, output_dir=output_dir)
    agent.run()


                  





            
