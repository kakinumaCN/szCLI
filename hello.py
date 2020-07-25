import imp
import szcli

def Foo(args):
    # sz_main = imp.load_source('szcli','szcli.py')
    if len(args) == 0:
        szcli.szout("Hello world!")
    else:
        szcli.szout(args[0])