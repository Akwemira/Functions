""" 
Create story.txt file and use copy() function to copy its contents to copy_story.txt

Args:
 use open() method with "w" option to create file and copy to file
 use "r" option to read from file
  Returns:
 copy_story.txt has same content as story.txt.
"""

story = open("story.txt", "w") # creates firstfile named story.txt
story.write("This is a story about Alice in WonderLand\n") # writing content to story.txt
story.write("Hope you enjoy reading this story\n")
story.write("The first chapter")

story.close() # closing file to save contents
def copy(source, destination):
    with open("story.txt", "r") as firstfile, open("copy_story.txt", "w") as secondfile: # read story.txt while creating copy_story.txt
        for line in firstfile: # reading line by line from story.txt
            secondfile.write(line) # copying or writing into copy_story.txt what was in story.txt

firstfile = "story.txt"
secondfile = "copy_story.txt"
copy(firstfile, secondfile)
