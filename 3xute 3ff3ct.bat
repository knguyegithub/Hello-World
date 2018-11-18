@echo off
color 04
:A
echo 0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1              2001:db8:acad:e12d:3402:aff2:32f4:c43  ffe6:32:8dda::0:4cd    
ping localhost -n 1 > nul
echo 1 0 0 1 0 1 0 0   1 0 0 1 0 1 0 0   1 0 0 1 0 1 0 0   1 0 0 1 0 1 0 0		2001:db8:acad:3849:0:8bd3::	2001:db8:acad:3849:0:8bd3::
ping localhost -n 1 > nul
echo 0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1		ff30:4fad:29bc::0:adc7		2001:db9:2124:0::873a:1a
ping localhost -n 1 > nul
echo 1 0 0 1 0 1 0 0   1 0 0 1 0 1 0 0   1 0 0 1 0 1 0 0   1 0 0 1 0 1 0 0		ffe6:32:8dda::0:4cd	        ffe6:32:8dda::0:4cd
ping localhost -n 1 > nul
echo 0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1   0 1 1 0 1 0 1 1 	        2001:db9:2124:0::873a:1a	2001:db8:acad:e12d:3402:aff2:32f4:c43
ping localhost -n 1 > nul
goto A