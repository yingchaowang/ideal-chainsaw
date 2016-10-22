from requests import get
def thing():
    try:
        print "we trying"
        get('http87://ihdkjfiajoiwefioajeoifja.com/this_isnt_a_thing')
        raise "oops"
    except:
        print "are we here??"
        thing()
