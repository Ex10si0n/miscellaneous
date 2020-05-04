class Gate(object):

    def __init__(self, idf):
        self.idf = idf
        self.input_line = []
        self.output_line = None

    def modify(self, input_line):
        for node in input_line:
            for i in range(len(controller.nodes)):
                if node == controller.nodes[i].idf:
                    self.input_line.append(controller.nodes[i])
        

    def delete(self):
        pass

    def out(self):
        print(self.idf, ": ", self.output_line)

    def get(self):
        return self.output_line


class Node(object):

    def __init__(self, idf):
        self.idf = idf
        self.status = False

    def switch(self):
        if self.status is False:
            self.status = True
        else:
            self.status = False

    def set(self, truth):
        self.status = truth

    def get(self):
        return self.status

    def out(self):
        print(self.idf, ": ", self.status)


class AND(Gate):

    def getType(self):
        return "AND"

    def logi(self):
        if len(self.input_line) < 2:
            print(self.input_line)
            print("Error: Input Line(s) don't match with the needed")
        else:
            self.output_line = True
            for line in self.input_line:
                if line.get() is False:
                    self.output_line = False
                    break
            for i in range(len(controller.nodes)):
                if self.idf == controller.nodes[i].idf:
                    controller.nodes[i].status = self.output_line
                    break
            else:
                controller.nodes.append(Node(self.idf))
                controller.nodes[len(controller.nodes)-1].set(self.output_line)


class OR(Gate):

    def getType(self):
        return "OR"

    def logi(self):
        if len(self.input_line) < 2:
            print("Error: Input Line(s) don't match with the needed")
        else:
            self.output_line = False
            for line in self.input_line:
                if line.get() is True:
                    self.output_line = True
                    break
            for i in range(len(controller.nodes)):
                if self.idf == controller.nodes[i].idf:
                    controller.nodes[i].status = self.output_line
                    break
            else:
                controller.nodes.append(Node(self.idf))
                controller.nodes[len(controller.nodes)-1].set(self.output_line)


class XOR(Gate):

    def getType(self):
        return "XOR"

    def logi(self):
        if len(self.input_line) < 2:
            print("Error: Input Line(s) don't match with the needed")
        else:
            adder = 0
            for line in self.input_line:
                if line.get() is True:
                    adder += 1
            if adder % 2 == 1:
                self.output_line = True
            else:
                self.output_line = False
            for i in range(len(controller.nodes)):
                if self.idf == controller.nodes[i].idf:
                    controller.nodes[i].status = self.output_line
                    break
            else:
                controller.nodes.append(Node(self.idf))
                controller.nodes[len(controller.nodes)-1].set(self.output_line)

class NOT(Gate):

    def getType(self):
        return "NOT"

    def transform(self, input_line):
        if input_line is True:
            return False
        else:
            return True

    def logi(self):
        if len(self.input_line) != 1:
            print("Error: Input Lines don't match with the needed")
        else:
            self.output_line = self.transform(self.input_line[0].get())
        for i in range(len(controller.nodes)):
            if self.idf == controller.nodes[i].idf:
                controller.nodes[i].status = self.output_line
                break
        else:
            controller.nodes.append(Node(self.idf))
            controller.nodes[len(controller.nodes)-1].set(self.output_line)


class Controller(object):

    def __init__(self):
        self.instr = 1
        self.gates = []
        self.nodes = []


    def callError(self, type):
        if type == "Boolean Value Error":
            print("Error: Boolean Value Error")

        if type == "idf Not Found":
            print("Error: Identifier Not Found")


    def getInputs(self, say):
        for i in range(len(say)):
            if say[i] == ',':
                say = say[:i] + ' ' + say[i+1:]
        return say


    def interact(self):
        print("[", self.instr, "]: ", end='')
        say = input()

        ''' End situation'''
        if say == 'exit':
            return 0

        ''' Preprocess the say string '''
        for i in range(len(say)):
            if say[i] == ',' and say[i+1] == ' ':
                isay = ""
                for j in range(0, len(say)):
                    if j != i+1:
                        isay = isay + say[j]

        self.instr += 1
        say = say.split()

        ''' Apply for a new Gate/Node '''
        if say[0] == "new":
            self.new(say[1], say[2], say[3])

        ''' Modify Exists Gate/Node '''
        if say[0] == "mod":
            self.mod(say[1], say[2], say[3])


    def new(self, cate, idf, val):
        if cate == "node":
            self.nodes.append(Node(idf))
            if val == "True" or val == "1" or val == "T":
                self.nodes[len(self.nodes)-1].set(True)
            elif val == "False" or val == "0" or val == "F":
                self.nodes[len(self.nodes)-1].set(False)
            else:
                self.callError("Boolean Value Error")

        else:
            ins = self.getInputs(val)

            if cate == "and":
                self.gates.append(AND(idf))
            if cate == "xor":
                self.gates.append(XOR(idf))
            if cate == "or":
                self.gates.append(OR(idf))
            if cate == "not":
                self.gates.append(NOT(idf))

            self.gates[len(self.gates)-1].modify(ins)
            self.gates[len(self.gates)-1].logi()


    def mod(self, cate, idf, val):
        if cate == "node":
            for i in range(len(self.nodes)):
                if self.nodes[i].idf == idf:
                    if val == "True" or val == "1" or val == "T":
                        self.nodes[i].set(True)
                    elif val == "False" or val == "0" or val == "F":
                        self.nodes[i].set(False)
                    else:
                        self.callError("Boolean Value Error")
                    break
            else:
                self.callError("idf Not Found")
            for gate in self.gates:
                gate.logi()

        if cate == "gate":
            ins = self.getInputs(val)
            for i in range(len(self.gates)):
                if self.gates[i].idf == idf:
                    self.gates[i].modify(ins)
                    break
            else:
                self.callError("idf Not Found")
            for gate in self.gates:
                gate.logi()




controller = Controller()
while True:
    ret = controller.interact()
    for node in controller.nodes:
        node.out()
    if ret == 0:
        break


