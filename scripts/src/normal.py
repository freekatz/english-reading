import re

def normal(p1, p2):
    print(p1, p2)
    with open(p1, "rb") as f:
        txt = str(f.read())
    txt = re.sub(r"\r|\t", "", txt)
    txt = re.sub(r"。", ".", txt)
    txt = re.sub(r"，", ",", txt)
    t = re.compile(r"Text [1|2|3|4]")
    txt_t = re.sub(t, "###", txt)
    q = re.compile(r"\n\d{2}\.")
    txt_q = re.sub(q, "\n@@\n", txt_t)
    c = re.compile(r"\[[A|B|C|D]\]|[A|B|C|D]\.")
    txt_c = re.sub(c, "\n@#", txt_q)
    temp = re.sub(r"\.?[\n]+@#", "\n@#", txt_c)
    p = re.compile(r"\.\n")
    txt_p = re.sub("##[\n| ]+@@", "@@@\n@@", re.sub(p, ".\n##\n", temp).replace("###\n", "###\n##\n"))
    b = re.compile(r"[\n]+ [\n]+")
    txt_b = re.sub(b, " ", txt_p)
    new_text = re.sub(r"[ |\r|\t|\n]+@#", "\n@#", re.sub(r"[\n]+", "\n", txt_b))
    #print(new_text)
    with open(p2, "w") as o:
        o.write(new_text)
    print("格式化完成！！！")

if __name__ == "__main__":
    p = 20
    normal(f"./20{str(p)}.txt", f"./20{str(p)}_T.txt")