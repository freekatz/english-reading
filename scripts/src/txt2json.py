import re, os
import json
eng_reading = {
    "data": [None]*10,
    "info": {}
}
txt_list = os.listdir("../../input/articles/")
print(txt_list)
year = 2010
n3 = 0
for txt in txt_list:
    per_data = {
        "no": year,
        "text": [None]*4
    }
    f = open("../../input/articles/" + txt, "r")
    content = f.read().strip()
    T = re.compile(r"###(.*?)@@@", re.DOTALL)
    p = re.compile(r"\n@##\n")
    Q = re.compile(r"(.*)###", re.DOTALL)
    q = re.compile(r"\n#@@\n")
    c = re.compile(r"\n@#")
    texts = re.findall(T, content)
    temp_content = re.sub("[\\x00-\\x08|\\x0b-\\x0c|\\x0e-\\x1f]", "", content)
    n2 = 0
    for t in texts:
        per_text = {
            "no": n2,
            "T": "",
            "Q": [None]*5
        }
        per_text["T"] = t
        temp_content = re.sub(t, "", temp_content)
        questions = re.split(q, re.split(r"###", temp_content)[n2+1])[1:]
        # print(questions)
        n1 = 0
        for question in questions:
            per_question = {
                "no": n1,
                "question":question
            }
            # print(per_question)
            # print("==============")
            per_text["Q"][n1] = per_question
            n1+=1
        per_data["text"][n2] = per_text
        n2+=1
    eng_reading["data"][n3] = per_data
    year +=1
    n3+=1

eng_data = json.dumps(eng_reading)
with open("english_reading_10_19_noword_191003.json", "w") as e:
    e.write(eng_data)
print("数据解析存储完毕！！！")
