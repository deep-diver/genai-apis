# genai-apis

```python
# openai, gemini, gemini-vertex, anthropic, anthropic-vertex, anthropic-bedrock
# !pip install genai-apis[openai]

kwargs = {
  "api_key": "..."
  "GCP_PROJECT_ID": "...",
  "GCP_LOCATION": "...",
  "AWS_LOCATION": "..."
}

extra_kwargs = {
  ...
  stream=False
}

service = "openai"
model = "gpt-4-turbo-2024-04-09"
prompt = "Hello!!"

# openai, 
# gemini, gemini-vertex, 
# anthropic, anthropic-bedrock, anthropic-vertex
api_client = APIFactory.get_api_client(service, **kwargs)
result = await api_client.generate_text(model, prompt, **extra_kwargs)
print(result)

# for stream
async for chunk in result:
    print(chunk, end='')
```