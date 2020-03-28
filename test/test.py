"""
This script recreates the file data/boundary_conditions_backup.txt with all the correct information
it relies on all_boundary_options.txt

"""
# reads in all possible boundary conditions defined in all_boundary_options.txt
with open('all_boundary_options.txt', "r") as f:
    all_BC_options = [line.rstrip('\n') for line in f]
# reads through each option and writes it along with its reactions to data/boundary_conditions.txt
with open('../data/boundary_conditions.txt', 'w+') as f:
    for bc in all_BC_options:
        #print(bc)
        if bc.split(',')[2].lower() == 'underterminate':
            next(bc)
        elif bc.split(',')[2].lower() == 'determinate':
            if bc.split(',')[0].lower() == "roller":
                conditions1 = "Fy"
            elif bc.split(',')[0].lower() == "fixed":
                conditions1 = "Fx,Fy,Mz"
            elif bc.split(',')[0].lower() == "pinned":
                conditions1 = "Fx,Fy"
            elif bc.split(',')[0].lower() == "free":
                conditions1 = "no reactions"
            elif bc.split(',')[0].lower() == "simple":
                conditions1 = "Fy"
            if bc.split(',')[1].lower() == "roller":
                conditions2 = "Fy"
            elif bc.split(',')[1].lower() == "fixed":
                conditions2 = "Fx,Fy,Mz"
            elif bc.split(',')[1].lower() == "pinned":
                conditions2 = "Fx,Fy"
            elif bc.split(',')[1].lower() == "free":
                conditions2 = "no reactions"
            elif bc.split(',')[1].lower() == "simple":
                conditions2 = "Fy"
            f.writelines(f'{bc.split(",")[0]},{bc.split(",")[1]},["{conditions1}","{conditions2}"]\n')