## User story testing

**All tests have been tested on google chrome inspect tools with small, medium and large devices**

## Testing of Feature 1 - Navigation 
User stories

- 2.1 As a site user I can intuitively navigate the site so that the layout of the site is consistent
- 2.2 As a site user I can search post title so that I can locate posts
- 2.3 As a site user I can click on the menu so that I can select topics and other pages to view

___

**Action** 
1.	Navigate to https://coronavirusforum.herokuapp.com/
2.	Navigate and click on menu icon
3.	Navigate and click on the account icon
4.	Navigate and click on account icon, sign in, enter credentials
5.	Navigate and click on the account icon
6.	Navigate and click on Search icon

This action was tested on a logged in user, not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|**Small screen devices**|[Small](docs/images/testing/features/test1_1.png)|Passed|
||Navigation bar is displayed at the top of the page|see "small" link|Passed|
||**On the Left**|
||Menu icon is displayed|see "small" link|Passed|
|2|Navigation links are displayed “Home”, “Topics”, “Latest Statistics” ,“About Us”|[Dropdown menu](docs/images/testing/features/test1_2.png)|Passed|
||**Center**|||
||**Not logged in user**|||
||Account icon is displayed|see small link above|Passed|
|| “Sign in” link is displayed|see small link above|Passed|
|3.| “Sign up” or “Sign in” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_3.png)|Passed|
||**Logged in user**|||
||Account icon is displayed|see small link above|Passed|
|4.|“Welcome (username)” e.g. “Welcome Admin” displayed under icon|see small link above|Passed|
|5.|“Change password” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_4.png)|Passed|
|| “Logout” is displayed in the drop down menu|see dropdown menu link above|Passed|
||**Right**|||
||Search icon is displayed|see small link above|Passed|
|6. |Search bar and submit button is displayed under the navigation menu|[Search bar](docs/images/testing/features/test1_5.png)|Passed|

<br>

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|**Medium and large screen devices**|[Medium ](docs/images/testing/features/test1_6.png)[large](docs/images/testing/features/test1_7.png)|Passed|
||**On the Left**||
||A coronavirus icon is displayed|see medium/large links above|Passed|
||**Center**||
||Search bar and submit button is displayed|see medium/large links above|Passed|
||Navigation links are displayed -“Home”, “Topics”, “Latest Statistics” ,“About Us”|see medium/large links above|Passed|
||**Right**||
||**Not logged in user**|||
||Account icon is displayed|see medium/large links above|Passed|
||Under icon, “Sign in” is displayed
|3.| “Sign up” or “Sign in” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_8.png)|Passed|
||**Logged in user**|||
||Account icon|see medium/large links above|Passed|
|4.|Under icon  - “Welcome (username)” e.g. “Welcome Admin”|[Dropdown menu](docs/images/testing/features/test1_8a.png)|Passed|
|5.|“Change password” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_9.png)|Passed|
|| “Logout” is displayed in the drop down menu |see dropdown menu link above|Passed|

___

## Testing of Feature 2 - Footer
User stories

- 3.1 As a site user I can locate the social media accounts so that I can follow their updates
- 3.2 As a guest/logged-in site user I can view the 'about us page so that I can understand more about the forum and its purpose
- 3.3 As a guest/logged-in site user I can view the 'talk guidelines page so that I can understand the rules
- 3.4 As a guest/logged-in site user I can complete a contact form so that I can provide feedback on posts to site admin where needed (report offending posts or express concern) so that appropriate action can be taken if needed

___

**Action** 
1. Navigate to footer
2. Navigate and click on Talkguidelines link
3. Navigate and click on Privacy policy link
4. Navigate and click on Contact us link
5. Navigate and click on Facebook icon
6. Navigate and click on Twittericon
7. Navigate and click on Instagram icon

This action was tested on a logged in user, not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Footer is displayed at the bottom of the page|[Small ](docs/images/testing/features/test2_1.png)[Medium ](docs/images/testing/features/test2_2.png)[Large](docs/images/testing/features/test2_3.png)|Passed|
|2.|Talkguides page is displayed|[Result ](docs/images/testing/features/test2_4.png)|Passed|
|3.|Privacy page is displayed|[Result ](docs/images/testing/features/test2_5.png)|Passed|
|4.|Contact us page is displayed|[Result ](docs/images/testing/features/test2_6.png)|Passed|
|5.|Facebook page is displayed in new tab|[Result ](docs/images/testing/features/test2_7.png)|Passed|
|6.|Twitter page is displayed in new tab|[Result ](docs/images/testing/features/test2_8.png)|Passed|
|7.|Instagram page is displayed in new tab|[Result ](docs/images/testing/features/test2_9.png)|Passed|

