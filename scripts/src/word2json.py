import os
import json
import xmltodict

xml_list = os.listdir("./xml/")
eng_reading = json.loads(open("./noword.json", "r").read())
eng_data = eng_reading["data"]
n = 0
for data in eng_data:
    text = data["text"]
    for t in text:
        word_list = []
        try:
            xml = "./xml/" + xml_list[n]
            with open(xml, 'r', encoding='UTF-8') as f:
                doc = xmltodict.parse(f.read())
            for word in doc['Frhelper_Backup']['StudyLists']['CustomizeListItem']:
                word_list.append(word["@word"])
            f.close()
            print(n)
        except:
            pass
        t["words"] = word_list
        n+=1
new_reading = json.dumps(eng_reading)
with open("./english_reading_10_19_word_191003.json", "w") as e:
    e.write(new_reading)
print("数据解析存储完毕！！！")