import pandas as pd

pairs = []


def read_dataset(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                pairs.append(parts)


# read all datasets
read_dataset("natural_chat.txt")
read_dataset("dialogs.txt")
read_dataset("human_chat.txt")

df = pd.DataFrame(pairs, columns=["question", "answer"])

df.to_csv("chatbot_dataset.csv", index=False)

print("Dataset prepared!")
print("Total pairs:", len(df))
