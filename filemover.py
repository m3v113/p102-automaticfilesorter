import os
import shutil

# this is where the files are located and where they will be moved from
# set this as your downloads folder (if you want to organize your downloads folder)
# otherwise, you can do any folder you want to organize
sourcepath = "/Users/mehvishbondre/Desktop/holypickles"

# this is the new folder where the files will be moved and sorted
# you can make this a completely empty folder
destinationpath = "/Users/mehvishbondre/Desktop/holymangoes"

# this saves all the files in the source path folder as a list
filelist = os.listdir(sourcepath)

# printing the file list
print(filelist)

# for every file in the list of files, do the following
for file in filelist:

    # for every file name (in the list) the string is split into name and extension
    name, extension = os.path.splitext(file)

    # if the extension is blank, that means that we are dealing with a folder, and we ignore it
    if extension == "":
        continue

    # however, if the extension is any of the following, we create three variables
    elif extension in (".png", ".jpg", ".jpeg", ".heic", ".jfif", ".gif", ".webp"):

        # this variable is the path of the file
        currentpath = sourcepath + "/" + file

        # this variable is the path of the folder that we plan to move the file to
        futurefolder = destinationpath + "/images"

        # this variable is the final path of the file, where it will reside
        futurepath = destinationpath + "/images/" + file

        # if the futurefolder path exists, so the folder has been created, than we will
        # print the name of the file that we are moving and move the file from where it currently is
        # (currentpath) to its final destination (futurepath)
        if os.path.exists(futurefolder):
            print("...moving", file, "...")
            shutil.move(currentpath, futurepath)

        # if the path does not exist, meaning it has not been created, we will create the path
        # and then continue to print that we are moving the file and move the files
        else:
            os.makedirs(futurefolder)
            print("...moving", file, "...")
            shutil.move(currentpath, futurepath)

    # we repeat the same process (as above) for other extension types
    elif extension in (".pdf", ".docx", ".py"):

        currentpath = sourcepath + "/" + file

        futurefolder = destinationpath + "/documents"

        futurepath = destinationpath + "/documents/" + file

        if os.path.exists(futurefolder):
            print("...moving", file, "...")
            shutil.move(currentpath, futurepath)

        else:
            os.makedirs(futurefolder)
            print("...moving", file, "...")
            shutil.move(currentpath, futurepath)

    else:

        currentpath = sourcepath + "/" + file

        futurefolder = destinationpath + "/other"

        futurepath = destinationpath + "/other/" + file

        if os.path.exists(futurefolder):
            print("...moving", file, "...")
            shutil.move(currentpath, futurepath)

        else:
            os.makedirs(futurefolder)
            print("...moving", file, "...")
            shutil.move(currentpath, futurepath)
