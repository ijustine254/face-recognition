import sys
from pathlib import Path

in_img = None
out_img = None

#   Check whether arguments were passed
#   if yes whether:
#   i) argument 1 is a file
#   i) argument 2's folder exists
#       amd if it has a png extension
#       if the folder does not exit
#       asks the user for permission to create it
def check_args():
    global in_img, out_img
    if len(sys.argv) != 3:
        print("Usage:\nThe programe requires two arguments.")
        print("Input file and Output file respectively both paths to be absolute.")
        print("\n"+sys.argv[0], "[input file] [output file]")
        exit(1)
    in_img = sys.argv[1]
    out_img = sys.argv[2]
    invalid_ext = "Out put file should have png extension"
    if not Path(in_img).is_file():
        print("No such file")
        exit(1)
    if "png" != Path(out_img).suffix[1:]:
        print(invalid_ext)
        exit(1)
    folder = str(Path(out_img).parent)
    if not Path(folder).exists():
        print("Directory to write image to, does not exists.")
        create_dir = input("\nCreate Folder? [y/n] ")
        if "y" in create_dir.lower() or "yes" in create_dir.lower():
            Path(folder).mkdir()
        else:
            print("Sorry, I can't continue")
            exit(1)

check_args()    #   Run the function

#   I am import this modules here because
#   they are only needed if the check
#   completes successfully
#   and also face_recognition takes time and ram
#   no one wants to go through that when you not
#   sure if the arguments meet the requirement
from PIL import Image, ImageDraw
import face_recognition as fr

#   load the image
img = fr.load_image_file(in_img)
#   locate faces
faces_loc = fr.face_locations(img)


with Image.open(in_img) as im:
    for face_loc in faces_loc:
        draw = ImageDraw.Draw(im)
        #   face_loc returns a set inside a list
        #   using the set as is could not capture the face
        cood = list(face_loc)
        #   I sought to use a reversed list and it worked
        cood.reverse() 
        draw.rectangle(cood, outline=155, width=7)
    im.save(out_img, "png")


