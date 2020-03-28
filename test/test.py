"""
This script recreates the file data/boundary_conditions_backup.txt with all the correct information
"""
i = 1
a = ""

with open('test/all_boundary_options.txt'
          '', "r") as f:
    all_BC_options = [line.rstrip('\n') for line in f]

with open("data/boundary_conditions_backup.txt", "w+") as f:
    for a in [["roller",'fixed'],["roller",'pinned'],["roller",'simple'],["roller",'free'],
              ["fixed",'roller'],["pinned",'roller'],['simple',"roller"],['free','roller'],
              ['fixed','pinned'],['fixed','simple'],['fixed','free'],
              ['pinned','fixed'],['simple','fixed'],['free','fixed'],
              ['pinned','simple'],['pinned','free'],
              ['simple','pinned'],['free','pinned'],
              ['simple', 'free'],
              ['free','simple'],
              ['roller','roller'],['pinned','pinned'],['free','free'],['fixed','fixed'],['simple','simple']]:
        print(a)
        ans = input("is this a possible combination: ")
        if ans.lower() == "no":
            next
        elif ans.lower() == 'yes':
            if a[0].lower() == "roller":
                conditions1 = "Fy"
            elif a[0].lower() == "fixed":
                conditions1 = "Fx,Fy,Mz"
            elif a[0].lower() == "pinned":
                conditions1 = "Fx,Fy"
            elif a[0].lower() == "free":
                conditions1 = "no reactions"
            elif a[0].lower() == "simple":
                conditions1 = "Fy"
            if a[1].lower() == "roller":
                conditions2 = "Fy"
            elif a[1].lower() == "fixed":
                conditions2 = "Fx,Fy,Mz"
            elif a[1].lower() == "pinned":
                conditions2 = "Fx,Fy"
            elif a[1].lower() == "free":
                conditions2 = "no reactions"
            elif a[1].lower() == "simple":
                conditions2 = "Fy"
            f.writelines(f'{a},["{conditions1}","{conditions2}"]\n')
        i = i+1