___

## Testing of feature 3 - home page
User stories

- 4.1 As a site user I can view the header and hero image so that I can learn more about the website and its purpose

- 4.2 As a site user I can click on the menu so that I can select topics and other pages to view

- 4.3 a guest/logged-in user I can view the latest 5 posts so that I can keep up to date with the latest posts

**Action** 
1. Navigate to https://coronavirusforum.herokuapp.com/
2. Users logs in
3. Users clicks on a post

This action was tested on a logged in user, not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|The home page is displayed|[Small ](docs/images/testing/features/test3_1.png)[Medium ](docs/images/testing/features/test3_2.png)[Large](docs/images/testing/features/test3_3.png)|Passed|
||Header title, carousel,Title "Latest post", 5 latest posts create, Post title, number of comments, posted by and created time is displayed|see  link above|Passed|
||Carousel of three images|see link above|Passed|
|2.|Flash message section is displayed|[Result ](docs/images/testing/features/test3_4.png)|Passed|
|3.|Post detail is displayed|[Result ](docs/images/testing/features/test3_5.png)|Passed|

___

## Testing of feature 4 - Account Management
User stories

- 1.1 As a site user I can login with my username and password so that I can access the sites full functionality 
- 1.2 As a site user I can login with google so that I can save time and login securely
- 1.3 As a site user I can change my password so that I can stay secure
- 1.4 As a logged-in site user I can log out of my account so that other users cannot access my account
- 1.5 As a site user I can see the current logged-in state so that I know if I can access logged in functionality
- 1.6 As a site user I can register so that I have a role-based login and functionality of commenting and voting on posts
- 1.7 As a site user I can receive a welcome email so that I know that I have signed up correctly and feel like a valued user
- 6.4 As a site admin I can restrict/delete a user account in django admin page if the content is offending or against 'talk guidelines' so that I can manage the site content for the best UX
- 6.5 As a site admin I can manage user accounts so that I can create new users, update their details, deactivate their status

___
All functionality has been tested fully from allauth

### **Test 1 - Sign in**

**Action** 
1. Click on Sign in from the account management menu
2. Navigate to sign in page, enter username and password and click sign in 
3. Navigate to sign in page, enter username which is not registered and password and click sign in 
4. Navigate to sign in page, enter username and incorrect password and click sign in 
5. Navigate to sign in page, enter username and leave password blank and click sign in 
6. Navigate to sign in page, leave username and fill out  password and click sign in 

This action was tested on a not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Sign is page displayed|[Small ](docs/images/testing/features/test4_1.png)[Medium ](docs/images/testing/features/test4_1_1.png)[Large](docs/images/testing/features/test4_1_2.png)|Passed|
|2.|Message displayed "Successfully signed in as NurseryKeyworker",Redirected to home page|[Result ](docs/images/testing/features/test4_1_3.png)|Passed|
||Under the account icon "Welcome NurseryKeyworker" will be displayed, the text will change from sign in to sign out in the drop down menu|[Result ](docs/images/testing/features/test4_1_4.png)|Passed|
|3.|Message displayed "The e-mail address and/or password you specified are not correct."|[Result ](docs/images/testing/features/test4_1_5.png)|Passed|
|4.|Message displayed "The e-mail address and/or password you specified are not correct."|[Result ](docs/images/testing/features/test4_1_6.png)|Passed|
|5.|Message displayed "Please fill in this field."|[Result ](docs/images/testing/features/test4_1_7.png)|Passed|
|6.|Message displayed "Please fill in this field."|[Result ](docs/images/testing/features/test4_1_8.png)|Passed|



### **Test 2 - Sign in with Google**

**Action** 
1. Navigate and click on Sign in, Sign in with Google
2. User clicks continue
3. User clicks on account to sign in

This action was tested on a not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Sign in via google page displayed|[Result ](docs/images/testing/features/test4_2_1.png)|Passed|
|2.|Sign in with Google page|[Result ](docs/images/testing/features/test4_2_2.png)|Passed|
|3.|Redirected to home page, flash message displayed|[Result ](docs/images/testing/features/test4_2_3.png)|Passed|


### **Test 3 - Change password**
User stories 

