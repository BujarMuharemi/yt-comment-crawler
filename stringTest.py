a = "Sig.rule :- Don't hesitate to say you're best .                                                                        Also Sigma rule #69:- Legends don't say yourself best .."
a=" ".join(a.split())
print(a)

with open('comment-crawler\dev.env', 'r') as file:
    data = file.read().rstrip()

print(data)