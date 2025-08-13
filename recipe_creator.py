from agno.agent import Agent
from agno.tools.wikipedia import WikipediaTools
from agno.models.groq import Groq
from agno.models.openai import OpenAIChat

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OpenAI_API_KEY"]=os.getenv("OpenAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")




ChefGenius = Agent(
    name="ChefGenius",
    model=Groq(id="qwen/qwen3-32b"),
    tools=[WikipediaTools()],
    markdown=True
)


def generate_prompt(input_data):
    return f"""
You are ChefGenius 🍳, a smart recipe creator.

🔸 Create a recipe based on:
- Ingredients: {', '.join(input_data['ingredients'])}
- Diet: {input_data['diet']}
- Max Cooking Time: {input_data['time']} minutes
- Skill Level: {input_data['skill_level']}

🧾 Format response in **Markdown** with:
1. **Recipe Title 🍽️**
2. **Ingredients List 📝**
3. **Steps (Numbered) 👨‍🍳**
4. **Estimated Cooking Time ⏱️**
5. **Nutritional Info 🔬 (Calories, Protein, Carbs, Fat)**
6. **Tips 💡 (Swaps, pitfalls, and plating ideas)**

Use emojis where helpful!
"""


user_input = {
    "ingredients": ["paneer", "onion", "tomato"],
    "diet": "vegetarian",
    "time": 20,
    "skill_level": "beginner"
}

prompt = generate_prompt(user_input)
response = ChefGenius.run(prompt, stream=False)
print(response.content)



