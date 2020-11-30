import sys
from pathlib import Path

in_img = None
out_img = None


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

check_args()


from PIL import Image, ImageDraw
import face_recognition as fr

img = fr.load_image_file(in_img)
face_loc = fr.face_locations(img)
face_marks = fr.face_landmarks(img)


with Image.open(in_img) as im:
    draw = ImageDraw.Draw(im)
    cood = list(face_loc[0])
    cood.reverse() 
    draw.rectangle(cood, outline=155, width=7)
    im.save(out_img, "png")


