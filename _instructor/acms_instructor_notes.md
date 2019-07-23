---
topic: "ACMS: Instructor Notes"
desc: "What instructors should know about the ACMS setup"
---

The typical ACMS setup for spis has the following kinds of accounts:

* a master instructor account, e.g. `spis19`, with some special privileges
* instructor/mentor accounts for speicifc individuals, e.g. spis19t1, spis19t2, spis19t3, etc.
* student acconts for the SPIS participants, that are typically named spis19aa, spis19ab, etc.

The directory hierarchy is typically as shown here:

```
[spis19@ieng6-240]:spis19:222$ pwd
/home/linux/ieng6/spis19
[spis19@ieng6-240]:spis19:223$ ls
hold      spis19ai  spis19at  spis19be  spis19bp  spis19ca  spis19cl  sps16t10
public    spis19aj  spis19au  spis19bf  spis19bq  spis19cb  spis19t1  sps16t11
spis19    spis19ak  spis19av  spis19bg  spis19br  spis19cc  spis19t2  sps16t12
spis19aa  spis19al  spis19aw  spis19bh  spis19bs  spis19cd  spis19t3  sps16t13
spis19ab  spis19am  spis19ax  spis19bi  spis19bt  spis19ce  spis19t4  sps16t14
spis19ac  spis19an  spis19ay  spis19bj  spis19bu  spis19cf  spis19t5  sps16t15
spis19ad  spis19ao  spis19az  spis19bk  spis19bv  spis19cg  spis19t6  sps16t16
spis19ae  spis19ap  spis19ba  spis19bl  spis19bw  spis19ch  spis19t7  sps16t17
spis19af  spis19aq  spis19bb  spis19bm  spis19bx  spis19ci  spis19t8
spis19ag  spis19ar  spis19bc  spis19bn  spis19by  spis19cj  spis19t9
spis19ah  spis19as  spis19bd  spis19bo  spis19bz  spis19ck  spis19zz
[spis19@ieng6-240]:spis19:224$ 
```

# Custom code for the student's path, etc.

If you want to customize things for the students account, the place to do it is in the directory 

```
/home/linux/ieng6/spis19/public
```

In that folder, there will likely be a file called `README.instructor` that explains the `modulefiles` directory, and
how it is used to control the `PATH` etc.

