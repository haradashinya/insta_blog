# My blog engine with redis.
ff


0. Setup Database.
1. Write markdown file to some dir.
2. And Everyone can see your some texts.
3. show first row of the text as a header instead of title key.


0. Setup Database.
Connect db and 
```
SET blog0219:username 'your username'
SET blog0219:password 'your password'


First row is the title of article.
##Pretty Code Formatting
	<pre class='prettyprint'>
	print 'hello world'
	</pre>
##Prepare for CLI API
	>> python command.py touch # create text.md file
	>> python command.py migrate # migrate it.

# Database settings...

Article
	id: auto_incr
	text: text
	created_at: datetime

	
Security
	name: admin
	password: password





