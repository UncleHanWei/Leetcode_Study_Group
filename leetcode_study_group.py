from random import shuffle
import leetcode_pick_one as po

def printGroup(the_group) :
    for i in [*the_group] :
        print(f"第 {i} 組:")
        print(*the_group[i]['member'], sep=' ')
        print('題目:')
        for k in [*the_group[i]['question']] :
            print(f"{k}: {the_group[i]['question'][k]}")
        print('==========\n')

def group(member, n) :
    shuffle(member)
    the_group = {}
    index = 0
    while member :
        the_group.setdefault(index%n+1, {}).setdefault('member', []).append(member.pop())
        if not the_group[index%n+1].get('question') :
            the_group[index%n+1]['question'] = po.main()
        index += 1
    printGroup(the_group)

def main() :
    with open('member.txt', 'r', encoding='utf8') as m :
        member = [l.strip() for l in m.readlines()]
    n = 3
    group(member, n)

if __name__ == '__main__' :
    main()