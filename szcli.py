import imp
import json

def szin(disp):
    in_i = input(disp)
    return in_i


def szout(out_c):
    print(out_c)


def yn():
    while True:
        in_line = szin('y/n ? :')
        if in_line == 'y':
            return True
        elif in_line == 'n':
            return False
        else:
            print('y for yes/n for no')


def main_szcli(conf):
    in_history = []
    while True:
        in_line = szin(conf['cli_disp'])
        in_s = in_line.split(' ')
        if in_s[0] == 'exit':
            yn_v = yn()
            if yn_v:
                break
        else:
            run_szcli(in_s)


def run_szcli(in_s):
    act_list = conf['act_list']
    if not in_s[0] in act_list:
        if not len(in_s[0]) == 0:
            print('act',in_s[0],'not found')
    else:
        this_act = imp.load_source(in_s[0],in_s[0]+'.py')
        this_act.Foo(in_s[1:])


if __name__ == '__main__':
    with open('config.json', 'r') as f:
        conf = json.load(f)
    szout('welcome to szcli!')
    main_szcli(conf)
    szout('bye bye')