SLZ - Scholastic Learning Zone (International applications)
We basically have to gut what was built and start fresh on the new arch
They took SAM connect, stripped it down made a new UI and added a new page.  It didn't work out so well.

Authentication Service
======================
A - Dev Desktop env (code/test)   (Ron)
B - Maven/Jenkins CI Env          (Anton)
C - Dev server VM                 (Anton)
D - Code service FrameWork        
E - Hire PG DBA
F - Finalize ESB Service decision   (Ron/Edison)

::

	----|
	A   |
	B   |---- 14 July
	C   |
	F   |
	----|


Arch Diagram::
============

					        ______________
	       |---------------| Auth ID MGMT |------------ [ ] postgres
	       |                --------------              [ ]
  ____     |
 |SLZ1|----|
  ----     |
           |   ____
           |--|SLZ2|
           |   ----



MILESTONE 1
-----------
Our SOA ESB
   - to reach auth svc
   - replication/sync

Authn svc/ Federated ID Management
   - authn

Traffic Mgr
   - Bounced
   - DDOS shield





MILESTONE 2
-----------

