# GEO3 Maple to Python converter
# cd ../Google\ Drive/My\ Drive/Sync/DTU/Kurser/Differntialgeometri\ og\ Parametrisk\ design\ -\ 01237/GEO3Py;  

import re

class GEO3Function:
    def __init__(self, name, params, description, locals, globals, codeStr):
        self.name = name
        self.params = params
        self.description = description
        self.locals = locals
        self.globals = globals
        self.codeStr = codeStr
    
    def convertCode(self):
        codeStr = self.codeStr
        params = self.params



def readFile(filePath):
    f = open(filePath, "r")

    count = 0
    funcStrList = []

    while f:
        line = f.readline()
        if line == '':
            break
        if line.startswith("GEO3[") :#and "proc(" in line:
            count += 1
            funcStr = [line]
            while f:
                line = f.readline()
                # if line == '':
                #     break
                funcStr.append(line)
                # if "end:" in line:
                if line.startswith("end:"):
                    break
            funcStrList.append(funcStr)
    #print("Count,", count)
    #print("Sizeof funcStrList", len(funcStrList))
    f.close()
    return funcStrList

def makeFunction(funcStr):
    defLine = funcStr[0]
    assert defLine.startswith("GEO3["), "Line did not pass start assertion: " + defLine
    assert defLine.endswith(')\n'), "Line did not pass end assertion: " + defLine
    endLine = funcStr[-1]
    assert endLine == "end:\n", "End line assertion failed"

    str = ''.join(funcStr)

    # Strings to remove from code string
    trimStrings = []

    # Find func name
    s, start, end = defLine, "GEO3[", "]:="
    name = s[s.find(start)+len(start):s.rfind(end)]
    trimStrings.append(defLine)
    trimStrings.append(endLine)

    # Find func params
    s, start, end = defLine, "GEO3[" + name + "]:= proc(", ")\n"
    params = s[s.find(start)+len(start):s.rfind(end)]
    #print(name + '('+ params +')')

    # Find func description
    result = re.search('description "([\S\s]+)";', str)
    if result:
        description = result.group(1)
        trimStrings.append(result.group())
        #descriptionCount += 1
    else: description = None

    # Find func locals
    result = re.search('local([\S\s\n]*?);' , str)
    if result:
        locals = result.group(1)
        trimStrings.append(result.group())
        #localCount += 1
        #print("Locals:", locals)
    else: locals = None

    # Find globals
    result = re.search('global([\S\s\n]*?);' , str)
    if result:
        globals = result.group(1)
        trimStrings.append(result.group())
        #globalsCount += 1
        #print("Globals:", globals)
    else: globals = None

    # Find option
    result = re.search('option([\S\s\n]*?);' , str)
    if result:
        options = result.group(1)
        trimStrings.append(result.group())
        #optionsCount += 1
        #print("Options:", options)
    else: options = None

    # Code string
    codeStr = str
    for r in trimStrings:
        codeStr = codeStr.replace(r, '')
    
    return GEO3Function(name, params, description, locals, globals, codeStr)

def makeFuncFile(path, func):
    filename = path +  func.name + ".py"
    f = open(filename, "w") # File options, w, x

    # Header
    f.write("# GEO3, Python port\n")
    f.write("# " + func.name + "\n")
    f.write("# " + filename + "\n")
    f.write("\n\n")
    
    # Description
    f.write("# " + (func.description or '') + "\n")
    f.write("# Globals: " + (func.globals or '') + "\n")
    f.write("# Locals: " + (func.locals or '') + "\n")
    f.write("# Parameters: " + (func.params or '') + "\n")

    # Function body
    f.write("def " + func.name + '('+ (func.params or '') +'):' + "\n")
    
    codeStr = (func.codeStr or '')
    #result = re.search("if([\s\S\n]*)then([\s\S\n]*)else([\s\S\n]*)end if", codeStr)
    #result.group(1)
    codeStr = codeStr.replace("\n", "\n\t")
    f.write("\t" + codeStr + "\n")

    # Close file
    f.close()

def run():
    descriptionCount, localCount, globalsCount, optionsCount = 0, 0, 0, 0

    funcStrList = readFile("GEO3.txt")
    #funcStrList = [funcStrList[22], funcStrList[25]] # Only run for one function for quicker development

    print("Description count:", descriptionCount)
    print("Local count:", localCount)
    print("Globals count:", globalsCount)
    print("Options count:", optionsCount)

    # Make function dictionary
    funcDict = {}
    for funcStr in funcStrList:
        func = makeFunction(funcStr)
        funcDict[func.name] = func

    print("Function dictionary size:", len(funcDict))

    # Find deprecated
    # Propagate deprecation to functions which reference deprecated functions
    deprecatedPreDef = {"base2d", "base3d", "base3dPlus"} # Predefined things to look for
    deprecated = set() # Functions that get marked deprecated
    def checkDeprecate(i = 0):
        didDeprecate = False
        for func in funcDict:
            if func in deprecated: continue
            for dep in deprecated.union(deprecatedPreDef):
                if re.search(dep, funcDict[func].codeStr) or dep == func:
                    deprecated.add(func)
                    didDeprecate = True
                    break
        if(didDeprecate):
            i = 1 + checkDeprecate(i)
        return i

    print("Deprecation rounds:", checkDeprecate())

    # Mark deprecated
    for name in deprecated:
        dep_name = "deprecated_" + name
        try:
            funcDict[dep_name] = funcDict.pop(name)
            funcDict[dep_name].name = dep_name
        except:
            print("Trying to mark {} as deprecated failed. Didn't exist.".format(name))

    # Make files
    print("Making files...")
    for func in funcDict.values():
        print(func.name)
        makeFuncFile("functions/", func)
    print("Done making", len(funcDict), "files."
        , "{}/{} are marked as deprecated.".format(len(deprecated), len(funcDict)))

##### Run #####
run()
