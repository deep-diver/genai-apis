from .openai_api import OpenAIAPI
from .gemini_api import GeminiAPI
from .anthropic_api import AnthropicAPI


class APIFactory:
    @staticmethod
    def get_api_client(api_name, **kwargs):
        if api_name == "openai":
            try:
                from openai import AsyncOpenAI

                return OpenAIAPI(AsyncOpenAI(api_key=kwargs["api_key"]))
            except ImportError:
                raise ImportError(
                    "OpenAI library is not installed. Please install the package before proceeding."
                )
        elif api_name == "gemini":
            try:
                import google.generativeai as genai

                genai.configure(api_key=kwargs["api_key"])
                return GeminiAPI()
            except ImportError:
                raise ImportError(
                    "Google GenerativeAI library is not installed. Please install the package before proceeding."
                )
        elif api_name == "anthropic":
            try:
                from anthropic import AsyncAnthropic

                return AnthropicAPI(AsyncAnthropic(api_key=kwargs["api_key"]))
            except ImportError:
                raise ImportError(
                    "Anthropic library is not installed. Please install the package before proceeding."
                )
        else:
            raise ValueError("Unsupported API")
