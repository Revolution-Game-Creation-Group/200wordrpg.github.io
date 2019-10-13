import smtplib, ssl

# Enable less secure connections: https://myaccount.google.com/lesssecureapps

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

nestedAssignments = [["Adam Blinkinsop","blinks@acm.org",1,2,3,4],["Aidan Sonia-Bolduc","zalmon135@gmail.com",2,3,4,5],["Alexander Newcombe","alexbnewcombe@gmail.com",3,4,5,6],["Andreas Lagerqvist","and_lag@hotmail.com",4,5,6,7],["Andrew J Young","thatonegm@gmail.com",5,6,7,8],["Audun Maatje","bitte_liten_kreps@ymail.com",6,7,8,9],["Cameron Ledbetter ","Cameronled@gmail.com",7,8,9,10],["Christine Beard","Petitewarlock@gmail.com",8,9,10,11],["Cyrus","cyrus.bukowsky@gmail.com",9,10,11,12],["Dane Fogdall","danefogdall@gmail.com",10,11,12,13],["Danielle Lauzon","impernious@gmail.com",11,12,13,14],["David Walker","sonicwaffle@outlook.com",12,13,14,15],["David zerbst","Tsbrez@gmail.com",13,14,15,16],["Deszmond Touray","DCTouray@live.com",14,15,16,17],["Dylan","Lozsrodu8@gmail.com",15,16,17,18],["Eva Schiffer","valleyviolet@gmail.com",16,17,18,19],["Eytan Kaplan","eytankaplan101@gmail.com",17,18,19,20],["Gabriel Robinson","bluelightscribe@gmail.com",18,19,20,21],["Gavin Rook","gavin.nich.rook@gmail.com",19,20,21,22],["Gray Detrick","graydetrick@gmail.com",20,21,22,23],["Iain Deans","iainthecopywriter@gmail.com",21,22,23,24],["Jane Higginson","jane2412@hotmail.co.uk",22,23,24,25],["Jeremy Esch","Jesch13@gmail.com",23,24,25,26],["Joey","labyrinthalone@gmail.com",24,25,26,27],["Johnnie Pittman","johnnie@videostorecowboy.com",25,26,27,28],["Jonathan Janssen","mrjonathanjanssen@gmail.com",26,27,28,29],["Joyce Chng","sabersger@gmail.com",27,28,29,30],["Kathryn Struck","k.struck@aol.com",28,29,30,31],["Lauren Schirduan","laurenchristiansmith@gmail.com",29,30,31,32],["Liz Stong","enstong@gmail.com",30,31,32,33],["Mark Preston","marcoksk1@gmail.com",31,32,33,34],["Martin Manrique","muchomil@gmail.com",32,33,34,35],["Matt Kaley-Burton","zebramatt@hotmail.com",33,34,35,36],["Matthew Gravelyn","matthew@gravelyn.com",34,35,36,37],["Matthew Orr","teachasneetch@juno.com",35,36,37,38],["Matthew Seagle","ogrebeef@gmail.com",36,37,38,39],["Megan Condis","megancondis@gmail.com",37,38,39,40],["Michael Inkmann","inkwan4@yahoo.com",38,39,40,41],["Mike Lake","mdlake@well.com",39,40,41,42],["Natalie Ash","natalie@natalieash.com",40,41,42,43],["Noé Falzon","falzon.noe@gmail.com",41,42,43,44],["Peter Lyons","shimek58@gmail.com",42,43,44,45],["Peter M.J. Gross","pmjgross@gmail.com",43,44,45,46],["Raymond Visser","raylvisser@gmail.com",44,45,46,47],["Ryan & Gabby Wilson","themysteriouslever@gmail.com",45,46,47,48],["Sarah Judd","dancesthroughlife@gmail.com",46,47,48,49],["Sean Smith","sean@bookseansmith.co.uk",47,48,49,50],["Seth Piercey","seth.pier@gmail.com",48,49,50,51],["Tara King","tara.r.king@gmail.com",49,50,51,52],["Thomas","thomasflott@outlook.com",50,51,52,53],["Tiffany LaPorta","dmwt21@yahoo.com",51,52,53,54],["Whit Carter","whithughcarter@gmail.com",52,53,54,55],["Aleksandra Sontowska","aleksandra.sontowska@go.art.pl",53,54,55,1],["Alex Teplitz","alexandrarose.nyc@gmail.com",54,55,1,2],["Ceri Bythesea ","Ceribythesea@gmail.com",55,1,2,3]]

password = input("Type your password and press enter:")

