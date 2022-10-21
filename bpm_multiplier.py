filename = input("enter filename:\n")
multiplier = float(input("enter multiplier (2 or 0.5 usually):\n"))
gsv_str = "SliderMultiplier:"
tmp_str = "[TimingPoints]"
data = ''

def change_sv (tstr):
    tstr = tstr.replace(gsv_str,"")
    sv = float(tstr) / multiplier
    tstr = gsv_str+str(sv)+"\n"
    return tstr

def change_bpm (tline):
    tlinedata = tline.split(",")
    if (tlinedata[6]=="1"):
        bpm = float (tlinedata[1]) / multiplier
        tlinedata[1] = str(bpm)

    tline = ""
    for word in tlinedata:
        tline += word + ","

    return tline[0:len(tline)-1]

with open(filename,"r") as dotosu:
    in_timing_points = False
    for line in dotosu:
        if (line.find(gsv_str) != -1):
            line = change_sv(line)
        elif (line.find(tmp_str) != -1):
            in_timing_points = True
        else :
            if (in_timing_points):
                if (line == "\n"):
                    in_timing_points = False
                else :
                    line = change_bpm(line)
        data+=line
print ("\ndone, don't forget to adjust slider tick rate value")

with open(filename,"w") as resfile:
    resfile.write(data)


