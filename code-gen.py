import sys


def action_code_generator(code):
    keywords = {
        "Set Credentials": "actions.set_credentials",
        "Open Page": "actions.go",
        "Open Page Wait Page Load": "with actions.wait_for_page_to_load():\n        actions.go",
        "Login Wait Page Load": "with actions.wait_for_page_to_load():\n        actions.login",
        "Click On": "actions.mouse_click",
        "Click On Wait Page Load": "with actions.wait_for_page_to_load():\n        actions.mouse_click",
        "Take Screenshot": "actions.take_screenshot",
    }
    lines = code.splitlines()
    lines = [line.strip() for line in lines if line]
    output = ""
    for line in lines:
        if "Parametrize Test Accounts" in line:
            line = line.replace("Parametrize Test Accounts:", "").strip()
            line = [f"{word.strip()}" for word in line.split(",")]
            line = ", ".join(line)
            line = f"import pytest as pytest\nfrom express import utils\n\n\n@pytest.mark.parametrize({line})"
            output += line + "\n"
            continue
        if "Test Name With Accounts" in line:
            line = line.replace("Test Name With Accounts:", "").strip()
            line = f"def test_{line.lower()}(actions, credentials):"
            output += line + "\n"
            continue
        if "Test Name" in line:
            line = line.replace("Test Name:", "").strip()
            line = f"def test_{line.lower()}(actions):"
            output += line + "\n"
            continue
        keyword = line.split(":", 1)
        arguments = keyword[1].strip()
        if keyword[0] in keywords:
            line = f"    {keywords[keyword[0]]}({arguments})"
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
