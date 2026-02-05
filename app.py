import json
import gradio as gr
from openai import OpenAI

client = OpenAI(api_key="你的API_KEY")

# 读取知识库
with open("knowledge.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# 简单关键词检索
def search_knowledge(question):
    results = []
    for item in knowledge:
        if any(word in item["content"] for word in question):
            results.append(item["content"])
    return "\n".join(results[:3])

def answer_question(question):
    context = search_knowledge(question)

    prompt = f"""
你是武汉大学校园智能助手，请根据提供的校园资料回答问题。

资料：
{context}

问题：{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

demo = gr.Interface(fn=answer_question,
                    inputs="text",
                    outputs="text",
                    title="武大校园智能问答助手")

demo.launch()
