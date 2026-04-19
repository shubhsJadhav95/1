process = [1,2,3,4,5]
co_ordinator = max(process)

print("Initial Co-ordinator is:",co_ordinator)

def election(p):
    print("process:",p,"Started Election")

    higher= [x for x in process if x>p]

    if not higher:
        print("process:",p,"Its an co-ordinator")
    else:
        print("process:",p,"send election to",higher)
        return max(higher)

#if co-ordiantor fails
process.remove(5)

new_co_ordinator = election(3)

print("new co-ordinator is:",new_co_ordinator)