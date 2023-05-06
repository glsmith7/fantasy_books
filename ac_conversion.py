def ac_convert(AC,AC_from='becmi', AC_to='acks'):

    ''' converts between D&D/AD&D/5E and ACKS styles of AC. Takes up to three:
    
    1st = AC (required)
    2nd = AC_from (starting AC) [defaults to BECMI]
    3rd = AC_to (goal AC) [defaults to ACKS]

    (capitalization does not matter, D&D and dnd--and all variations thereof--are all accepted)

    'becmi','dnd','basic','odnd','0dnd','b/x','holmes','moldvay' are [9 - (ACKS AC)]
    'adnd','adnd1','adnd2' are [10 - (ACKS AC)]
    'adnd3','adnd4','adnd5','dnd3','dnd3.5', 'dnd4', 'dnd5', '3e','3.5e','4e','5e' are [(ACKS AC) + 10]
    
    '''
    AC_from = AC_from.lower()
    AC_to = AC_to.lower()
    AC_from = AC_from.replace('d&d','dnd')

    def get_as_BECMI(AC,AC_from):
        ''' converts any AC type to BECMI as a "standard" form for later conversion '''
        if AC_from in ('becmi','dnd','basic','odnd','0dnd','b/x','holmes','moldvay'):
            return AC

        elif AC_from in ('adnd','adnd1','adnd2','2e','1e'):
            return (AC-1)
        
        elif AC_from in ('adnd3','adnd4','adnd5','dnd3','dnd3.5', 'dnd4', 'dnd5', '3e','3.5e','4e','5e'):
            return (9-AC+10)

        elif AC_from in ('acks'):
            return (9-AC)
        
        else:
            raise TypeError
    
    def convert_to_desired_AC(AC,AC_to):

        '''AC always comes in as BECMI style'''

        if AC_to in ('becmi','dnd','basic','odnd','0dnd','b/x','holmes','moldvay'):
            return AC

        elif AC_to in ('adnd','adnd1','adnd2','2e','1e'):
            return (AC+1)
        
        elif AC_to in ('adnd3','adnd4','adnd5','dnd3','dnd3.5', 'dnd4', 'dnd5', '3e','3.5e','4e','5e'):
            return (19-AC)

        elif AC_to in ('acks'):
            return (9-AC)
        
        else:
            raise TypeError

    becmi_standard_AC = get_as_BECMI(AC,AC_from)
    goal_AC = convert_to_desired_AC(becmi_standard_AC,AC_to)

    #print (becmi_standard_AC,goal_AC)
    return goal_AC
    
def attack_convert(attack,attack_from='THACO', attack_to='acks'):

    ''' converts between D&D/AD&D/5E and ACKS attacks. Takes up to three:
    
    1st = attack (required)
    2nd = attack_from [defaults to 'THACO']
    3rd = attack_to [defaults to 'acks' attack throws]

    (capitalization does not matter, D&D and dnd--and all variations thereof--are all accepted)

    'becmi','dnd','basic','odnd','0dnd','b/x','holmes','moldvay','adnd','adnd1','adnd2','THAC0' are all [THACO]
    'adnd3','adnd4','adnd5','dnd3','dnd3.5', 'dnd4', 'dnd5', '3e','3.5e','4e','5e' are [basic attack bonus]
    'acks','attack throw','attack_throw','attackthrow','throw','at' are [ACKS attack throw]
    
    '''
    attack_from = attack_from.lower()
    attack_from = attack_from.replace('d&d','dnd')

    attack_to = attack_to.lower()
    attack_to = attack_to.replace('d&d','dnd')

    def get_as_THACO (attack,attack_from):
        ''' converts any attack bonus type to BECMI THACO as a "standard" form for later conversion '''

        if attack_from in ('becmi','dnd','basic','odnd','0dnd','b/x','holmes','moldvay','adnd','adnd1','adnd2','thaco','thac0'):
            return attack

        elif attack_from in ('adnd3','adnd4','adnd5','dnd3','dnd3.5', 'dnd4', 'dnd5', '3e','3.5e','4e','5e'):
            return (-1*(attack-20))
        
        elif attack_from in ('acks','attack throw','attack_throw','attackthrow','throw','at'):
            return (attack+10)
        
        else:
            raise TypeError
    
    def convert_to_desired_attack (attack,attack_to):

        '''attack always comes in as THACO style'''

        if attack_to in ('becmi','dnd','basic','odnd','0dnd','b/x','holmes','moldvay','adnd','adnd1','adnd2','thaco','thac0'):
            return attack

        elif attack_to in ('adnd3','adnd4','adnd5','dnd3','dnd3.5', 'dnd4', 'dnd5', '3e','3.5e','4e','5e'):
            return (20-attack)
        
        elif attack_to in ('acks','attack throw','attack_throw','attackthrow','throw','at'):
            return (attack-10)
        
        else:
            raise TypeError

    THACO = get_as_THACO(attack,attack_from)
    attack_to_return = convert_to_desired_attack(THACO,attack_to)

    return attack_to_return