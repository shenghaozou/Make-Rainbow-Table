import sys
import hashlib
import random

fn = sys.argv[1]
k = int(sys.argv[2])
COMMAND = "select * from rainbow where hash = \"{}\"; --{}\n"
sql = ""

with open(fn) as fr:
    words = [word.strip() for word in fr]
    sample_words = random.sample(words, k)
    for word in sample_words:
        hash = hashlib.sha256(word.encode()).hexdigest()
        sql += COMMAND.format(hash, word)

print(sql)
with open("test.sql", "w") as fw:
    fw.write(sql)

print("finished.")
