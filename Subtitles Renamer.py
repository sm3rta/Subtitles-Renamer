import os
print("This tool is developed by SMARTA!")
while True:
    folder=input("Please enter the full path to the folder containing both videos and subtitles\n")
    a=os.listdir(folder)

    ext1=a[0][-3:]
    ext2=a[1][-3:]
    sub_exts=["srt","ass","sub"]
    epi_exts=["mp4","mkv","avi","wmv","flv","m4v", "mpg"]

    subs, epis = [], []

    for item in a:
        ext=item[-3:]
        if ext in sub_exts:
            subs.append(item)
        elif ext in epi_exts:
            epis.append(item)
    #print(subs, epis)        

    if len(subs)==0 and len(epis)==0:
        print("There are no videos or subtitles!")
    elif len(subs)==0:
        print("There are no subtitles!")
    elif len(epis)==0:
        print("There are no videos!")
    elif len(subs)!=len(epis):
        print("The number of videos isn't equal to that of subtitles. Quitting.")
    else:
        index=0
        while index<len(epis):
            sub_ext=subs[index][-3:]
            print(subs[index], "->", epis[index][:-3]+sub_ext)
            
            os.rename(folder+"\\"+subs[index],folder+"\\"+epis[index][:-3]+sub_ext)
            index+=1

    input("Press Enter to give me another job!")
