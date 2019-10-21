from Bio.Seq import transcribe, translate, reverse_complement

RNA = input("Input DNA string: ")

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

print(max(allOrfs, key=len))
