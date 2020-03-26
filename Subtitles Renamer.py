import os
from time import sleep
from shutil import rmtree, copy2
# print("This tool is developed by Smarta")  #A bit cheesy

sub_exts = ['aqt',
            '.ass',
            '.gsub',
            '.jss',
            '.pjs',
            '.psb',
            '.rt',
            '.sbv',
            '.smi',
            '.srt',
            '.srt',
            '.ssa',
            '.ssf',
            '.stl',
            '.sub',
            '.ttxt',
            '.usf']
epi_exts = ['3g2',
            '.3gp',
            '.avi',
            '.amv',
            '.asf',
            '.drc',
            '.f4a',
            '.f4b',
            '.f4p',
            '.f4v',
            '.flv',
            '.gif',
            '.gifv',
            '.m2v',
            '.m4p',
            '.m4v',
            '.mkv',
            '.mng',
            '.mov',
            '.mp2',
            '.mp4',
            '.mpe',
            '.mpeg',
            '.mpg',
            '.mpv',
            '.mxf',
            '.mxf',
            '.nsv',
            '.ogg',
            '.ogv',
            '.qt',
            '.rm',
            '.rmvb',
            '.roq',
            '.roq',
            '.svi',
            '.vob',
            '.webm',
            '.wmv',
            '.yuv']


def undo(changes):
    for pair in changes:
        os.rename(pair[1], pair[0])


folder = input(
    "Please enter the full path to the folder containing both episodes and subtitles\n")
files = os.listdir(folder)

subs, epis = [], []

for file in files:
    _, ext = os.path.splitext(file)
    if ext.lower() in sub_exts:
        subs.append(file)
    elif ext.lower() in epi_exts:
        epis.append(file)

if len(subs) == 0 and len(epis) == 0:
    print("Neither videos nor subtitles were found in this folder!")
elif len(subs) == 0:
    print("There are no subtitles!")
elif len(epis) == 0:
    print("There are no videos!")
elif len(subs) != len(epis):
    print("The number of videos isn't equal to that of subtitles.")
else:
    # ask
    choice = input(
        "Type V to rename episodes to subtitles or S (or anything) to rename subtitles to episodes: ")
    index = 0
    changes = []
    try:
        # taking a backup first
        print("Taking a backup of subtitles")
        if "subtitles backup" in os.listdir(folder):
            rmtree(os.path.join(folder, "subtitles backup"))
            sleep(1)
        os.makedirs(os.path.join(folder, "subtitles backup"))
        for sub in subs:
            copy2(os.path.join(folder, sub), os.path.join(
                folder, "subtitles backup"))

        if choice.lower() != 'v':
            # rename subs
            while index < len(epis):
                _, sub_ext = os.path.splitext(subs[index])
                epi_name, _ = os.path.splitext(epis[index])
                print(
                    '{0: <{maxLength}} -> {1}'.format(subs[index], epi_name+sub_ext, maxLength=len(max(subs, key=len))))
                os.rename(folder+"\\"+subs[index],
                          folder+"\\"+epi_name+sub_ext)
                changes.append(
                    (folder+"\\"+subs[index], folder+"\\"+epi_name+sub_ext))
                index += 1
        else:
            # rename episodes
            while index < len(epis):
                _, epi_ext = os.path.splitext(epis[index])
                sub_name, _ = os.path.splitext(subs[index])
                print(
                    '{0: <{maxLength}} -> {1}'.format(epis[index], sub_name+epi_ext, maxLength=len(max(epis, key=len))))
                os.rename(folder+"\\"+epis[index],
                          folder+"\\"+sub_name+epi_ext)
                changes.append(
                    (folder+"\\"+epis[index], folder+"\\"+sub_name+epi_ext))
                index += 1
        choice = input(
            "Press Y to undo (e.g. if the renaming process wasn't correct) or Enter to exit: ")
        if choice.lower() == 'y':
            undo(changes)

    except:
        # undo
        print("An error occured. Most likely some files are already in use. Close any programs that might be using any video file or subtitle file and try again.\nUndoing changes now...\n")
        undo(changes)
        input("Done. Press Enter to exit")  # keep window open
