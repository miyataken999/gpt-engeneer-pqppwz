from dataclasses import dataclass
import random

@dataclass
class Prompt:
    company_name: str
    industry: str
    description: str

class PromptGenerator:
    def __init__(self, prompts):
        self.prompts = prompts

    def generate_prompts(self):
        generated_prompts = []
        for prompt in self.prompts:
            company_name = prompt.company_name
            industry = prompt.industry
            description = prompt.description
            generated_prompt = f"Can you describe the company {company_name} in the {industry} industry? {description}"
            generated_prompts.append(generated_prompt)
        return generated_prompts