for reader in nestedAssignments:
    sender_email = "200wordrpg@gmail.com"
    receiver_email = reader[1]

    message = MIMEMultipart("alternative")
    message["Subject"] = "200 word Reader Assignments"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hello PERSONNAME!

    This is your chance to have a major influence over the challenge and help the best entries make it to the top. Thank you once again for all your hard work and your commitment to this challenge. Without you it wouldn't be much of anything.

    Oh! And please let me know if I spelled your name right on the Readers page.
    Here are your assignments:

        https://200wordrpg.github.io/2000/01/01/GROUPA
        https://200wordrpg.github.io/2000/01/01/GROUPB
        https://200wordrpg.github.io/2000/01/01/GROUPC
        https://200wordrpg.github.io/2000/01/01/GROUPD

    You have about 40 entries in total to evaluate. Treat the four lists as one when reading through and picking your top 5 choices. Once you have chosen your top 5, submit them at this link:
    Top Five Choices Form

    You have until 23:59 EST October 26th to get your choices in, but I would encourage you to try and get your choices in earlier if you can.

    Tips/Advice:

        Read through them immediately. Just give them a quick skim, and get them in your brain. Then it will simmer until you can give it your full attention.
        It's easy to read a really cool game and get excited about it, but keep in mind that the Challenge is about tabletop roleplaying games, not other kinds of games (board, card, etc). It's okay if an RPG has elements from other games, but it should involved role-playing at its core.
        Keep the Criteria in mind.
            Actionable. The entry should contain enough information to play the game.
            New and Overlooked Stories. The entry should encourage its players to tell a new kind of story, a story that has often been overlooked, or a familiar story from a new perspective.
            Engaging. The game should inspire the reader with ideas and questions. It should make the reader want to play this game as soon as possible.
        Keep a notepad when reading through the first time. If something interests you, write it down. Then you can narrow down your list from there.
        Please bring any grossly offensive games to our attention with an email. Dark subject matter is one thing, but we must not allow this to become a place for hate speech or prejudice.
        Content Warnings. If an entry you are assigned contains content that you don't feel comfortable reading or judging, let us know and we'll get you a different assignment.
        Ignore Links and References. You should not do any additional research or reading apart from the entry itself. If it says "read this link first" or "listen to this song", ignore it and try to judge the entry on its own.
        Please don't discuss entries publicly until the results are posted. Just to make sure other Readers aren't influenced in their decisions.
        Feel free to email us with any questions or concerns you have. I'm here to help!

    Thank you again for all the incredible work you are about to do. I owe you a coffee/burger/beer.

    - Jax, David, and Marshall"""

    html = """\
    <html>
    <body>
    <h2>Hello PERSONNAME!</h2>

    <p>This is your chance to have a major influence over the challenge and help the best entries make it to the top. Thank you once again for all your hard work and your commitment to this challenge. Without you it wouldn't be much of anything.</p>

    <p>Oh! And please let me know if I spelled your name right <a href="https://200wordrpg.github.io/readers">on the Readers page</a>.</p>

    <h3>Here are your assignments:</h3>

    <ul>
    <li><a href="https://200wordrpg.github.io/2000/01/01/GROUPA">https://200wordrpg.github.io/2000/01/01/GROUPA</a></li>
    <li><a href="https://200wordrpg.github.io/2000/01/01/GROUPB">https://200wordrpg.github.io/2000/01/01/GROUPB</a></li>
    <li><a href="https://200wordrpg.github.io/2000/01/01/GROUPC">https://200wordrpg.github.io/2000/01/01/GROUPC</a></li>
    <li><a href="https://200wordrpg.github.io/2000/01/01/GROUPD">https://200wordrpg.github.io/2000/01/01/GROUPD</a></li>
    </ul>

    <p>You have about 40 entries in total to evaluate. Treat the four lists as one when reading through and picking your top 5 choices. Once you have chosen your top 5, submit them at this link:</p>

    <h4><strong><a href="https://forms.gle/tkp9iG7XTRnvLnwFA">Top Five Choices Form</a></strong></h4>

    <p>You have until 23:59 EST October 26th to get your choices in, but I would encourage you to try and get your choices in earlier if you can.<p>

    <h3>Tips/Advice:</h3>

    <ul>
    <li>Read through them immediately. Just give them a quick skim, and get them in your brain. Then it will simmer until you can give it your full attention.</li>
    <li>It's easy to read a really cool game and get excited about it, but keep in mind that the challenge is for roleplaying games, not other kinds of games (board, card, etc). It's okay if an RPG has elements from other games, but it should involved role-playing at its core.</li>
    <li>Keep the Criteria in mind.
        <ul>
        <li>Actionable. The entry should contain enough information to play the game.</li>
        <li>New and Overlooked Stories. The entry should encourage its players to tell a new kind of story, a story that has often been overlooked, or a familiar story from a new perspective.</li>
        <li>Engaging. The game should inspire the reader with ideas and questions. It should make the reader want to play this game as soon as possible.</li>
        </ul>
    </li>
    <li>Keep a notepad when reading through the first time. If something interests you, write it down. Then you can narrow down your list from there.</li>
    <li>Please bring any grossly offensive games to our attention with an email. Dark subject matter is one thing, but we must not allow this to become a place for hate speech or prejudice.</li>
    <li>Content Warnings. If an entry you are assigned contains content that you don't feel comfortable reading or judging, let us know and we'll get you a different assignment.</li>
    <li>Ignore Links and References. You should not do any additional research or reading apart from the entry itself. If it says "read this link first" or "listen to this song", ignore it and try to judge the entry on its own.</li>
    <li>Please don't discuss entries publicly until the results are posted. Just to make sure other Readers aren't influenced in their decisions.</li>
    <li>Feel free to email us with any questions or concerns you have. I'm here to help!</li>
    </ul>

    <p>Thank you again for all the incredible work you are about to do. I owe you a coffee/burger/beer.</p>
    <p>   - Jax, David, and Marshall</p>

    </body>
    </html>
    """

    text = text.replace("PERSONNAME", reader[0])
    text = text.replace("GROUPA", "GROUP" + str(reader[2]))
    text = text.replace("GROUPB", "GROUP" + str(reader[3]))
    text = text.replace("GROUPC", "GROUP" + str(reader[4]))
    text = text.replace("GROUPD", "GROUP" + str(reader[5]))

    html = html.replace("PERSONNAME", reader[0])
    html = html.replace("GROUPA", "GROUP" + str(reader[2]))
    html = html.replace("GROUPB", "GROUP" + str(reader[3]))
    html = html.replace("GROUPC", "GROUP" + str(reader[4]))
    html = html.replace("GROUPD", "GROUP" + str(reader[5]))

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    print("EMAIL SENT:" + reader[0] + " - " + reader[1])