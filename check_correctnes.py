import sys
import os
import time
import parasite.views as views

destdir = 'basedata'

def main(args):
    filenames = os.listdir(destdir)
    filenames.sort()

    count = 0
    success = 0
    for name in filenames:
        count += 1
        args = tuple(name.split('_'))
        print args

        url = '/compare/%s/%s/%s/' % args

        start = time.time()
        result = views.app.test_client().get(url)
        print time.time()-start
        if result.status_code != 200:
            print result
            continue
        with open(os.path.join(destdir, '%s_%s_%s' % args)) as fp:
            ref = fp.read()
            if ref != result.get_data():
                print 'Fail:', args
                with open('%s_%s_%s' % args, 'w') as fp2:
                    fp2.write(result.get_data())
                continue
        success += 1
    print 'success rate: %i/%i' % (success, count)
    
    
if __name__ == '__main__':
    main(sys.argv[1:])
