import subprocess

out=subprocess.run(["wmctrl", "-d"], capture_output=True, text=True).stdout
buttons = ["(box "]
for i, line in enumerate(out.split("\n")):
    if len(line) == 0:
        break
    splitted = line.split()
    is_active = splitted[1] == "*"
    name = splitted[-1]
    css_class = "active_workspace" if is_active else "workspace" 
    buttons.append("(button :onclick \"wmctrl -s " + str(i) + "\" :class \"" + css_class + "\" \"" + name + "\")")
print(''.join(buttons) + ")")
