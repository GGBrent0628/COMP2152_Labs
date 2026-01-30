contacts = {
    "Angelica": "555-1431",
    "Sana": "555-1432",
    "Karina": "555-1433",
    "Asa": "555-1434"
}
print(f"Angelica's number: {contacts['Angelica']}")
contacts["Winter"] = "555-1435"
print(f"Contacts after adding Diana: {contacts}")
contacts["Angelica"] = "143-1431"
print(f"Contacts after updating Angelica {contacts}")
del contacts["Asa"]
print(f"Contacts after deleting Asa: {contacts}")
print(f"All names {contacts.keys()}")
print(f"All numbers {contacts.values()}")
print(f"Total contacts {len(contacts)}")