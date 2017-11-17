# hashdiff
Check files on two servers are in sync
~~~~
server1$ ./file_hashes.py . hashleft
Adding ./README.md
Adding ./file_hashes.py
Adding ./hashdiff.py
3 unique hashes
File hashleft written.
server1$ cat hashleft
93d07fb1b85bb0cfeecb8ce6489521f51941865d,./hashdiff.py
49cf89dda913336fdbf2efb6a16a24f2568fddff,./README.md
122132961dc35188e1c4a7abdc337736df99fdf8,./file_hashes.py

server2$ /file_hashes.py . hashright
Adding ./README.md
Adding ./file_hashes.py
2 unique hashes
File hashright written.
server2$ cat hashright
49cf89dda913336fdbf2efb6a16a24f2568fddff,./README.md
122132961dc35188e1c4a7abdc337736df99fdf8,./file_hashes.py
server2$ ./hashdiff.py hashleft hashright
Loaded 3 hashes from hashleft.
Loaded 2 hashes from hashright.
1 hashes are in left but not right:
93d07fb1b85bb0cfeecb8ce6489521f51941865d ./hashdiff.py
server2$
~~~~

