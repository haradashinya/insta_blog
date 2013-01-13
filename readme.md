# My blog engine with redis.


1. Write markdown file to some dir.
2. And Everyone can see your some texts.
3. show first row of the text as a header instead of title key.




デファオルトで、一行目に書いた行はタイトルになる。

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





