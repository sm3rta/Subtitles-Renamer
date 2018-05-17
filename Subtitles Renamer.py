import os
from time import sleep
from shutil import rmtree, copy2
#print("This tool is developed by Smarta")  #A bit cheesy

sub_exts=['aqt',
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
epi_exts=['3g2',
         '.3gp',
         '.abi',
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


while True:
    folder=input("Please enter the full path to the folder containing both videos and subtitles\n")
    files=os.listdir(folder)

    subs, epis = [], []

    for file in files:
        _, ext = os.path.splitext(file)
        if ext in sub_exts:
            subs.append(file)
        elif ext in epi_exts:
            epis.append(file)

    if len(subs)==0 and len(epis)==0:
        print("There are no videos or subtitles!")
    elif len(subs)==0:
        print("There are no subtitles!")
    elif len(epis)==0:
        print("There are no videos!")
    elif len(subs)!=len(epis):
        print("The number of videos isn't equal to that of subtitles.")
    else:
        #taking a backup first
        if "subtitles backup" in os.listdir(folder):
            rmtree(os.path.join(folder, "subtitles backup"))
            sleep(1)
        os.makedirs(os.path.join(folder, "subtitles backup"))
        for sub in subs:
            copy2(os.path.join(folder, sub), os.path.join(folder, "subtitles backup"))
            
        #rename subs
        index=0
        while index<len(epis):
            _, sub_ext = os.path.splitext(subs[index])
            epi_name, _ = os.path.splitext(epis[index])
            print(subs[index], "->", epi_name+sub_ext)
            
            os.rename(folder+"\\"+subs[index],folder+"\\"+epi_name+sub_ext)
            index+=1
    input("Press Enter to give me another job!")
