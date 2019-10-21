from Bio.Seq import transcribe, translate, reverse_complement

inFile = open("files/eighteenIn", "r")
RNAlist = inFile.read().splitlines()

RNAlist = RNAlist[1:]

RNA = ""

for i in RNAlist:
    RNA += i

rfs = [translate(transcribe(RNA)), translate(transcribe(RNA[1:])), translate(transcribe(RNA[2:])),
       translate(transcribe(reverse_complement(RNA))), translate(transcribe(reverse_complement(RNA)[1:])),
       translate(transcribe(reverse_complement(RNA)[2:]))]

allOrfs = []
for rf in rfs:
    start = [i for i in range(len(rf)) if rf[i] == 'M']
    stop = [i for i in range(len(rf)) if rf[i] == '*']
    for str in start:
        for stp in stop:
            if str < stp and '*' not in rf[str:stp]:
                allOrfs.append(rf[str:stp])

file = open("files/eighteenRez", "w")

allOrfs = list(dict.fromkeys(allOrfs))

for i in allOrfs:
    file.write(i + "\n")
