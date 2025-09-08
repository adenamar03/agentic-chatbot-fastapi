# step # 1 --> set up api keys for groq, openai and tavily

import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#step # 2 --> setup llm and the tools
#step # 3 --> setup AI Agent with Search tool functionality
