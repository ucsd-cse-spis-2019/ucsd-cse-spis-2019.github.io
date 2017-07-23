---
topic: "Github: Addding members to an organization"
desc: "SPIS instructors, mentors and students must be added to ucsd-cse-spis-20xx github organization"
---

# Adding member to a github organization

SPIS instructors, mentors and students must be added to ucsd-cse-spis-2016 github organization.

* Instructors and mentors should be added with "Owner" access.
* Students should be added with "Member" access.
* In addition, it is very important the default access be set to 


# First, make sure the default access is "None"

Before adding anyone to the organization as a member, be sure that the default repo permission is set to None.

Otherwise, members of the organization may have too many privileges to repos in the organization.  For SPIS, we want
the default permission to be "None."     

With that setting, being a member of the organization confers only the privilege to create private repos in the organization.  

* Those private repos, by default are accessible only to the student that create the repo, and everyone with the "owner" privilege can access all of the repos (i.e. all instructors and mentors).  
* For students working in pairs (or teams), one of the pair partners (or team members) creates a a private repo under the ucsd-cse-spis-2016 organization, and then they can add their pair partner (or teammates) as collaborators with write permission.

Here is the screen where you should verify that the organization has the correct setting:

![default repo permissions should be none](github-spis-org-default-repo-permissions-50.png)

# Adding a member

To add a member, visit the organization page, and the click "Settings" (for the organization)

![](click-settings-on-org-page-50.png)

Then, click on "People" as shown in the image below:

![](click-people-on-organizations-settings-page-50.png)

To add a member, type in their github id in the box shown, and when it appears, click on it.  As of this writing: in the example below, you have to click on the atriton icon that pops up&mdash;it is not sufficient to just press enter.

![](add-atriton-to-github-org-50.png)

Once the id appeas, you can click to invite the member

![](click-invite-member-50.png)

Choose "member" for SPIS students.  Choose owner only for SPIS instructors and mentors.

![](invite-atriton-choose-member-50.png)

Note that the invited user *must* visit the organization page to accept the invitation before it takes effect.

This is typically a page such as https://github.com/ucsd-cse-spis-2016 (i.e. github.com followed by the organization name.)

