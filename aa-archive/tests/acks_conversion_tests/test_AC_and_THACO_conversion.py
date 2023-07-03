import sys
import pytest
sys.path.append('../') # to see parallel folders for module import

import ac_conversion as ac
import tests.test_settings_GLS as s

def test_AC_conversion_routine():

    test_acks_values = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    test_becmi_values = (9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11)
    test_adnd_values = (10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10)

    for i in range (0,len(test_acks_values)):
        # check ACKS to itself and the other two
        assert ac.ac_convert(test_acks_values[i],'acks','acks') == test_acks_values[i]
        assert ac.ac_convert(test_acks_values[i],'acks','becmi') == test_becmi_values[i]
        assert ac.ac_convert(test_acks_values[i],'acks','adnd') == test_adnd_values[i]
            
    for i in range (0,len(test_becmi_values)):
        assert ac.ac_convert(test_becmi_values[i],'becmi','becmi') == test_becmi_values[i]
        assert ac.ac_convert(test_becmi_values[i],'becmi','adnd') == test_adnd_values[i]
        assert ac.ac_convert(test_becmi_values[i],'becmi','acks') == test_acks_values[i]

    for i in range (0,len(test_adnd_values)):
        assert ac.ac_convert(test_adnd_values[i],'adnd','adnd') == test_adnd_values[i]
        assert ac.ac_convert(test_adnd_values[i],'adnd','becmi') == test_becmi_values[i]
        assert ac.ac_convert(test_adnd_values[i],'adnd','acks') == test_acks_values[i]

def test_attack_bonus_attack_throw_conversion():

    test_acks_values = (10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9)
    test_3e_BAB = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
    test_THACO = (20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1)

    for i in range (0,len(test_acks_values)):
        # check ACKS to itself and the other two
        assert ac.attack_convert(test_acks_values[i],'acks','acks') == test_acks_values[i]
        assert ac.attack_convert(test_acks_values[i],'acks','3e') == test_3e_BAB[i]
        assert ac.attack_convert(test_acks_values[i],'acks','thaco') == test_THACO[i]
            
    for i in range (0,len(test_3e_BAB)):
        # 3rd edition basic attack bonus (BAB) versus itself and others
        assert ac.attack_convert(test_3e_BAB[i],'3e','3e') == test_3e_BAB[i]
        assert ac.attack_convert(test_3e_BAB[i],'3e','thaco') == test_THACO[i]
        assert ac.attack_convert(test_3e_BAB[i],'3e','acks') == test_acks_values[i]

    for i in range (0,len(test_THACO)):
        # THACO versus self and others
        assert ac.attack_convert(test_THACO[i],'thaco','thaco') == test_THACO[i]
        assert ac.attack_convert(test_THACO[i],'thaco','3e') == test_3e_BAB[i]
        assert ac.attack_convert(test_THACO[i],'thaco','acks') == test_acks_values[i]