- 1.3 As a site user I can change my password so that I can stay secure

**Action** 
1. Navigate and click on Sign in
2. User clicks Change password
3. User clicks Change password button

This action was tested on a not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Drop down menu displayed|[Result ](docs/images/testing/features/test4_3_1.png)|Passed|
|2.|Changed password page displayed|[Result ](docs/images/testing/features/test4_3_2.png)|Passed|
|3.|Flash message displayed "Password successfully changed"|[Result ](docs/images/testing/features/test4_3_3.png)|Passed|


### **Test 3a - Forgot password**
User stories

- 1.3 As a site user I can change my password so that I can stay secure

**Action** 
1. Navigate, click on Sign in, click on forgot password link
2. User enters their email address and clicks reset password
3. User is sent an email
4. User clicks on reset link
5. User  enters password twice, clicks on change password

This action was tested on a not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Password reset page displayed|[Result ](docs/images/testing/features/test3a_1.png)|Passed|
|2.|Password reset password page - sent email displayed|[Result ](docs/images/testing/features/test3a_2.png)|Passed|
|3.|Email with reset link|[Result ](docs/images/testing/features/test3a_3.png)|Passed|
|4.|Change password page displayed|[Result ](docs/images/testing/features/test3a_4.png)|Passed|
|5.|Flash message displayed "Password successfully changed"|[Result ](docs/images/testing/features/test3a_3.png)|Passed|

### **Test 4 - Sign out**

**Action** 
1. Navigate and click on Sign in
2. User clicks on log out
3. User clicks on sign out

This action was tested on a logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Logout is displayed in the drop down menu|[Result ](docs/images/testing/features/test4_4_1.png)|Passed|
|2.|Sign out page is displayed|[Result ](docs/images/testing/features/test4_4_2.png)|Passed|
|3.|A success message will appear “you have signed out”, |[Result ](docs/images/testing/features/test4_4_3.png)|Passed|
||Under the account icon, the text will change from username to sign in|[Result ](docs/images/testing/features/test4_4_4.png)|Passed|


### **Test 5 - Sign up**

**Action** 
1. Navigate and click on Sign up
2. Complete required fields Email address, username, password(twice) and click sign up
3. Click Confirm email address link
4. User selects confirm button

This action was tested on a not logged user

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Sign up page displayed|[Result ](docs/images/testing/features/test4_5_1.png)|Passed|
|2.| Success message – “ Confirmation email sent”|[Result ](docs/images/testing/features/test4_5_2.png)|Passed|
||User is redirected to verify your email address page|[Result ](docs/images/testing/features/test4_5_3.png)|Passed|
||email sent to verify email address|[Result ](docs/images/testing/features/test4_5_4.png)|Passed|
||Welcome email sent |[Result ](docs/images/testing/features/test4_5_5.png)|Passed|
|3.|  Confirm email address page displayed|[Result ](docs/images/testing/features/test4_5_6.png)|Passed|
|4.|  Success message – you have confirmed (ckcabs@hotmail.com), User redirected to home page|[Result ](docs/images/testing/features/test4_5_7.png)|Passed|

### **Test 6 - User management -restrict/delete an account**

**Action** 
1. Login to django admin panel as admin, select users and click on the username
2. Deselect Active to deactivate user
3. Check if user has been deactivated.  Sign in with user details


This action was tested on admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Change user info page displayed    |[Result ](docs/images/testing/features/test4_6_1.png)|Passed|
|2.| Success message – “ The user “USERNAME” was changed successfully.”|[Result ](docs/images/testing/features/test4_6_2.png)|Passed|
|3.| Messages displayed – “This account is inactive.” |[Result ](docs/images/testing/features/test4_6_3.png)|Passed|

### **Test 7 - User management -Create and update**

**Action** 
1. Login to django admin panel as admin, select users and click add user
2. Fill in username, password twice and click save
3. To update a user details, select users, select the user
4. Update detail and click save
5. To delete a user, select users, select the user, click on the dropdown bar action and select delete
6. User clicks Yes, I'm sure

