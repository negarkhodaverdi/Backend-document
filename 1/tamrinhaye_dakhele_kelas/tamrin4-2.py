data = {
    "name": "reza",
    "family": "rezaei",
    "social": {
        "instagram": {
            "fake": ["ali123", "peykan"],
            "real": ["rezaei"]
        },
        "telegram": "rezaei_reza",
        "twitter": "loser_user"
    }
}

print(data["social"]["instagram"]["fake"])
print(data["social"]["instagram"]["real"])

tedad_fake = len(data["social"]["instagram"]["fake"])
tedad_real = len(data["social"]["instagram"]["real"])

print("Tedad Account Haye Fake :", tedad_fake)
print("Tedad Account Haye Real :", tedad_real)
