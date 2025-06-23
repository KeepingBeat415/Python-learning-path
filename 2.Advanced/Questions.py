# adding to multilevel dictionaries
d["employees"].append(dict(firstName="Alert", lastName="Bert"))

# add to JSON
with open("company1.json", "r+") as file:
    d = josn.loads(file.read())
    d["employees"].append(dict(firstName="Albert",lastName="Bert"))
    file.seek(0) # move cursor to index 0
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate() # delete content after cursor

# Time with Threshould
i = 0
while True:
    print("hello")

    i = i + 1
    if i > 3:
        print("End of loop")
    time.sleep(i)

# Letter Counter
response = request.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
count_a = text.count("a")
