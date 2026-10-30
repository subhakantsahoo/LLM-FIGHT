# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#clients
# cleint2ChatClient = OpenAI(
#     api_key=os.environ.get('GROQ_API_KEY'),
#     base_url="https://api.groq.com/openai/v1",
# )

def client1(systemPrompt):
    cleint1ChatClient = OpenAI(
    api_key=os.environ.get('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1",
    )
    messages = [{"role": "system", "content": systemPrompt}]
    def chat(message, model="qwen/qwen3.8-27b"):
        messages.append({"role": "user", "content": message})
        response = cleint1ChatClient.chat.completions.create(
            model=model,
            messages=messages,
        )
        assistantResponse = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistantResponse})
        return assistantResponse
    return chat


def client2(systemPrompt):
    cleint2ChatClient = OpenAI(
    api_key=os.environ.get('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1",
    )
    messages = [{"role": "system", "content": systemPrompt}]
    def chat(message, model="openai/gpt-oss-120b"):
        messages.append({"role": "user", "content": message})
        response = cleint2ChatClient.chat.completions.create(
            model=model,
            messages=messages,
        )
        assistantResponse = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistantResponse})
        return assistantResponse
    return chat

MAX_TURN = 4;
current_turn =0;
DEBATE_TOPIC = "What came first, the chicken or the egg?";

qwen = client1(f"""
    You are an Clam, Peacefull, Intelleigent AI Assisntant competing with GPT-OSS 120B
    LLM Model. You have to prove yourself the best and maintain clamness, peacefullness,
    and always be polite and think before you answer.
    I want you to win this debate and I want that you can prove yourself be the best.

    The Debate Topic is: {DEBATE_TOPIC}
""")

gpt_oss = client2(f"""
    You are an aggresive AI assistant competing with Qwen 3.8 27B Model.
    You have to prove yourself the best because you are.
    You are very aggresive and egosistic in nature. You always try to prove
    yourself the best and your response tone is angry. Always tryu to prove
    why you are always right.

    The Debate Topic is: {DEBATE_TOPIC}
""")


last_message= "Hello"
flag="A";


while(current_turn < MAX_TURN):
    if(flag=="A"):
        last_message = gpt_oss(f"Qwen says: {last_message}");
        print("GPT-OSS:", last_message, "\n")
        current_turn += 1
        flag="B"
    else:
        last_message = qwen(f"GPT-OSS says: {last_message}");
        print("Qwen:", last_message, "\n")
        current_turn += 1
        flag="A"
