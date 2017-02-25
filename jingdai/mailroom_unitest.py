#!/usr/bin/env python

import mailroom

def test_1():
    donation=[("Andy","Thomas", 300),("Sally", "Bui", 400),("Andy","Tom", 100),("Tom","Colin", 700),("Lisa","Dodo",90),("Abby","Lust",1000),("Abby","Lust",200),("Abby","Lust",300)]
    assert mailroom.create_a_report(donation)==[('AndyThomas', 300, 1, 300.0), ('SallyBui', 400, 1, 400.0), ('AndyTom', 100, 1, 100.0), ('TomColin', 700, 1, 700.0), ('LisaDodo', 90, 1, 90.0), ('AbbyLust', 1500, 3, 500.0)]
