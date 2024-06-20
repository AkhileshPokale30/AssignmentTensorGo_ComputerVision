from transformers import pipeline

def initialize_llm():
    llm = pipeline('text-generation', model='gpt2')
    return llm

def ask_question(llm, prompt):
    response = llm(prompt, max_length=100, truncation=True)
    generated_text = response[0]['generated_text']
    
    # Extract valid column names from the generated text
    try:
        columns = generated_text.split(':')[-1].strip().split(',')
        columns = [col.strip() for col in columns if col.strip()]
    except:
        columns = []
    return columns
