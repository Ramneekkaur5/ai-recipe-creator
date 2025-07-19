🧑‍🍳 **AI Recipe Generator using Agno**

This project is a simple AI-based recipe creator built using the [Agno] framework and Groq models. It allows users to input a list of ingredients and get a recipe or meal suggestion.

---
📖 **Overview**

ChefGenius leverages cutting-edge AI models to generate creative and feasible recipes using natural language prompting. It's ideal for:

- Home cooks with limited ingredients
- Health-conscious users with dietary needs
- Beginners looking for step-by-step guidance
- Anyone in need of quick, customized cooking ideas 

---
📌 **Features**

- Uses Groq LLMs via Agno's `Agent`.
- Tool integration using DuckDuckGo search.
- Clean prompt-response architecture.
- Handles both markdown and plain-text outputs.
---
🗂️ **Project Structure**

> recipe_creator.py      # Main Python script

> README.md              # Project documentation

---
📦 Requirements

Python 3.10+

python-dotenv

Groq API Key

OpenAI API Key

---
⚙️ **Setup Instructions**

1. Install Python
2. Clone the Repository:
   ```
     git clone <your-repo-url>
     cd <your-repo-directory>
   ```
3. Create a Virtual Environment:
   ```
   venv\Scripts\activate
   ```
   
4. Install dependencies:
   ```
   pip install agno openai
   ```
---
▶️ **How to Run**

->In the terminal, navigate to the project directory and run:
     
     python recipe_creator.py
     
->Customize your recipe query Edit

---
⚙️ **How It Works**

 1. Agent Initialization
- Instantiates an agent named `ChefGenius` using `Groq(id="qwen/qwen3-32b")` LLM.
- Uses the `WikipediaTools()` tool for enhanced knowledge grounding.

 2. Environment Setup
- Loads OpenAI and Groq API keys from a `.env` file via `python-dotenv`.

 3. Prompt Generation
- Dynamically constructs a detailed cooking prompt using:
  - Ingredients
  - Dietary preference
  - Cooking time
  - Skill level

 4. Agent Execution
- `ChefGenius.run()` sends the generated prompt to the LLM.
- Returns a recipe response formatted in Markdown with:
  - 🍽️ Title  
  - 📝 Ingredient List  
  - 👨‍🍳 Numbered Steps  
  - ⏱️ Estimated Time  
  - 🔬 Nutritional Info  
  - 💡 Smart Tips

 5. Output Display
- The final recipe is printed in the terminal

---
📝 **License**

This project is licensed under the MIT License.

See the ``LICENSE`` file for details.

---



