def make_menu(menu_items, tb_border = '-', s_border = '|', space = 1, numbered = False):
    '''
    a function for printing menus:
    example of this output is:
    ------------
    | thanks   |
    | for      |
    | using    |
    | this     |
    ------------

    this can be achieved by running this command:
    make_menu(['thanks', 'for', 'using', 'this'])

    I MaskedTitan would like to thank you for using this module in your work
    '''
    
    width = len(max(menu_items, key = len))
    print(str(tb_border)*round((int(width)+4+space)/len(tb_border)+1))
    for i in menu_items:
        iteration = 0
        additional = 1+(width-(len(i)+(len(iteration)+3)))+space
        line = s_border+' '+i
        line = s_border+' '+i
        while True:
            line = line+' '
            iteration = iteration + 1
            if iteration == additional:
                line = line +' '+s_border 
                break
        print(line)
    print(str(tb_border)*round((int(width)+4+space)/len(tb_border)+1))