This action was tested on admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Add user page displayed    |[Result ](docs/images/testing/features/test4_7_1.png)|Passed|
|2.| Success message – “ The user “USERNAME” was added successfully. You may edit it again below..”|[Result ](docs/images/testing/features/test4_7_2.png)|Passed|
|3.| Change user page displayed |[Result ](docs/images/testing/features/test4_7_3.png)|Passed|
|4.| Message displayed “The user Christopher was changed successfully. |[Result ](docs/images/testing/features/test4_7_4.png)|Passed|
|5.| Confirmation page displayed |[Result ](docs/images/testing/features/test4_7_5.png)|Passed|
|6.| Message displayed “Successfully deleted 1 user. |[Result ](docs/images/testing/features/test4_7_6.png)|Passed|

___

## Testing of feature 5 - Posts
User stories

- 5.1 As a guest user, I can view posts so that I can keep up to date with the latest posts and user comments
- 5.2 As a Site User I can view a paginated list of posts so that my screen doesn't get overpopulated with posts
- 5.3 As a guest/logged-in site user, I can select a topic so I can view posts related to the topic
- 5.4 As a guest/logged-in user I can view a list of posts so that I can select a post that interests me
- 5.5 As a guest/logged-in user I can click on a post so that I can read the full article and related comments
- 5.6 As a logged-in site user I can vote on a post/opinion poll, where applicable, so that I can take an active role in the forum if I wish
- 5.7 As a logged-in user I can create a new post so that I can post content on the site for other users to view
- 5.8 As a logged in site user I can edit a post (subject header /text body) so that I can change the content if required
- 5.9 As a logged-in site user I can leave comments on a post so that I can take an active role in the forum (be involved in the conversation/express my opinion)
- 5.10 As a Site User, I can view a paginated list of comments so that my screen doesn't get overpopulated with comments
- 5.11 As a Site User I can delete a post that I have posted so that I can take content off the website
- 5.12 As a user I can report a post to site admin so that I can provide feedback on posts on offending posts or express concern so that appropriate action can be taken if needed
- 5.13. As a user who is directed to a non-existent page or resource, I can receive feedback and be redirected back to the main page automatically/smoothly without having to use the browser navigation buttons so that I have a streamlined UX
- 6.3 As a Site Admin user I can view, update and delete posts in django admin page so that I can manage content or information that might be breaching policy or upon the request of a user/poster

___


### **Test 1 -View a list of posts**

**Action** 
1. Login, Navigate to the topic in the main menu and select a topic
2. Log out, Navigate to the topic in the main menu and select a topic
3. Logged in user - User completes form with image and enable voting
4. Logged in user - User clicks submit post


This action was tested on a not logged user and logged in user 

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Logged in user- Post list is displayed with posts ,paginated by 5 posts|[Small ](docs/images/testing/features/test5_1_1.png)[Medium ](docs/images/testing/features/test5_1_2.png)[Large](docs/images/testing/features/test5_1_3.png)|Passed|
||"Start a new post within this topic" displayed|See link above|Passed|
|2.| Not-logged in user - Link NOT displayed "start a new post within this topic"|[Result ](docs/images/testing/features/test5_1_4.png)|Passed|
|3.|New post page displayed |[Result ](docs/images/testing/features/test5_1_5.png)
|4.| Flash message is displayed "Post submitted"|[Result ](docs/images/testing/features/test5_1_8.png)|Passed|
|| Redirected to the post|See above result link|Passed|
|| Voting thumbs displayed, image displayed|See above result link|Passed|

### **Test 2 - Post detail**

**Action** 
1. Not-logged in user -Navigate to topic in the main menu and select a topic and click on a post
2. Not-logged in user - try's to select up and down thumb
3. Not-logged in user - select sign in to vote
4. login, Navigate to topic in the main menu and select a topic and click on a post

This action was tested on a not logged user and  logged in user

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Post displayed, Sign in to vote and "Add one" referring to add a comment NOT DISPLAYED|[Result ](docs/images/testing/features/test5_2_1.png)|Passed|
||Update, Delete, Report post links NOT DISPLAYED|See link above|Passed|
|2.|User can not select a thumb||Passed|
|3.|Login page displayed|[Result ](docs/images/testing/features/test5_2_2.png)|Passed|
|4.|Post displayed, Sign in to vote NOT DISPLAYED and "Add one" referring to add a comment DISPLAYED|[Result ](docs/images/testing/features/test5_2_3.png)|Passed|
||Update, Delete, Report post links DISPLAYED|See link above|Passed|
||No Comments yet displayed as no comments made|See link above|Passed|
||See section 8 for comment testing|See link above|Passed|


### **Test 3 - Voting**

See feature 6


### **Test 4 - Update /delete a post**

