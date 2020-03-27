# copy the if statements and changes a. to boundary_conditions[0].


i = 1
for a in [["roller",'fixed'],["roller",'pinned'],["roller",'simple'],["roller",'free'],
          ["fixed",'roller'],["pinned",'roller'],['simple',"roller"],['free','roller'],
          ['fixed','pinned'],['fixed','simple'],['fixed','free'],
          ['pinned','fixed'],['simple','fixed'],['free','fixed'],
          ['pinned','simple'],['pinned','free'],
          ['simple','pinned'],['free','pinned'],
          ['simple', 'free'],
          ['free','simple'],
          ['roller','roller'],['pinned','pinned'],['free','free'],['fixed','fixed'],['simple','simple']]:

    print(f'{i}.) {a}')
    i = i+1




    '''
    if a.lower() == 'fixed' and :
        start_string = (f"//|\n"
                        f"//|\n"
                        f"//|\n")
    elif a.lower() == 'free':
        start_string = (f"\n"
                        f"\n"
                        f"\n")
    elif a.lower() == 'simple':
        start_string = (f"   "
                        f"  /\ \n"
                        f" /  \ \n"
                        f"/_ _ \ \n")
    '''