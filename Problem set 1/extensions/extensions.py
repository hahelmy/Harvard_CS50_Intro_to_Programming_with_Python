# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
# A program that prompts the user for the name of a file and then outputs that file’s media type
def main():
    uInput = input("Please enter a file name to check it\'s media type: ").strip().lower()
    
    getExtension(uInput)

def getExtension(fileName):
    index = fileName.find(".")
    if index != -1:
        ext = fileName[index+1:]
        # print(ext)
        
        match ext:
            case "gif":
                print("image/gif")
            case "jpg" | "jpeg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _:
                print("application/octet-stream")
    else:
        print("application/octet-stream")

main()