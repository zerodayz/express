import sys


def action_code_generator(code):
    # keywords and their corresponding functions
    keywords = {
        "Open Page": "actions.go",
        "Click On": "actions.mouse_click",
        "Take Screenshot": "actions.take_screenshot",
    }
    # for each line in the code, split it into a list of words
    lines = code.splitlines()
    # trim the whitespace from each line
    lines = [line.strip() for line in lines if line]
    # remove empty lines
    output = ""
    for line in lines:
        # search for the keyword in the line
        # Convert Test Name keyword into def test_name(actions):
        if "Test Name" in line:
            # remove the keyword from the line
            line = line.replace("Test Name", "")
            # remove the whitespace from the line
            line = line.strip()
            # add the function to the line
            line = "def test_" + line.lower() + "(actions):"
            # add the line to the output
            output += line + "\n"
        for keyword in keywords:
            if keyword in line:
                # find keyword and convert it into a function
                function = keywords[keyword]
                # remove the keyword from the line
                line = line.replace(keyword, "")
                # remove the whitespace from the line
                line = line.strip()
                # take the line and split it into a list of words by ,
                line = line.split(",")
                # wrap each word in quotes
                line = [f"\"{word.strip()}\"" for word in line]
                # join the list of words into a string
                line = ", ".join(line)
                # add the function to the line and indent it
                line = "    " + function + "(" + line + ")"
                # add the line to the output
                output += line + "\n"
    return output


if __name__ == "__main__":
    filename = sys.argv[1]
    # read the code from the file as argument
    with open(filename, "r") as f:
        code = f.read()
    # replace the extension with .py
    new_filename = filename.replace(".rsc", ".py")
    directory = new_filename.split("/")[0]
    filename = new_filename.split("/")[1]
    # prefix with test_
    new_filename = directory + "/test_" + filename
    with open(new_filename, "w") as f:
        f.write(action_code_generator(code))
