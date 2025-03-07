# Report for assignment 4

**Project Name:** sir-lancebot

**URL:** https://github.com/python-discord/sir-lancebot

A Discord bot built by the Python Discord community.

## Onboarding experience

For this task we chose another project since we couldn't find an appropriate issue on the previous project. The available documentation to start working on sir-lancebot gave a variation of approaches, such as using Gitpod, Docker, Poetry or installing dependencies yourself. Three people in the group used docker and one used Poetry to run the server. For testing, we all used Poetry. 

We felt that the documentation for the use of docker was a bit insufficient for people that haven't used docker before. For example, it doesn't mention that if you are a Windows user using WSL and Ubuntu, there are some required changes to the docker desktop settings page which are not presented in their documentation. In André’s case, Docker was unable to run at all because of the version of Windows 10 he was using. This took quite a lot of onboarding time and as with many development projects it would have been easier to develop on Linux. This shows how it is even more important for repositories labeled as “easy-to-contribute” to have an easy and quick onboarding process because the presentation of a straight forward setup in the onboarding documentation clashes with the experience for some users. 

The experience of setting up the discord server and bot was a little bit tricky. Some group members had some prior experience with discord bots, but the instructions from sir-lancebot where somewhat incorrect or difficult to interpret in some steps. Most was however pretty well described, but the problems that were encountered did cause us to spend a lot of time debugging and trying to get everything to work. But after docker desktop setup we simply needed to run a single command to install the dependencies and run the server. 

Since testing wasn't supported or used in this project we chose to do testing without docker. For this, we first installed the dependencies with the use of poetry install, as instructed by the documentation. This installation included the poetry virtual environment. Later on we used pytest and pytest asyncio for testing and these were not included in the original installation of the dependencies with poetry. It took quite a lot of development time understanding how to perform unit tests that works with this repository. If the repository would have had some testing cases to study from, the onboarding for creating tests would have been much quicker.

## Effort spent

| Task | William | Marcus | Arvid | Andre |
| --- | --- | --- | --- | --- |
| **plenary discussions/meetings** | 8h | 8h | 8h | 8h |
| **discussions within parts of the group** | 1h | 2h | 0h | 1h |
| **reading documentation** | 2h | 2h | 1.5h | 1h |
| **configuration and setup** | 0.5h | 0.5h | 2.5h | 4h |
| **analyzing code/output** | 3h | 1.5h | 2h | 2h |
| **writing documentation/ report** | 2h | 3h | 1h | 2h |
| **writing code** | 4h | 3h | 8h | 3h |
| **running code** | 1h | 1h | 1h | 2h |

For setting up tools and libraries (step 4), enumerate all dependencies you took care of and where you spent your time, if that time exceeds 30 minutes.

**Andre:** I had severe issues with setting up the environment so I could run the code. The documentation fails to warn about the issues that will arise from trying to set up a development environment on Windows. The start of the project for me was trying and failing to set up docker and poetry dependency manager. After some debugging I determined that the main issue was that Windows 10 Home edition does not have HyperV which is essential for WSL2 which docker runs on. The choice of using docker ultimately made it harder for development on Windows. However, fortunately, the code could be run without docker, but this also required setting up Poetry which took some time as well. 

## Overview of issue(s) and work done.

## Issue 1: Option to send public valentines privately through DMs

**URL:** https://github.com/python-discord/sir-lancebot/issues/1477

**Summary:** The discordbot sir-lancelot has a discord command “.bemyvalentine” that can either send a formatted love letter publicly in the channel it is called from or privately to a user. The issue creator would want a way to specify if the love letter sent should be anonymous or not.

**Scope:** effects the class “BeMyValentine”, function “send_valentine” and “anonymous” in the “be_my_valentine.py” file.

### Requirements:

1. public: When calling the command with the parameter “public” the function sends the love letter in the discord-channel it was created from. 

2. private: When calling the command with the parameter “private” the function sends the love letter to the user specified as a direct message.

3. signed: When calling the command with the parameter “signed” the function sends the love letter and includes the username of the person sending the message.

4. anon: When calling the command with the parameter “anon” the function sends the love letter but does not include the name of the person sending the message.

5. Wrong input: If the user does not include the necessary parameters an error message is display.

6. True anonymity: To make sure the message is anonymous if using anon,  it should be assured that it is not shown to other users. For instance the command call should be deleted from the public channel.

