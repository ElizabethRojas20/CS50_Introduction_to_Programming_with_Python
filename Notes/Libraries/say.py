import cowsay
import sys

if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
    #cowsay.trex("hello, " + sys.argv[1])
    #cowsay.ghostbusters("hello, " + sys.argv[1])
    cowsay.meow("hello, " + sys.argv[1])

#dir opens that file in VS Code to inspect everything defined there.
print(dir(cowsay))