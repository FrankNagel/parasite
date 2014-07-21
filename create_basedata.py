import sys
import os
import cProfile
import timeit
import parasite.views as views

destdir = 'basedata'

def usage():
    print """\
python create_basedata.py bibletext1 bibletext2 verse
"""

def main(args):
    args = tuple(args)
    
    if len(args) != 3:
        usage()
        sys.exit(1)

    url = '/compare/%s/%s/%s/' % args
    global result
    result = views.app.test_client().get(url)
    if result.status_code != 200:
        print result
        sys.exit(1)
    if not os.access(destdir, os.F_OK):
        os.mkdir(destdir)
    with open(os.path.join(destdir, '%s_%s_%s' % args), 'w') as fp:
        fp.write(result.get_data())
    
    
if __name__ == '__main__':
    main(sys.argv[1:])
