original = []
changes = []
for i in xrange(int(raw_input())):

    nick, new_nick = raw_input().split()
    
    if nick not in original and nick not in changes:
        original.append(nick)
        changes.append(new_nick)

    elif nick in changes and new_nick not in changes:
        n = changes.index(nick)
        changes[n] = new_nick

print len(original)
for j in xrange(len(original)):
    print original[j],changes[j]
