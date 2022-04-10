



def process_input():
    f = open("input.txt","r")
    memories = f.readline().split("\n")[0].split(" ")
    processes = f.readline().split("\n")[0].split(" ")
    f.close()
    return {
            "memories":memories,
            "processes":processes
            }
def process_output(filename,value):
    f = open(filename,"a")
    f.write(value)
    f.close()
def clear_outputfile(filename):
    f = open(filename, "w")
    f.write("")
    f.close()
def first_fit():
    data = process_input()
    processes = data["processes"]
    memories = data["memories"]
    filename = "firstfit.txt"
    clear_outputfile(filename)
    for process in processes:
        isFit = False
        for i in range(len(memories)):
            if(int(memories[i]) > int(process)):
                process_output(filename,str(i) + " ")
                memories[i] = str(int(memories[i]) - int(process))
                isFit = True
                break
        if isFit == False:
            process_output(filename, str(-1) + " ")      
    string = "\n" + " ".join(memories)
    process_output(filename,string)
    print("First-Fit done")
def best_fit():
    data = process_input()
    processes = data["processes"]
    memories = data["memories"]
    filename = "bestfit.txt"
    clear_outputfile(filename)
    for process in processes:
        min_memory = memories[0]
        index = -1
        for i in range(len(memories)):
            if int(memories[i]) > int(process) and int(memories[i]) <= int(min_memory):
                min_memory = memories[i]
                index = i
        if index != -1:
            process_output(filename,str(index) + " ")
            memories[index] = str(int(memories[index]) - int(process))
        else:
            process_output(filename, str(-1) + " ")
    string = "\n" + " ".join(memories)
    process_output(filename,string)
    print("Best-fit done")


def worst_fit():
    data = process_input()
    processes = data["processes"]
    memories = data["memories"]
    filename = "worst.txt"
    clear_outputfile(filename)
    for process in processes:
        max_memory = memories[0]
        index = -1
        for i in range(len(memories)):
            if int(memories[i]) > int(process) and int(memories[i]) >= int(max_memory):
                max_memory = memories[i]
                index = i
        if index != -1:
            process_output(filename,str(index) + " ")
            memories[index] = str(int(memories[index]) - int(process))
        else:
            process_output(filename, str(-1) + " ")
    string = "\n" + " ".join(memories)
    process_output(filename,string)
    print("Worst-fit done")

first_fit()
best_fit()
worst_fit()