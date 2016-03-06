# profile ycsb benchmark.
# author: Yingjun Wu <yingjun@comp.nus.edu.sg>
# date: March 5th, 2016

import os
import time

server1_name = "yingjunw@dev1.db.pdl.cmu.local"
server2_name = "yingjunw@dev2.db.pdl.cmu.local"

oltp_home = "~/oltpbench"

if __name__ == "__main__":
	cwd = os.getcwd()

	start_cleanup = "rm -rf callgrind.out.*"
	start_peloton_valgrind = "valgrind --tool=callgrind --trace-children=yes ./src/peloton -D ./data > /dev/null 2>&1 &"
	stop_peloton = "pg_ctl -D ./data stop"
	script_location = cwd + "/../scripts/oltpbenchmark/peloton_ycsb_config.xml"
	start_ycsb_bench = "./oltpbenchmark -b ycsb -c " + script_location + " --create=true --load=false --execute=true -s 5 -o outputfile"
	
	os.system(stop_peloton)
	os.system(start_cleanup)
	os.system(start_peloton_valgrind)
	time.sleep(5)
	# go to oltpbench directory
	os.chdir(os.path.expanduser(oltp_home))
	os.system(start_ycsb_bench)
	# go back to cwd
	os.chdir(cwd)
	os.system(stop_peloton)
	