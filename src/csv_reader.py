import csv
from dataclasses import dataclass
from typing import List

@dataclass
class Prompt:
    company_name: str
    industry: str
    description: str

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_prompts(self) -> List[Prompt]:
        prompts = []
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                company_name, industry, description = row
                prompt = Prompt(company_name, industry, description)
                prompts.append(prompt)
        return prompts