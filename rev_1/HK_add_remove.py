from HK_dict import HOTKEYS
if __name__ == '__main__':
    # print(HOTKEYS)
    # del HOTKEYS['sucks']
    # print(HOTKEYS)

    lines = []
    stringtest = str(HOTKEYS['<alt>+<ctrl>+f+1'])
    lines.append(stringtest)
    print(lines)

    # lines = []
    # lines.append("from HK_output import *")
    # for i, keys in enumerate(HOTKEYS):
    #     lines.append((keys:HOTKEYS[keys]))
    # with open("HK_dict.py", "w") as f:
    #     f.write("\n".join(lines))
