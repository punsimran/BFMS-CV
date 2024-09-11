import pickle

with open("trained_encodings2.pkl", "rb") as f:
    data = pickle.load(f)

print("Encodings:", data["encodings"])
print("Names:", data["names"])