**Action** 
1. Not logged in user - Navigate to the topic in the main menu and select a topic and click on a post 
2. Navigate to account icon and sign in as admin, Navigate to the topic in the main menu and select a topic and click on a post (Signed In)
3. Navigate to account icon and sign in as TwickehamTeacher, Navigate to the topic in the main menu and select a topic and click on a post (Signed In)
4. User clicks on update
5. User changes title and clicks submit
6. User click on delete
7. User clicks cancel
8. User clicks delete link, then delete post button

This action was tested on a not logged user and logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Post displayed - Update, Delete links not displayed|[Result ](docs/images/testing/features/test5_4_1.png)|Passed|
|2.|Post displayed - Update, Delete links not displayed as not user TwickenhamTeacher|[Result ](docs/images/testing/features/test5_4_2.png)|Passed|
||Report Post link displayed as logged in|See link above|Passed|
|3.|Post displayed - Update, Delete links displayed|[Result ](docs/images/testing/features/test5_4_3.png)|Passed|
|4.|Update post displayed with current data in fields|[Result ](docs/images/testing/features/test5_4_4.png)|Passed|
|5.|Success message displayed "post updated", redirected to updated post detail page|[Result ](docs/images/testing/features/test5_4_5.png)|Passed|
|6.|Delete post displayed "are you sure?"|[Result ](docs/images/testing/features/test5_4_6.png)|Passed|
|7.|redirect back to post detail page|[Result ](docs/images/testing/features/test5_4_7.png)|Passed|
|8.|Message displayed post deleted|[Result ](docs/images/testing/features/test5_4_8.png)|Passed|
||Redirected to home page|See link above|Passed|

### **Test 5 - Comment on a post**

See feature 8

### **Test 6 - Report post**

See feature 7

### **Test 7 - Error page**

**Action** 
1. user types in a post id that doesn't exist in the URL https://coronavirusforum.herokuapp.com/topic/21

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|404 error page displayed|[Result ](docs/images/testing/features/test5_7_1.png)|Passed|


### **Test 8 - Post management -Create, update, delete**

**Action** 
1. Login to django admin panel as admin, click posts, click add post
2. Fill in details and click save
3. To edit - click posts, select post to change
4. Update post and click save
5. To delete a post, select posts, select the post check box, click on the dropdown bar action,select delete and click go
6. User clicks Yes, I'm sure

This action was tested on admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.| Add post displayed |[Result ](docs/images/testing/features/test5_8_1.png)|Passed|
|2.| Success message – “ The post Test post 8 was added successfully.”|[Result ](docs/images/testing/features/test5_8_2.png)|Passed|
|3.| Change post page displayed |[Result ](docs/images/testing/features/test5_8_3.png)|Passed|
|4.| Message displayed “the Test post 8 was changed successfully". |[Result ](docs/images/testing/features/test5_8_4.png)|Passed|
|5.| Confirmation page displayed |[Result ](docs/images/testing/features/test5_8_5.png)|Passed|
|6.| Message displayed “Successfully deleted 1 post". |[Result ](docs/images/testing/features/test5_8_6.png)|Passed|

___

## Testing of feature 6 - Voting
User stories

- 5.6 As a logged-in site user I can vote on a post/opinion poll, where applicable, so that I can take an active role in the forum if I wish
___

**Action** 
1. Navigate to the topic in the main menu and select a topic and click on a post ( with voting enabled) - Not logged in 
2. Navigate to the topic in the main menu and select a topic  - Not logged in /logged in
3. Login as WelshDoctor, Navigate to the topic in the main menu and select a topic and click on a worried teacher post by twickenhamteacher 
    User trys to down the existing vote
4. Login as twickenhamteacher , Navigate to the topic in the main menu and select a topic and click on Worried Teacher ( with voting enabled) 
5. Make a vote, Select "upthumb"
6. Change vote, Select "downthumb"
7. Change vote, deSelect "downthumb" - No vote made
8. Make a vote, select "upthumb", "deselect upthumb" No vote made
9. Make a vote, select downthumb,
10. Change vote, select "upthumb"


