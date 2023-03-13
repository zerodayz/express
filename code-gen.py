import json
import sys

from express import utils


def action_code_generator(code):
    # load keywords from keywords.json
    with open("keywords.json") as f:
        keywords = json.load(f)
    lines = code.splitlines()
    lines = [line.strip() for line in lines if line]
    output = ""
    for line in lines:
        line_keyword = []
        # walk the line and find all words starting by a capital letter
        words = line.split(" ")
        for word in words:
            if word[0].isupper():
                line_keyword.append(word)
        keyword = " ".join(line_keyword)
        # if line starts with keyword
        if keyword in keywords:
            # remove the keyword from the line
            line = line.replace(keyword, "").strip()
            # replace the keyword with the corresponding code
            line = keywords[keyword].format(line)
            output += line + "\n"
    return output


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        code = f.read()
    new_filename = filename.replace(".rsc", ".py")
    directory = "/".join(new_filename.split("/")[:-1])
    new_filename = "test_" + new_filename.split("/")[-1]
    filename = directory + "/" + new_filename
    with open(filename, "w") as f:
        f.write(action_code_generator(code))
