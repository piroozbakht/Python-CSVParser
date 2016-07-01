#! C:\Users\Monkey\AppData\Local\Programs\Python\Python35-32\

def main():
    file = open('csv file.csv')
    print(parser(file.read()))

def parser(data):
    parschar = 0
    parsline = 0
    br = False
    pars = []
    pars.append([''])
    qut = False
    datachar=0
    while (datachar < len(data)-1):
        if data[datachar] == ',' and (not qut):
            parschar+=1
            datachar+=1
            pars[parsline].extend([''])
        if qut and data[datachar] == '"':
            qut = False
            datachar+=1
            parschar+=1
            pars[parsline].extend([''])
        if (not qut) and data[datachar] == '"':
            if data[datachar + 1] == '"':
                datachar+=1
            else:
                qut = True
                parschar+=1
                datachar+=1
                pars[parsline].extend([''])
        if data[datachar] == '\n':
            br = True
        if not qut and br:
            parsline+=1
            parschar=0
            datachar += 1
            pars.append([''])
            br = False
        if qut and br:
            pars[parsline][parschar] = pars[parsline][parschar] + "\n"
        else:
            pars[parsline][parschar]=pars[parsline][parschar]+data[datachar]
        datachar+=1
    return(pars)

if __name__ == "__main__": main()
