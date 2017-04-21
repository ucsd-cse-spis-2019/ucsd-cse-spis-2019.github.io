---
topic: "ACMS: Instructor Notes"
desc: "What instructors should know about the ACMS setup"
---

The typical ACMS setup for spis has the following kinds of accounts:

* a master instructor account, e.g. `spis16`, with some special privileges
* instructor/mentor accounts for speicifc individuals, e.g. spis16t1, spis16t2, spis16t3, etc.
* student acconts for the SPIS participants, that are typically named spis16aa, spis16ab, etc.

The directory hierarchy is typically as shown here:

```
[spis16@ieng6-240]:spis16:222$ pwd
/home/linux/ieng6/spis16
[spis16@ieng6-240]:spis16:223$ ls
hold      spis16ai  spis16at  spis16be  spis16bp  spis16ca  spis16cl  sps16t10
public    spis16aj  spis16au  spis16bf  spis16bq  spis16cb  spis16t1  sps16t11
spis16    spis16ak  spis16av  spis16bg  spis16br  spis16cc  spis16t2  sps16t12
spis16aa  spis16al  spis16aw  spis16bh  spis16bs  spis16cd  spis16t3  sps16t13
spis16ab  spis16am  spis16ax  spis16bi  spis16bt  spis16ce  spis16t4  sps16t14
spis16ac  spis16an  spis16ay  spis16bj  spis16bu  spis16cf  spis16t5  sps16t15
spis16ad  spis16ao  spis16az  spis16bk  spis16bv  spis16cg  spis16t6  sps16t16
spis16ae  spis16ap  spis16ba  spis16bl  spis16bw  spis16ch  spis16t7  sps16t17
spis16af  spis16aq  spis16bb  spis16bm  spis16bx  spis16ci  spis16t8
spis16ag  spis16ar  spis16bc  spis16bn  spis16by  spis16cj  spis16t9
spis16ah  spis16as  spis16bd  spis16bo  spis16bz  spis16ck  spis16zz
[spis16@ieng6-240]:spis16:224$ 
```

# Custom code for the student's path, etc.

If you want to customize things for the students account, the place to do it is in the directory 

```
/home/linux/ieng6/spis16/public
```

In that folder, there will likely be a file called `README.instructor` that explains the `modulefiles` directory, and
how it is used to control the `PATH` etc.

