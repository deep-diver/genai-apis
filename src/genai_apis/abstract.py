class TextGenerationAPI:
    """Abstract base class for text generation APIs."""

    async def generate_text(self, prompt):
        """Generate text based on the given prompt."""
        raise NotImplementedError("This method should be overridden by subclasses.")
