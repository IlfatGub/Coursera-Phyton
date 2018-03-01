def gen_scories(infile):
    for line in infile:
        _, *points = line.rstrip().rsplit(None, 3)
        points = [int(x) for x in points]
        if any(x < 40 for x in points):
            continue
        yield sum(points)


with open("input.txt", "r",
          encoding="utf-8") as fin, open("output.txt", "w",
                                         encoding="utf-8") as fout:

    places = int(next(fin))
    scories = sorted(gen_scories(fin), reverse=True)

    if places >= len(scories):
        print(0, file=fout)
    else:
        max_score = scories[0]
        if places < len([x for x in scories if x == max_score]):
            print(1, file=fout)
        else:
            print(scories[places - 1], file=fout)
