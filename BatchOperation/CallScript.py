import os
import subprocess
PERL_TOOLS_DIR="/ocs/ocsrun/r7code/perl/ocs_perl_tools"
SQL_TOOLS_DIR="/ocs/ocsrun/r7code/perl/do_sql"
SCRIPT_PATH={
    'UserQuery':os.path.join(PERL_TOOLS_DIR,'django_control/look_oam.pl -u {0} -t {1} -o {2} -d {3}'),
    'BatchOperation':os.path.join(SQL_TOOLS_DIR,'do_sql.pl -t {0} -s {1}')
}

def call_script(app,*args):
    
    if app=="UserQuery":
        output=subprocess.Popen(SCRIPT_PATH[app].format(args[0],args[1],args[2],args[3]),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    elif app=="BatchOperation":
        output=subprocess.Popen(SCRIPT_PATH[app].format(args[0],args[1]),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout=output.stdout.read().decode('GBK')
    stderr=output.stderr.read().decode('GBK')
    if stdout: 
        return stdout
    else:
        return stderr
if __name__=='__main__':
    output=call_script('UserQuery','13246484759','107','ocs') 
    print(output)