**Code changes:** Se appendix for git diff for issue 1

### Test results

Overall results with link to a copy or excerpt of the logs (before/after refactoring).

Since there were no tests in this project we implemented tests both for the original function and for the updated function.

**Before:**

Coverage for whole file: 59 %

link: https://github.com/agussarsson/sir-lancebot/blob/main/bemyvalentine_coverage_original_file.pdf 

Coverage for function: 100 %

link: https://github.com/agussarsson/sir-lancebot/blob/main/bemyvalentine_coverage_original_function.pdf 

**After:**

Coverage for whole file: 67 %

link: https://github.com/agussarsson/sir-lancebot/blob/main/bemyvalentine_coverage_new_file.pdf 

Coverage for function: 100 %

link: https://github.com/agussarsson/sir-lancebot/blob/main/bemyvalentine_coverage_new_function.pdf 

UML 
[BeMyValentine](https://www.plantuml.com/plantuml/umla/lLV1Sjis4BtpAr3ducOO9UbC3zKqCuazQSS7fmTxUj6e68XSKh10B0E0bZLj_xqB0g8WohITGoCT1Eo-tGKU5hlGH-k4SLsZikm7juO6MAk4r9d3bZbaAtGE6rPA0uMJg3ExaReLHZHCIGrkrm93uzQOPOKIrZAD9RnZmh8pCft1WxEpDIfPYfsTtGi5sf6PdQs0Dpi-26ONSBtxSpyxOtzdZFdOS-O71ximvrngwJW_jw2gFE0kqFqOj0f5oUyiwlD1S0yLMCSDAeWsXNkOimARHkZIpYvHErfgn5lGvM5fvrxKVvwmp5bdmSo99rkWAMVNqAp0vEnrVbWyzsJDcNM6_SE-e0RseV_f_SVGGgFUDTZPxnhr02xMK6mYHO-uY7X3Yy26GuDtylnOTg3DEpdnto8qZsjeRwsI3Sq6_Rz9IltKfzH-exJtsK16WJKHKiUaKOYRhWtUAK_9NsIsRNaq2G8m1WrVqrnv3hse8P3KTPZK1hkMfouuEQXvuiZo0EBH7CjEmIGseeXZgKho6gP5KtBXd8cfNNHc773iuDW-2S4DLCCDYLGTB-5eptj_dkxe6TjT66qDsK5agcjBuVQJViVfyagmXP6jBmx35dk55WqSIoQXWSPJWo2VDBFWA7TgUomz8NpwA7gDajQ11ZCII_l4KJ-N2j_2F-SQjbJC2cNfwWfJqnb-qZiQlzviXscyC3MumLrwaRmy3PNgldP2oKf2sJESQX9cdnBdgIGj15kXDe-6x1LJwqdauoqCPv4gkDTG3JT6bYLetW3rcpBm5SPpzbkdYzjzlOzE0iBlETI_3-pwwkRcwill4RSMenD9WtfbUhScWNqAKSiPopezbbAV2WMMeowE6b6ivmjgOhVBCVevO9_pBm5A4XdHj_4ZWqH-w2LN1-7YKacgIRVBdBrDOwRCJCREGw6TiyyF1VG9bBWu8VY5AngSfYas-zIsbs7ysMkJE2keq02z6kvn0o_XKrGKwuLuWjtHusZq6BaG5d8MivOIS8MeSbPtLBldx8-U2A4MDngtbH8RM4OTNVOR-De19KYYt4U2oK2zCPVUVd1-vVbQALWGdSlbkAE-VxQZNeCJiQi-LLadwkTqmVt_6qCqizNsCRde7DALBUZjmQakd7QG02DAZB3VgUDyGmiOlNwVWu-gFuK8cP25bphxwytYrS-_-6_Ul_oNRrXySMNXX_rwG9J2hg4ao9cqKjDV1yfJhCvYGcKVwUNi_qhy1m00)

### Project plan: 

**Steps:**

- Read documentation.

- Set up a test server.

- Create a discord server for testing.

- Change constant etc. to make it easier to test on our server.

- Set up a server on our local machine.

- Try out “.bemyvalentine” and see how it works/what to test for.

- The function has no tests. Create tests for the current version of the “.bemyvalentine” function. (this could possibly be different from documentation)

- Create new tests for the new functionality.

- Implement the new features.

- Make sure the tests passes.

- Change tests that are effected by the new features.

### Test case analysis:

The function had no tests from the start. We have created tests for before + after the changes. The first tests cover the functionality of the function as we have deemed it because there weren’t clear documentation on how exactly it should work. 

## Issue 2: Yoda Text Commands
**URL:** https://github.com/python-discord/sir-lancebot/issues/494 

**Summary:** The issue is to implement a “.yoda <text>” command which transforms the input text into “yoda-like” speech. The idea is based on a previous command implemented in the project called snakify, and should supposedly follow a similar structure.

This is the structure changes Yoda does to their speech, and the command should do the same:

*<subject> <action>* to *<action> <subject>*

**Example:** 

.yoda You must have patience my young Padawan.

Returns:

Patience you must have my young Padawan.

However, the issue does not describe the process well enough. Yoda speech is transforming

*subject-verb-object* to  *object-subject-verb*    

So we interpret that the issue will be resolved if this functionality is implemented instead of what is described in the issue.

**Scope:** Requires a new file and functions. Other effected files and areas are:

### Requirements:

**Generic requirements:**

1 Bot-command: When a user writes .yoda <text> it runs the function.

2 Scope: It should only work in “sir-lancebot-playground”, if called elsewhere an error is displayed explain it. [Will not test for because it’s handled outside the function]

3 Help: If the user only writes .yoda it shows an instruction of what the function is and how it works.  [Will not test for because it’s handled outside the function]

4 Findable: The command should be included in the command .help that lists commands.

**Specific requirements:**

5 Format: The returned text should have the format object-subject-verb.

6 Invalid sentence: If no changes to the format can be made, it should return: “Yodafication this doesn't need {username}!” + the original text.

7 Consistency: No words should be lost during the conversion.

8 Capitalization: The sentence should be capitalized correctly.

9 Multiple sentences: The function should apply the yodaification on all sentences without mixing between them. 
	
Example: 	“I am driving a car. She is buying a boat.” should become
			
   “Driving a car, I am. Buying a boat, she is.

### Project plan: 

- See how other functions handle requirement 2, 3, and 4.

- Write tests for those generic requirements

- Write tests for specific requirements.

- Create a baseline bot that fulfills generic requirements.

- Study how yoda speech work.

- Find a way to identify subject/object/verb.

- Implement the function

- Run tests and possibly improve function. 

- Continue until all tests pass or deemed faithful enough to the original issue description.

- Go through code and change to comply with repos specifications of how code should look.

### UML diagram
[Yodaify](//www.plantuml.com/plantuml/png/lLPDZzis4BthLqotbpHGt0-WXmeja0-anHwI7ZQNmd07N79aiwP8XQJYDTh-zr8YxSogjUfS0XzCldapZnmEENeUel1nw4prHTnHHz0ReMqLNG_HmRsBqNMWj2SPjRDLs6lR2oywCDfIFFR9mPdZEAagQKG8O9sYRq04k4dUAtg8OTKETdLqIkZskFej_z_0dnK0O84na8ra9Jq9PDeQJjC6GlHVDJ1o2xKmP7neGBgk4rQ5rIjdOvAguMaDus3oWx_WhRCqkl_D5lVTj3YbWtHUZGjSdSD8jqsXjcLnnhdzq6Vnj6coCOz5tsDnoG1vxppkqjoGpr2NIDfkysJhtT0Z3u6Of9052fX9MDoT6WnTv6Ano9qsAaNDKzaf537wKAQ3dmlE0ppsPnBegGqdpvAgnqjujETJlF5eIcJN7_Feu9CVbKmDlHAH54iBNvwY8Btknqf3v0OhEaAyYZe5vGuSl-mMACPqNW5n8LyBHv4jHeT8blmCrc7Xg1TAuPFpZsZfWFX4cf2kWl3RqC0BUqpZf_l3ULhkqvRYETnqgHZEfRZj_I2CRZMfASFSmZAx1DSSuRVx8Cn-9iaCbzR3yFaMpcV13JXQt0VoNYj55ZkAEwTollAuWPy7AzyL_Yb8PenxpY_BJ_3czkxkzkqlXRSJinFXeid8Dt2PE9MG4sgE3NQEthk8SaToZyvAuazYUGdNBrryjvcpbubPx2gYJf0NKq_W3XnluFJ4tdu4rw-C9flYrF0rr-IPkQXTmsHluFM3fAc0M8X_9VZA5Ps3yX9RlUZxLtdyUhGodNjgdIVKzeFRqpNv56tIkfAVQ7-GZ8MMZgs1P7uf0jLGgfQQX3jJmtRGHZNmwvG8OTPtrXrQ8_QqARRGm1sz7yXAOiQJ4bqIoiweLM31RyTytHjQQnitctb7_VP_E-eRYY9rrQMNTU7zv4VpkHj3SGljuRzmCKI7nabX24Fql8DmMag95-4pTPnFQ068skg8MEfWcJv__KU9N0bL_kQ3tv-jl_p-X_5NJv-HcsTGlhYg_0S_VcGe4NQa4kL61sr355QIQszoGLNFoQgXC_y0)

### Further work:
**For issue 2:** some tests are missing for the generic specifications. However, this should be handled by another test file because that functionality is implemented in another higher-level function.

**For both issues:** Dependency managers would need to be updated to include the new testing environment. This is also however outside the scope of the issues and should be raised as a new issue with its own pull request. Furthermore, the documentation should be updated to show how to run tests and basic examples of test-structure should be included to help onboarding of people who want to add tests.

## Overall experience

What are your main take-aways from this project? What did you learn?

It was clear that the main time sinks were onboarding and understanding the codebase. This time could be shortened down a lot by having a very clear tutorial for the onboarding part. Another issue was understanding how to incorporate new features into the system. Our main way of understanding the code was studying other peoples functions and mimicking their behavior. This could also be vastly improved by including template functions and graphical representations of how the code works together. 

Another issue was group work, with these small tasks/issues it became hard to work concurrent on the same thing. The lesson here is that 

## Self-assessment: Way of working

Same as the previous assignment, we as a group assess that we are still in the “In Place” state of way-of-working. We all have a clear understanding of who we are, what skills the team possesses, and how we communicate. We have understood our equal responsibilities in contributing roughly equal amounts because we are using a flat structure without an official leader. For this assignment, we communicated mostly on Discord as we felt it was easier than to divide the issue into tasks and work separately. Trust has been firmly established at this point. As for the previous assignment, we feel that we fully achieved most checkboxes for the “In Place” state in the way-of-working. We still do more regular voice calls to better make sure that we are all on the same page in our work.

For this week's assignment, our way-of-working was a little scattered compared to previous weeks. This mainly had to do with the fact that exam weeks are here, and some people had earlier exams and some people later exams. This made the time that we worked on the project a little different for each person (note: not time spent, just at which times during the days/weeks), although trust was always in place that each team member would contribute as we also discussed this beforehand.

This being the last assignment of the course, we do not have much to take with us to the next assignment between us. But we all agree that we have gained a lot of experience from these assignments, both regarding teamwork and skills in code collaboration.

## Statement of contributions

**William:** Participated in planning the assignment. Implemented tests for the original code, which were then updated with new tests for our new feature. Also worked on the report. 

**André:** Participated in planning the assignment. Formulaized requirements for issue 1 and 2. Implemented tests for issue 2. Created UML diagrams.

**Arvid:** Participated in planning the assignment. Set up discord server & bot, wrote code for issue 1. Worked on the report.

**Marcus:** Participated in planning the assignment. Helped formalize the requirements for issue 2. Wrote the implementation for issue 2. Wrote on the report.


## Issue 1 git diff

diff --git a/bot/exts/holidays/valentines/be_my_valentine.py b/bot/exts/holidays/valentines/be_my_valentine.py
index 81679794..70b52ce0 100644
--- a/bot/exts/holidays/valentines/be_my_valentine.py
+++ b/bot/exts/holidays/valentines/be_my_valentine.py
@@ -41,21 +41,39 @@ class BeMyValentine(commands.Cog):
     	"""
     	raise MovedCommandError(MOVED_COMMAND)

-	@commands.cooldown(1, 1800, commands.BucketType.user)
+	# @commands.cooldown(1, 1800, commands.BucketType.user)
 	@commands.group(name="bemyvalentine", invoke_without_command=True)
 	async def send_valentine(
-    	self, ctx: commands.Context, user: discord.Member, *, valentine_type: str | None = None
+    	self, ctx: commands.Context, user: discord.Member, privacy_type: str | None = None, anon: str | None = None, valentine_type: str | None = None
 	) -> None:
     	"""
     	Send a valentine to a specified user with the lovefest role.

-    	syntax: .bemyvalentine [user] [p/poem/c/compliment/or you can type your own valentine message]
+    	syntax: .bemyvalentine [user] [public/private] [anon/signed] [p/poem/c/compliment/or you can type your own valentine message]
     	(optional)

-    	example: .bemyvalentine Iceman#6508 p (sends a poem to Iceman)
-    	example: .bemyvalentine Iceman Hey I love you, wanna hang around ? (sends the custom message to Iceman)
+    	example: .bemyvalentine Iceman#6508 private anon p (sends an anonymous private poem through DM to Iceman)
+    	example: .bemyvalentine Iceman public signed Hey I love you, wanna hang around ? (sends the custom message publicly and signed to Iceman in the current channel)
     	NOTE : AVOID TAGGING THE USER MOST OF THE TIMES.JUST TRIM THE '@' when using this command.
     	"""
+
+
+    	if anon.lower() == "anon":
+        	# Delete the message containing the command right after it was sent to enforce anonymity.
+        	try:
+            	await ctx.message.delete()
+        	except discord.Forbidden:
+            	await ctx.send("I can't delete your message! Please check my permissions.")
+       	 
+
+    	if anon not in ["anon", "signed"]:
+        	# Anonymity type wrongfully specified.
+        	raise commands.UserInputError(
+            	f"Specify if you want the message to be anonymous or not!"
+        	)
+
+
+
     	if ctx.guild is None:
         	# This command should only be used in the server
         	raise commands.UserInputError("You are supposed to use this command in the server.")
@@ -64,21 +82,50 @@ class BeMyValentine(commands.Cog):
         	raise commands.UserInputError(
             	f"You cannot send a valentine to {user} as they do not have the lovefest role!"
         	)
+   	 
+    	if privacy_type not in ["public", "private"]:
+        	# Privacy type wrongfully specified.
+        	raise commands.UserInputError(
+            	f"Specify if you want the message to be sent privately or publicly!"
+        	)
+   	 
+    	# COMMENTED FOR TESTING PURPOSES
 
-    	if user == ctx.author:
-        	# Well a user can't valentine himself/herself.
-        	raise commands.UserInputError("Come on, you can't send a valentine to yourself :expressionless:")
+    	# if user == ctx.author:
+    	# 	# Well a user can't valentine himself/herself.
+    	# 	raise commands.UserInputError("Come on, you can't send a valentine to yourself :expressionless:")
 
     	emoji_1, emoji_2 = self.random_emoji()
     	channel = self.bot.get_channel(Channels.sir_lancebot_playground)
     	valentine, title = self.valentine_check(valentine_type)
 
-    	embed = discord.Embed(
-        	title=f"{emoji_1} {title} {user.display_name} {emoji_2}",
-        	description=f"{valentine} \n **{emoji_2}From {ctx.author}{emoji_1}**",
-        	color=Colours.pink
-    	)
-    	await channel.send(user.mention, embed=embed)
+    	if anon.lower() == "anon":
+        	embed = discord.Embed(
+            	title=f"{emoji_1} {title} {user.display_name} {emoji_2}",
+            	description=f"{valentine} \n **{emoji_2}From an anonymous admirer{emoji_1}**",
+            	color=Colours.pink
+        	)
+   	 
+    	else:
+        	embed = discord.Embed(
+            	title=f"{emoji_1} {title} {user.display_name} {emoji_2}",
+            	description=f"{valentine} \n **{emoji_2}From {ctx.author}{emoji_1}**",
+            	color=Colours.pink
+        	)
+
+    	if privacy_type.lower() == "private":
+        	# Send the message privately if "private" was speicified
+        	try:
+            	await user.send(embed=embed)
+            	await ctx.author.send(f"Your valentine has been **privately** delivered to {user.display_name}!")
+        	except discord.Forbidden:
+            	await ctx.send(f"I couldn't send a private message to {user.display_name}. They may have DMs disabled.")
+    	else:
+        	# Send the message publicly if "public" was speicified
+        	try:
+            	await ctx.send(user.mention, embed=embed)
+        	except discord.Forbidden:
+            	await ctx.send(f"I couldn't send a private message to {user.display_name}. They may have DMs disabled.")
 
 	@commands.cooldown(1, 1800, commands.BucketType.user)
 	@send_valentine.command(name="secret")
(END)


