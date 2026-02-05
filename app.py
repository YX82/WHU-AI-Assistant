import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 读取知识库
with open("knowledge.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

documents = [item["title"] + " " + item["content"] for item in knowledge]

# 建立向量模型（把文本变成“数学向量”）
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def answer_question(question):
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, doc_vectors)[0]
    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    if best_score < 0.1:
        return "抱歉，知识库中暂时没有找到相关信息。"

    best_item = knowledge[best_match_index]
    return f"【{best_item['title']}】\n{best_item['content']}"

print("🎓 武汉大学校园智能问答助手（智能检索版）已启动！输入 q 退出\n")

while True:
    q = input("请输入你的问题：")
    if q.lower() == "q":
        break

    ans = answer_question(q)
    print("\n🤖 回答：\n", ans, "\n")
