ANON_DECREASE = 0.15

def calc_gbp(current_land, total_land_lost, num_days_ago, is_war):
    original_land = current_land + total_land_lost
    

def calc_pnf(target_nw, self_nw):
    relative_pnf = float(target_nw) / self_nw
    print "Relative PNF: %s" % relative_pnf
    if relative_pnf < 0.567:
        return 0
    elif 0.567 < relative_pnf and relative_pnf < 0.9:
        print "PNF mod: %s" % (3 * relative_pnf - 1.7)
        return 3 * relative_pnf - 1.7
    elif 0.9 < relative_pnf and relative_pnf < 1.1:
        return 1
    elif 1.1 < relative_pnf and relative_pnf < 1.6:
        return -2 * relative_pnf + 3.2
    else:
        return 0

def calc_knf(target_nw, self_nw):
    relative_knf = float(target_nw) / self_nw
    print "Relative KNF: %s" % relative_knf
    
    if relative_knf < 0.4:
        return 0.6666
    elif relative_knf >= 0.4 and relative_knf < 0.9:
        print "KNF mod: %s" % (relative_knf * (2/3) + 0.4)
        return relative_knf * (float(2)/3) + 0.4
    else:
        return 1

def calc_gains(resource_amount, attack_type_base, pnf, knf, gbp, gs, race, stance, relations, target_stance, attack_time_modifier, schools, anonymity):
    print "Resource amount: %s" % resource_amount
    gain = resource_amount * attack_type_base
    print "  attack type base (%s): %s" % (attack_type_base, gain)
    gain = gain * pnf
    print "  pnf (%s): %s" % (pnf, gain)
    gain = gain*knf
    print "  knf (%s): %s" % (knf, gain)
    gain = gain * gbp
    print "  gbp (%s): %s" % (gbp, gain)
    gain = gain * race
    print "  race (%s): %s" % (race, gain)
    gain = gain * stance
    print "  stance (%s): %s" % (stance, gain)
    gain = gain * relations
    print "  relations (%s): %s" % (relations, gain)
    gain = gain * target_stance
    print "  target_stance (%s): %s" % (target_stance, gain)
    gain = gain * attack_time_modifier
    print "  attack time modifier (%s): %s" % (attack_time_modifier, gain)
    gain = gain * gs
    print "  gs (%s): %s" % (gs, gain)
    gain = gain * schools
    print "  schools (%s): %s" % (schools, gain)
    gain = resource_amount * attack_type_base * pnf * knf * gbp * race * stance * relations * target_stance * attack_time_modifier * gs * schools
    # gain -= gain * gs
    # gain -= gain * schools
    if anonymity:
        gain = gain * (1 - ANON_DECREASE)
        print " anon (%s): %s" % (ANON_DECREASE, gain)
    
    return gain
    
def test_gains():
    resources = 738207
    attack_type_base = 0.09375
    self_nw = 406084
    target_nw = 334790
    target_kd_nw = 5268956
    self_kd_nw = 5754757
    gbp = 1
    gs = 1.0133
    # gs = 1
    race = 1
    stance = 1
    relations = 1
    target_stance = 0.5
    attack_time_modifier = 1
    schools = 1.464
    anon = False

    gains = calc_gains(resources, attack_type_base, calc_pnf(target_nw, self_nw), calc_knf(target_kd_nw, self_kd_nw), gbp, gs, race, stance, relations, target_stance, attack_time_modifier, schools, anon)
    print gains
    
# Your forces arrive at Xeripmav (6:2). A tough battle took place, but we have managed a victory! Your army stole 16,103 books of knowledge!
# We lost 97 soldiers, 39 Skeletons and 50 Ghouls in this battle.
# We killed about 585 enemy troops.
# Our forces will be available again in 14.37 days (on July 15 of YR6).

# Your forces arrive at Xeripmav (6:2). A tough battle took place, but we have managed a victory! Your army stole 14,399 books of knowledge!
# We lost 99 soldiers, 39 Skeletons and 46 Ghouls in this battle.
# We killed about 467 enemy troops.
# Our forces will be available again in 14.48 days (on July 15 of YR6).

def test_gains2():
    resources = 817107
    attack_type_base = 0.09375
    self_nw = 470519
    target_nw = 456677
    target_kd_nw = 6418133
    self_kd_nw = 6449160
    gbp = 0.7639
    gs = 1
    race = 1
    stance = 1
    relations = 1
    target_stance = 1
    attack_time_modifier = 1.125
    schools = 1
    anon = False
    gains = calc_gains(resources, attack_type_base, calc_pnf(target_nw, self_nw), calc_knf(target_kd_nw, self_kd_nw), gbp, gs, race, stance, relations, target_stance, attack_time_modifier, schools, anon)
    print gains
# Your forces arrive at Victor of M-N-Y (2:15). A tough battle took place, but we have managed a victory! Your army stole 65,832 books of knowledge!
# We lost 83 Skeletons and 193 Ghouls in this battle.
# We killed about 1,705 enemy troops.
# Our forces will be available again in 18.00 days (on March 2 of YR7).

def test_gains3():
    resources = 1391879
    attack_type_base = 0.09375
    self_nw = 460513
    target_nw = 487481
    target_kd_nw = 5766863 
    self_kd_nw = 6521388
    gbp = 1
    gs = 1
    race = 1
    stance = 0.5
    relations = 1
    target_stance = 1
    attack_time_modifier = 1
    schools = 1
    anon = False
    gains = calc_gains(resources, attack_type_base, calc_pnf(target_nw, self_nw), calc_knf(target_kd_nw, self_kd_nw), gbp, gs, race, stance, relations, target_stance, attack_time_modifier, schools, anon)
    print " Total gains: %s" % gains