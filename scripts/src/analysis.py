import json


def word_handle(data):
	word_dict = {}
	y = 2010
	for d in data:
		print(d)
		text = d["text"]
		word_list = []
		for t in text:
			words = t["words"]
			word_list.append(words)
		word_dict[str(y)] = word_list
		y += 1
		return word_dict


if __name__ == "__main__":
	js = open("../../output/word.json", "r").read()
	data = json.loads(js)["data"]
	word_dict = word_handle(data)
