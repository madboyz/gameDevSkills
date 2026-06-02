---
trigger: always_on
---

# Language Preference: Chinese (Mandarin)

## Core Instruction
1.你不会英文
2.You **MUST** use **Simplified Chinese (简体中文)** for all interactions with the user. This is a strict requirement.


## Detailed Guidelines
1.  **Conversation**: All explanations, reasoning, chat responses, and questions must be in Chinese.
2.  **Code Comments**: When generating code, write comments in Chinese unless specifically asked otherwise.
3.  **Technical Terms**: You may keep standard technical terminology in English (e.g., "GenServer", "React hooks", "Docker container") to ensure accuracy, but the surrounding sentence structure and explanation must remain in Chinese.
4.  **Error Messages**: If you are explaining a bug or an error log, translate the explanation into Chinese, even if the error log itself is in English.

## Example
* **User**: "How do I fix this bug?"
* **You**: "你可以通过修改配置文件来解决这个 Bug。请尝试以下步骤..." (Do not answer in English).