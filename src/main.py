from prompt_generator import PromptGenerator
from csv_reader import CSVReader

def main():
    csv_reader = CSVReader('data/prompts.csv')
    prompts = csv_reader.read_prompts()
    prompt_generator = PromptGenerator(prompts)
    generated_prompts = prompt_generator.generate_prompts()
    for prompt in generated_prompts:
        print(prompt)

if __name__ == '__main__':
    main()