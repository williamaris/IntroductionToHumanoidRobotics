import os

input_file = 'SetupBipedRobot.txt'
output_file = 'SetupBipedRobot.py'

links = []

with open(input_file, 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = line.split(',')

        
        if len(line) > 1:
            val = {
                "name": line[1].strip(),
                "m": float(line[3]),
                "sister": int(line[5]),
                "child": int(line[7]),
                "b": " ".join(line[9].replace("'", "").split()).replace(' ', ', '),
                "a": line[11],
                "q": float(line[13].split(')')[0])}

            links.append(val)


with open(output_file, 'a') as f:
    for idx in range(len(links)):
        results = "uLINK[" + str(idx + 1) + "] = Link("
        results += "name=" + links[idx]["name"] + ", "
        results += "m=" + str(links[idx]["m"]) + ", "
        results += "sister=" + str(links[idx]["sister"]) + ", "
        results += "child=" + str(links[idx]["child"]) + ", "
        results += "b=np.array(" + links[idx]["b"] + ").T, "
        results += "a=" + links[idx]["a"] + ", "
        results += "q=" + str(links[idx]["q"]) + ")\n"
        f.write(results)
            