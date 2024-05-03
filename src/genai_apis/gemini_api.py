from .abstract import TextGenerationAPI


class GeminiAPI(TextGenerationAPI):
    async def generate_text(self, model, prompt, system_instruction=None, **kwargs):
        import google.generativeai as genai

        model = genai.GenerativeModel(
            model_name=model, system_instruction=system_instruction
        )
        response = await model.generate_content_async([prompt], **kwargs)
        return response.text