This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Post displayed, Sign to vote link displayed, thumbs displayed|[Result ](docs/images/testing/features/test6_1_1.png)|Passed|
|2.|Post list displayed, under post title, has "VOTE" displayed to show posts where voting is enabled|[Result ](docs/images/testing/features/test6_1_2.png)|Passed|
|3.|No option too. The logged in user is not the owner of the post|[Result ](docs/images/testing/features/test6_1_3.png)|Passed|
|4.|Post displayed, votes displayed, no existing vote by logged in user|[Result ](docs/images/testing/features/test6_1_4.png)|Passed|
|5.|success message displayed "upthumb selected", upthumb highlight and number increased|[Result ](docs/images/testing/features/test6_1_5.png)|Passed|
|6.|success message displayed "downthumb selected", downthumb highlighted and downthumb number increased and upthumb decreased by 1 and not highlighted|[Result ](docs/images/testing/features/test6_1_6.png)|Passed|
|7.|success message displayed "downthumb selected", downthumb and upthumb not highlighted no vote in the numbers|[Result ](docs/images/testing/features/test6_1_7.png)|Passed|
|8.|success message displayed "upthumb selected", upthumb highlighted, number increase by 1.  success messages displayed "upthumb deselected" number decreased by 1, upthumb not highlighted|[Result ](docs/images/testing/features/test6_1_8.png)|Passed|
|9.|success message displayed "downthumb selected", downthumb highlighted and downthumb number increased| [Result ](docs/images/testing/features/test6_1_9.png)|Passed|
|10.|success message displayed "upthumb selected",upthumb highlighted, down thumb not highlighted and downthumb number decrease and upthumb increase by 1|[Result ](docs/images/testing/features/test6_1_10.png)|Passed|

___

## Testing of Feature 7 -Report post
User stories

- 5.12 As a user I can report a post to site admin so that I can provide feedback on posts on offending posts or express concern so that appropriate action can be taken if needed

**Action** 
1. Navigate to the topic in the main menu and select a topic and click on a post with comments (not signed in)
2. Navigate to account icon and sign in, navigate to the topic in the main menu and select a topic and click on a post (Signed In)
3. User clicks on report post
4. User leaves emails address blank and clicks send message button
5. User completes emails address, message is  blank and clicks send message button
6. User completes all fields and clicks send message button

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Post and comments displayed - report post link not displayed|[Result ](docs/images/testing/features/test7_1_1.png)|Passed|
|2.|Post displayed with comments- report post link displayed|[Result ](docs/images/testing/features/test7_1_2.png)|Passed|
|3.|Contact us page displayed with title and email address(if registered) populated|[Result ](docs/images/testing/features/test7_1_3.png)|Passed|
|4.|message displayed "Please fill in this field"|[Result ](docs/images/testing/features/test7_1_4.png)|Passed|
|5.|message displayed "Please fill in this field"|[Result ](docs/images/testing/features/test7_1_5.png)|Passed|
|6.|message displayed "Email sent successfully", on the template message " thanks twickenhamteacher"|[Result ](docs/images/testing/features/test7_1_6.png)|Passed|
||Email received by admin |[Result ](docs/images/testing/features/test7_1_7.png)|Passed|

___

## Testing of Feature 8 - Comments
User stories

- 5.9 As a logged-in site user I can leave comments on a post so that I can take an active role in the forum (be involved in the conversation/express my opinion)
- 5.10 As a Site User, I can view a paginated list of comments so that my screen doesn't get overpopulated with comments
- 6.2 As a site admin I can create, edit and delete comments on the Django admin page so that I can manage the site content for the best UX

**Action** 
1. Navigate to the topic in the main menu and select a topic and click on a post with comments (not signed in)
2. Navigate to the topic in the main menu and select a topic and click on a post without comments (not signed in)
3. Sign in, select a topic in the main menu  and click on a post with no comments(Signed In)
4. Sign in, select a topic in the main menu  and click on a post with comments(Signed In)
5. User clicks on add comment link
6. User leaves comment blank and clicks add comment
7. Users fills in comment and clicks add comment button

This action was tested on a not logged user, logged in user and admin   

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Post  and comments displayed - add comment link not displayed|[Result ](docs/images/testing/features/test8_1_1.png)|Passed|
|2.|Sign in to make a comment link displayed |[Result ](docs/images/testing/features/test8_1_1.png)|Passed|
|3.|Post displayed, "no comments yet" displayed , add one link displayed|[Result ](docs/images/testing/features/test8_1_3.png)|Passed|
|4.|Post displayed with comments- add comment link displayed|[Result ](docs/images/testing/features/test8_1_4.png)|Passed|
|5.|Add new comment page displayed |[Result ](docs/images/testing/features/test8_1_5.png)|Passed|
|6.|This field is required displayed |[Result ](docs/images/testing/features/test8_1_6.png)|Passed|
|7.|Success message displayed "Comment added", redirected to post detail page with comment|[Result ](docs/images/testing/features/test8_1_6_1.png)|Passed|
||Post with more than 5 comments - paginated by 5|[Result ](docs/images/testing/features/test8_1_8.png)|Passed|

