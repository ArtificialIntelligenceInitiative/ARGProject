def apple( x, y ):
    if( x + 5 == y ):
        print( x + y )
    elif( x > 100 ):
        print( y - x )
    else:
        apple( x + 2, y + 1 )

    print( "x is equal to " + str(x) )
    print( "y is equal to " + str(y) )