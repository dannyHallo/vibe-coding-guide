# vibe-coding-guide

This is a vibe coding guide for the modern era. Currently just for personal use.

## Tools

-   **Aider**
    -   An open-sourced AI coding assistant.
    -   *Note: Consider using it as a Master Control Program (MCP) and connecting it to Claude Code.*
    -   Reference: [CRACKED Aider AND Claude Code Combo. Zuck ships Llama4. Gemini 2.5 Pro is SOTA?](https://www.youtube.com/watch?v=QzZ97noEapA)

-   **Claude Code**
    -   *Note: Might be a better alternative, testing required.*

-   **[Repomix](https://github.com/yamadashy/repomix)**
    -   Packs your entire repository into a single, AI-friendly file.

-   **Cursor**
    -   An AI-first code editor.

## Other References

-   [AI Coding DEVLOG: Claude Code has CHANGED Software Engineering](https://www.youtube.com/watch?v=d-SyGA0Avtw)

## Setup

### Aider

1.  **Install Aider**

2.  **Setup API Key**
    -   We are currently using Gemini 2.5 Pro as the backend LLM. Consider checking the [LLM Benchmark](https://artificialanalysis.ai/) regularly for the latest performance metrics.
    -   Use the [OpenAI Compatible APIs guide](https://aider.chat/docs/llms/openai-compat.html) for setup. This method also supports other models.
    -   The API can be found at a low cost on services like Taobao. You can find pricing and supported models [here](https://www.chataiapi.com/pricing).

3.  **Configure Aider**
    -   In your terminal, you can configure `aider` to use your chosen model:

      ```shell
      aider --model openai/<model-name>
      ```

    -   Replace `<model-name>` with the model you want to use. You can copy the exact model names from the [pricing page](https://www.chataiapi.com/pricing).