___

### **Test 2 - Create, edit and delete comment by admin panel**

**Action** 
1. Login to django admin panel as admin, select comments and add comment
2. select post from the drop down list, complete name and comment and click save
3. To edit - select comment from select comment to change comment page
4. Update comment and click save
5. To delete a comment, select comments, select the comment, click on the dropdown bar action and select delete
6. User clicks Yes, I'm sure

This action was tested on admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.| Add comment displayed page   |[Result ](docs/images/testing/features/test8_2_1.png)|Passed|
|2.| Success message – “ The comment "COMMENTNAME" was added successfully.”|[Result ](docs/images/testing/features/test8_2_2.png)|Passed|
|3.| Change comment page displayed |[Result ](docs/images/testing/features/test8_2_3.png)|Passed|
|4.| Message displayed “the COMMENTNAME” was changed successfully. |[Result ](docs/images/testing/features/test8_2_4.png)|Passed|
|5.| Confirmation page displayed |[Result ](docs/images/testing/features/test8_2_5.png)|Passed|
|6.| Message displayed “Successfully delete 1 comment". |[Result ](docs/images/testing/features/test8_2_6.png)|Passed|

___

## Testing of Feature 9 -Topics
User stories

- 5.3 As a guest/logged-in site user, I can select a topic so I can view posts related to the topic
- 5.4 As a guest/logged-in user I can view a list of posts so that I can select a post that interests me
- 6.1 As a site admin I can create, edit and delete topic title on the Django admin page so that I can manage the site content for the best UX

### **Test 1 - Topic list and post list**
**Action** 
1. Navigate to the topic in the main menu 
2. Select a topic 
This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Topic list displayed in the main menu dropdown|[Result ](docs/images/testing/features/test9_1_1.png)|Passed|
|2.|Posts displayed by topic selected|[Result ](docs/images/testing/features/test9_1_2.png)|Passed|

### **Test 2 - Create, edit and delete topic by admin panel**

**Action** 
1. Login to django admin panel as admin, select topics and add topic"injections"
2. Fill in the Name and click save

3. To edit - select topics from select topic to change page
4. Update topic and click save
5. To delete a topic, select topics, select the topic, click on the dropdown bar action and select delete
6. User clicks Yes, I'm sure

This action was tested on admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.| Add topic displayed page   |[Result ](docs/images/testing/features/test9_1_3.png)|Passed|
|2.| Success message – “ The topic "injections" was added successfully.”|[Result ](docs/images/testing/features/test9_1_4.png)|Passed|
|3.| Change topic page displayed |[Result ](docs/images/testing/features/test9_1_5.png)|Passed|
|4.| Message displayed “the injections hospital” was changed successfully. |[Result ](docs/images/testing/features/test9_1_6.png)|Passed|
|5.| Confirmation page displayed |[Result ](docs/images/testing/features/test9_1_7.png)|Passed|
|6.| Message displayed “Successfully delete 1 topic". |[Result ](docs/images/testing/features/test9_1_8.png)|Passed|

___

## Testing of Feature 10 -Latest statistics
User stories

- 3.5 As a site user I can access reputable up to date data/support via a reliable and trustworthy source (such as the NHS/public health England) so that I am correctly informed and can stay up to date with statistics

- 3.6 As a site user, i can receive feedback if an API call fails, so that I receive a graceful UX and be correctly notified

**Action** 
1. Navigate and click on Latest statistics link in the main menu
2. Select date from the last 200 days and click select date
3. User try's to select a date in the future
4. User try's to select a date more then 200 days old
5. Api fails

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Latest statistics page is displayed|[Small ](docs/images/testing/features/test10_1_1.png)[Medium ](docs/images/testing/features/test10_1_2.png)[Large](docs/images/testing/features/test10_1_3.png)|Passed|
|2.|Data is displayed|[Result ](docs/images/testing/features/test10_1_4.png)|Passed|
|3.|Dates are not able to be selected|[Result ](docs/images/testing/features/test10_1_5.png)|Passed|
|4.|Dates are not able to be selected|[Result ](docs/images/testing/features/test10_1_6.png)|Passed|
|5.|500 error page displayed|[Result ](docs/images/testing/features/test10_1_7.png)|Passed|

