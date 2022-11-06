#!/usr/bin/python3
# pip install pytruth

# TODO Any volunteer to implement unit tests? Many thanks in advance!

import os
import lib # TODO create lib.py containing the functions to be tested.

#from truth.truth import AssertThat

# Module under test
#from app.core.main import Application

def test_sanitize():
    i=17
    #AssertThat(i).IsEqualTo(17);
    #AssertThat("abc").IsEqualTo("abc");

    sanitize('a;b')

test_sanitize()
