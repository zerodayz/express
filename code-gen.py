import sys


def action_code_generator(code):
    keywords = {
        "Open Page": "actions.go",
        "Click On": "actions.mouse_click",
        "Take Screenshot": "actions.take_screenshot",
    }
    lines = code.splitlines()
    lines = [line.strip() for line in lines if line]
    output = ""
    for line in lines:
        if "Test Name" in line:
            line = line.replace("Test Name", "").strip()
            line = f"def test_{line.lower()}(actions):"
            output += line + "\n"
        for keyword, function in keywords.items():
            if keyword in line:
                line = line.replace(keyword, "").strip()
                line = [f"\"{word.strip()}\"" for word in line.split(",")]
                line = ", ".join(line)
                line = "    " + function + "(" + line + ")"
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
