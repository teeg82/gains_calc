ANON_DECREASE = 0.15

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
        print "KNF mod: %s" % (relative_knf * (2/3) + 4)
        return relative_knf * (2/3) + 4
    else:
        return 1

def calc_gains(resource_amount, attack_type_base, pnf, knf, gbp, gs, race, stance, relations, target_stance, attack_time_modifer, schools, anonymity):
    gain = ((resource_amount * attack_type_base) * (pnf * knf * gbp * race * stance * relations * target_stance * attack_time_modifer)) / gs / schools
    # gain -= gain * gs
    # gain -= gain * schools
    if anonymity:
        gain = gain / (1 + ANON_DECREASE)
    
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