___

## Testing of Feature 11 - About us
User stories

- 3.2 As a guest/logged-in site user I can view the 'about us page so that I can understand more about the forum and its purpose
on the main menu

**Action** 
1. Navigate and click on About us link in the main menu
2. User clicks up-to-date government guidelines link
3. User clicks up-to-date NHS help and support link

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|About us page is displayed|[Small ](docs/images/testing/features/test11_1_1.png)[Medium ](docs/images/testing/features/test11_1_2.png)[Large](docs/images/testing/features/test11_1_3.png)|Passed|
|2.|Government guidelines page displayed|[Result ](docs/images/testing/features/test11_1_4.png)|Passed|
|3.|NHS help and support  page displayed|[Result ](docs/images/testing/features/test11_1_5.png)|Passed|

___

## Testing of Feature 12 -Contact us
User stories

- 3.4 As a guest/logged-in site user I can complete a contact form so that I can provide feedback on posts to site admin where needed (report offending posts or express concern) so that appropriate action can be taken if needed

**Action** 
1. Navigate and click on Contact us link in the footer
2. User leaves subject blank, completes email and message and clicks send message button
3. User completes subject, leaves email blank and message blank and clicks send message button
4. User completes subject, types Hotmail in the email address, completes message and clicks send message button
5. User completes subject and email and leaves message blank and clicks send message button
6. User completes subject, email and message  and clicks send message button

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Contact us page displayed |[Result ](docs/images/testing/features/test12_1_1.png)|Passed|
|2.|Message displayed "Please fill in this field"|[Result ](docs/images/testing/features/test12_1_2.png)|Passed|
|3.|Message displayed "Please fill in this field"|[Result ](docs/images/testing/features/test12_1_3.png)|Passed|
|4.|Message displayed "Please include an @ sign in this field"|[Result ](docs/images/testing/features/test12_1_4.png)|Passed|
|5.|Message displayed "Please fill in this field"|[Result ](docs/images/testing/features/test12_1_5.png)|Passed|
|6.|Message displayed "Email sent successfully", on the template message " thanks" USERNAME"|[Result ](docs/images/testing/features/test12_1_6.png)|Passed|
||Email received by admin |[Result ](docs/images/testing/features/test12_1_7.png)|Passed|

___

## Testing of Feature 13 -Talk guidelines
User stories

- 3.3 As a guest/logged-in site user I can view the 'talk guidelines page so that I can understand the rules

**Action** 
1. Navigate and click on talk guideline link in the footer
2. Navigate and click on talk guideline link add new post
3. Navigate and click on talk guideline link add new comment

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1,2,3.|talkguide lines displayed|[Small ](docs/images/testing/features/test13_1_1.png)[Medium ](docs/images/testing/features/test13_1_2.png)[Large](docs/images/testing/features/test13_1_3.png)|Passed|

___

## Testing of Feature 14 -Privacy policy
User stories

- 3.7 As a guest/logged-in site user I can view the ‘privacy policy’ so that I can understand the rules

**Action** 
1. Navigate and click on privacy policy link in the footer

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|Privacy policy displayed|[Small ](docs/images/testing/features/test14_1_1.png)[Medium ](docs/images/testing/features/test14_1_2.png)[Large](docs/images/testing/features/test14_1_3.png)|Passed|

___

## Testing of Feature 15 -Search
User stories

- 7.1. As a site user I can search posts by title so I can view posts that interest me
- 7.2. As a site user I can search posts by title so I can view a paginated list of posts  so they don’t over populate the page

**Action** 
1. Navigate and click on Search bar in the nav bar, user types a post title "post" 
2. Navigate and click on Search bar in the nav bar, user types a post title that is not in the database
3. Navigate and click on Search bar in the nav bar, user doesn't enter criteria and clicks search

This action was tested on a not logged user, logged in user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1.|post list displayed paginated by 5|[Small ](docs/images/testing/features/test15_1_1.png)[Medium ](docs/images/testing/features/test15_1_2.png)[Large](docs/images/testing/features/test15_1_3.png)|Passed|
|2.|Search header display the search criteria, no posts displayed|[Result ](docs/images/testing/features/test15_1_4.png)|Passed|
|3.|"No Search criteria" displayed in header|[Result ](docs/images/testing/features/test15_1_5.png)|Passed|