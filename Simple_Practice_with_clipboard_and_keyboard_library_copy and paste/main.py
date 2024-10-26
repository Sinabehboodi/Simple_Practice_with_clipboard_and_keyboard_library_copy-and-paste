import keyboard
import clipboard
import time 
from my_stack import CStack 
from my_queue import CQueue


def greetings():
    print("Welcome to Clipboard Master ---> Version 1.0")


def get_memory_type():
    while True:
        try:
            memory_type = int(input("Please entre the memory type you want to use:\n1. Stack\n2. Queue\n3. File\n"))
            if memory_type == 1 or memory_type == 2 or memory_type == 3:
                if memory_type == 1:
                    memory = CStack()
                    memory_label = "Stack"
                    return memory, memory_label
                elif memory_type == 2:
                    memory = CQueue()
                    memory_label = "Queue"
                    return memory, memory_label
                elif memory_type == 3:
                    memory = CQueue()
                    memory_label = "File"
                    return memory, memory_label

            else:
                print("Invalid input, Please try again")
        except:
            continue


def get_text():
    global memory 
    global memory_label
    global pasting
    time.sleep(0.05)
    memory_handler(val=clipboard.paste())
    clipboard.copy(memory.atfront())
    pasting = False


def set_text():
    global memory 
    global memory_label
    global pasting
    if len(memory) == 0:
        clipboard.copy("")
    else:
        if not pasting:
            memory_handler()
            pasting = True
        clipboard.copy(memory_handler())


def get_file():
    while True:
        file_address = input("Please enter the file address:\n")
        try:
            file = open(file_address, 'r')
            break 
        except:
            print("Invalid file address, Please try again.")
    
    return file


def memory_handler(val=None):
    global memory 
    global memory_label
    global pasting
    if val is not None:
        if memory_label == "Stack":
            memory.push(val)
        else:
            memory.enqueue(val)
    else:
        if memory_label == "Stack":
            return memory.pop()
        else:
            return memory.dequeue()


if __name__ == '__main__':
    greetings()

    memory, memory_label = get_memory_type()

    if memory_label == 'File':
        file = get_file()
        print("You can now paste the next from the file into the clipboard.")
        for line in file:
            clipboard.copy(line)
            get_text()
        else:
            file.close()
    else:
        print(f"You are using {memory_label} type as your memory.")
        print("Monitoring the clipboard ...")

    pasting = False

    keyboard.add_hotkey('ctrl+c', get_text)
    keyboard.add_hotkey('ctrl+v', set_text)


    input("")