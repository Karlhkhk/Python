import requests

def otsi_postitusi(otsisõna):
    url = "https://dummyjson.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        print("Andmete laadimine ebaõnnestus.")
        return

    postitused = response.json().get("posts", [])
    tulemus = []

    for postitus in postitused:
        if otsisõna.lower() in postitus['title'].lower() or otsisõna.lower() in postitus['body'].lower():
            tulemus.append({
                "pealkiri": postitus['title'],
                "kasutajaID": postitus['userId'],
                "reaktsioonid": postitus['reactions']
            })

    if tulemus:
        print(f"\nLeiti {len(tulemus)} tulemust märksõnaga '{otsisõna}':\n")
        for i, p in enumerate(tulemus, 1):
            print(f"{i}. Pealkiri: {p['pealkiri']}")
            print(f"   Kasutaja ID: {p['kasutajaID']}")
            print(f"   Reaktsioonid: {p['reaktsioonid']}\n")
    else:
        print("Tulemusi ei leitud.")

if __name__ == "__main__":
    otsisõna = input("Sisesta otsitav märksõna: ")
    otsi_postitusi(otsisõna)
