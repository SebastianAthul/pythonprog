class Vscode:
    def compile(self):
        print("compiling using vscode")
    def excecute(self):
        print("excecute using vscode")
    def debug(self):
        print("debug using vscode")
class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def excecute(self):
        print("excecute using pycharm")
    def debug(self):
        print("debug using pycharm")
class Programmer:
    def coding(self,ide):
        ide.coding()
        ide.excecute()
        ide.debug()
dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)