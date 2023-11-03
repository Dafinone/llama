from transformers import AutoTokenizer
import transformers
import torch


model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
    "text-generation", model=model, torch_dtype=torch.float16, device_map="auto"
)

sequences = pipeline(
    'I have recently watch "24" and "Suits" and thoroughly enjoyed them. Can you give me 10 recommendations of series I might find interesting?\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)

for seq in sequences:
    print(f"Result: {seq['generated_text']}")
