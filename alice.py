def write_story():
    '''
This function creates a text file and writes to it
Argument: None
Return: none

'''
    with open("story.txt", "w") as file:# creates firstfile named story.txt
        file.write("This is a story about Alice in WonderLand\n") # writing content to story.txt
        file.write("Hope you enjoy reading this story\n")
        file.write("The first chapter")
        


def copy_story():
    '''
This function reads from a text file and writes its content to a new file
Arguments: None
Return: none

'''
    with open("story.txt", "r") as firstfile, open("copy_story.txt", "w") as secondfile: # read story.txt while creating copy_story.txt
        for line in firstfile: # reading line by line from story.txt
            secondfile.write(line) # copying or writing into copy_story.txt what was in story.txt
            


if __name__ == '__main__':


    write_story()

    copy_story()
