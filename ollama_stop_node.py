import subprocess
from typing import Any, Tuple


class OllamaStopNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_name": ("STRING", {"default": ""}),
                "input": ("*",),
            },
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("output",)
    FUNCTION = "execute"
    CATEGORY = "Ollama"
    OUTPUT_IS_LIST = (False,)

    def execute(self, model_name: str, input: Any) -> Tuple[Any]:
        """
        execute 'ollama stop <model_name>' command and return the input unchanged.
        """
        if model_name:
            try:
                subprocess.run(
                    ["ollama", "stop", model_name],
                    check=False,
                    capture_output=True,
                )
            except Exception:
                # swallow exceptions to avoid breaking workflows
                pass

        return (input,)


NODE_CLASS_MAPPINGS = {
    "OllamaStopNode": OllamaStopNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OllamaStopNode": "Ollama Stop",
}

