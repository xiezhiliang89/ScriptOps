import os
import subprocess
PERL_TOOLS_DIR="/ocs/ocsrun/r7code/perl/ocs_perl_tools"
SCRIPT_PATH={
    'UserQuery':os.path.join(PERL_TOOLS_DIR,'django_control/look_oam.pl -u {0} -t {1} -o {2} -d {3}'),
}

def call_script(app,msisdn,callType,target,date=None):
    output=subprocess.Popen(SCRIPT_PATH[app].format(msisdn,target,callType,date),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout=output.stdout.read().decode('GBK')
    stderr=output.stderr.read().decode('GBK')
    if stdout: 
        return stdout
    else:
        return stderr
if __name__=='__main__':
    output=call_script('UserQuery','13246484759','107','ocs') 
    print(output)
