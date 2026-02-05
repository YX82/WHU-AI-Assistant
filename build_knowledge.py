from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json, time, re

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

# ✅ 武大各大官方入口栏目（稳定且信息多）
urls = [
    "https://www.whu.edu.cn",              # 武大官网首页
    "https://www.whu.edu.cn/xxgk/xxjj.htm",# 学校简介
    "https://www.whu.edu.cn/jgsz/yxsz.htm",# 院系列表
    "https://www.whu.edu.cn/jgsz/znbm.htm",# 职能部门
    "https://www.lib.whu.edu.cn",          # 图书馆
    "https://ugs.whu.edu.cn",              # 本科生院
    "https://gs.whu.edu.cn",               # 研究生院
    "https://xgb.whu.edu.cn",              # 学工部
    "https://xsjy.whu.edu.cn",             # 就业网
    "https://cwc.whu.edu.cn",              # 财务部
    "https://jwc.whu.edu.cn",              # 教务处
    "https://hr.whu.edu.cn",               # 人事部
    "https://fao.whu.edu.cn",              # 国际交流部
    "https://yz.whu.edu.cn",               # 研究生招生
    "https://admission.whu.edu.cn"         # 本科招生
]

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

knowledge = []

for url in urls:
    try:
        print("正在抓取:", url)
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        text = clean_text(soup.get_text(" ", strip=True))

        if len(text) > 1200:
            knowledge.append({
                "title": soup.title.string if soup.title else "WHU页面",
                "content": text[:4000],
                "source": url
            })
            print("✅ 成功:", url)
        else:
            print("⚠️ 内容较少:", url)

    except Exception as e:
        print("❌ 失败:", url)

driver.quit()

with open("knowledge.json", "w", encoding="utf-8") as f:
    json.dump(knowledge, f, ensure_ascii=False, indent=2)

print(f"\n🎉 知识库构建完成！共收录 {len(knowledge)} 条官网页面内容")






