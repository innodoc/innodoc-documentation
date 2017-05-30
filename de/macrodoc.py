import re

class CmdCollector(object):
    pass

def generate_paramtext(cmd, n):
    s = "\\texttt{\\relax$\\backslash$" + cmd
    for k in range(n):
        s += "\{PRM\#" + str(k + 1) + "\}"
    s += "}"
    return s


def notifyCommand(col, cmd, typ, usage):
    s = "\\texttt{" + cmd + "} & " + typ + " & " + usage
    if s in col.clist:
        return ""
    else:
        col.clist.append(s)
    return ""


collector = CmdCollector()
collector.clist = list()
text = "Codegenerierung aus mintmod.tex gescheitert!\n"
with open("mintmod.tex", "r", encoding = "utf-8") as f:
    macrotex = f.read()
    text = ""
    capture_usage = r"%[\t ]*@usage[\t ]+([^\n]*)\n"
    capture_params = r"\[(\d*)\]"
    cmd_list = ["newcommand", "providecommand", "newenvironment", "DeclareMathOperator"]
    desc_list = ["Kommando", "Kommando", "Umgebung", "Matheoperator"]
    for k in range(len(cmd_list)):
        # try capture with usage instead of parameter counting, then with parameters, then solo
        capture_main = r"\\" + cmd_list[k] + r"\{(?:\\)*([^\}]+)\}(?:#[123456789])*"
        macrotex = re.sub(capture_usage + capture_main, lambda m: notifyCommand(collector, m.group(2), desc_list[k], "\\verb%" + m.group(1) + "%"), macrotex, 0, re.S)
        macrotex = re.sub(capture_main + capture_params, lambda m: notifyCommand(collector, m.group(1), desc_list[k], generate_paramtext(m.group(1), int(m.group(2)))), macrotex, 0, re.S)
        macrotex = re.sub(capture_main, lambda m: notifyCommand(collector, m.group(1), desc_list[k], ""), macrotex, 0, re.S)
    macrotex = re.sub(r"\\def\\(\w*)", lambda m: notifyCommand(collector, m.group(1), "Definition", ""), macrotex, 0, re.S)
    collector.clist = sorted(collector.clist,  key = lambda s: s.lower())
    text += "\\begin{MDTabular}{lll}\n"
    text += "\\ifttm\\relax\\else%\nSchlüsselwort & Typ & Benutzung\\\\\\hline\n\\fi%\n"
    text += "\\ \\\\\n".join(collector.clist)
    text += "\\end{MDTabular}\n"

print(text)
