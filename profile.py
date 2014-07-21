import sys
import cProfile
import timeit
import parasite.views as views

def usage():
    print """\
python profile.py [-r] bibletext1 bibletext2 verse
    -r    run without profiling code, only show run time
"""

def main(args):
    do_profile = True
    
    if '-r' in args:
        do_profile = False
        args.remove('-r')
    if len(args) != 3:
        usage()
        sys.exit(1)

    statement= 'views.app.test_client().get("/compare/%s/%s/%s/")' % tuple(args)
    if do_profile:
        cProfile.run(statement)
    else:
        print timeit.timeit(statement, 'import parasite.views as views', number=1)

if __name__ == '__main__':
    main(sys.argv[1:])
