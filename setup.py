import os, sys, errno, getopt
def create_sub_folder(n,p,s):
    try:
        os.makedirs(p+'/'+n)
        print ' |-'+p+'/'+n,'has been created!'
        #Create Route
        route = '/'+n
        if route == '/main':
            route='/'
        with open(p+'/routing.js', "a") as routing:
            routing.write("Router.route('"+route+"',function(){\n")
            routing.write("\tthis.render('"+n+"');\n")
            routing.write("});\n")
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print ' |-'+p+'/'+n,'already exists!'
    #Create js file
    if not os.path.isfile(p+'/'+n+'/'+n+'.js'):
        with open(p+'/'+n+'/'+n+'.js', "a") as js_file:
            js_file.write("//"+n+'.js\n')
            js_file.write("Template."+n+".onRendered(function(){\n\t//Code\n});\n")
            js_file.write("Template."+n+".helpers({\n\t//Code\n});\n")
            js_file.write("Template."+n+".events({\n\t//Code\n});\n")

        print '  |-'+p+'/'+n+'/'+n+'.js','has been created!'
    else:
        print '  |-'+p+'/'+n+'/'+n+'.js','already exists!'
    #Create style file
    if not os.path.isfile(p+'/'+n+'/'+n+'.'+s):
        with open(p+'/'+n+'/'+n+'.'+s, "a") as style_file:
            style_file.write("//"+n+'.'+s+'\n')
        print '  |-'+p+'/'+n+'/'+n+'.'+s,'has been created!'
    else:
        print '  |-'+p+'/'+n+'/'+n+'.'+s,'already exists!'
    #Create html file
    if not os.path.isfile(p+'/'+n+'/'+n+'.html'):
        with open(p+'/'+n+'/'+n+'.html', "a") as html_file:
            html_file.write("<!--"+n+'.html-->\n')
            html_file.write('<template name="'+n+'">\n\tHello, World!\n</template>\n')
        print '  |-'+p+'/'+n+'/'+n+'.html','has been created!'
    else:
        print '  |-'+p+'/'+n+'/'+n+'.html','already exists!'

def create_main_folder(n,p,i,s):
    #create folder
    try:
        os.makedirs(p+'/'+n)
        print p+'/'+n,'has been created!'
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print p+'/'+n,'already exists!'
    #create sub folders
    create_sub_folder(n,p+'/'+n,s)
    if i >1:
        for x in xrange(1,i):
            create_sub_folder(n+'_'+str(x),p+'/'+n,s)

def main(argv):
    name = 'main'
    path = 'client'
    num_pages = 1
    style='scss'
    try:
        opts, args = getopt.getopt(argv,"hn:p:i:s:",["name=","path=","num_pages=","style="])
    except getopt.GetoptError:
        print 'setup.py -n <name> -p <path> -i <num_pages>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'setup.py -n <name> -p <path> -i <num_pages>'
            sys.exit()
        elif opt in ('-n','--name'):
            name=arg
        elif opt in ('-p','--path'):
            path=arg
        elif opt in ('-i','--num_pages'):
            num_pages=int(arg)
        elif opt in ('-s','--style'):
            style=arg
    if num_pages < 1:
        print 'Usage: setup.py -n <name> -p <path> -i <num_pages>'
        print '<num_pages> must be at least 1'
        sys.exit(2)
    create_main_folder(name,path,num_pages,style)

if __name__ == "__main__":
    main(sys.argv[1:])
