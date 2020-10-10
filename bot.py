import datetime
import pytz
import requests
from telegram.ext import Updater, CommandHandler
import telegram
import threading
import os

group = [-455705027,-1001244490540,-1001428889789]
TOKEN = os.environ.get("TOKEN")

datelst = ['17/5', '12/2', '17/10', '15/9', '28/2', '21/9', '28/3', '20/5', '15/5', '6/10', '12/7', '11/10', '29/3', '24/10', '6/11', '21/5', '24/4', '28/9', '28/1', '28/5', 

'9/10', '6/7', '5/7', '22/5', '10/6', '7/10', '13/10', '26/6', '29/10', '5/11', '18/11', '25/8', '29/11', '27/2']

event = {"17/5" : ["Agender Pride Day","19 May","Day to promote awareness of agender individuals"],
"12/2" : ["Aromantic Spectrum Awareness Week","The first full week after 14 February","Week to promote information and awareness about aromantic spectrum identities and the issues they face"],
"17/10" : ["Asexual Awareness Week","Last full week in October","Week to promote awareness of those on the asexual spectrum"],
"15/9" : ["Bisexual Awareness Week","Week surrounding 23 September","Also referred to as BiWeek, and Bisexual+ Awareness Week"],
"28/2" : ["Bisexual Health Awareness Month","March","Also referred to as #BiHealthMonth; celebrated to raise awareness about the bisexual+ community's social, economic, and health disparities, advocate for resources, and inspire actions to improve bi+ people's well-being"],
"21/9" : ["Celebrate Bisexuality Day","23 September","Also referred to as Bisexual Pride Day, CBD, Bisexual Pride, and Bi Visibility Day"],
"29/3" : ["Day of Silence","April","Day varies from year to year; GLSEN's Day of Silence is an organizing tool to end the silencing effect of anti-LGBT bias."],
"20/5" : ["Harvey Milk Day","22 May","Celebrated to honor Harvey Milk, assassinated politician, on his birthday. It is celebrated officially in California, Milk's home state."],
"15/5" : ["International Day Against Homophobia, Transphobia and Biphobia","17 May","The main purpose of the 17 May mobilizations is to raise awareness of violence, discrimination, abuse, and repression of LGBT communities worldwide."],
"6/10" : ["International Lesbian Day","8 October","Annual day which celebrates lesbian culture, mainly celebrated in New Zealand and Australia"],
"12/7" : ["International Non-Binary People's Day","14 July","Date chosen due to being between International Men's Day and International Women's Day"],
"11/10" : ["International Pronouns Day","Third Wednesday in October","An annual event that seeks to make sharing, respecting and educating about personal pronouns commonplace"],
"28/3" : ["International Transgender Day of Visibility","31 March","Celebrated to bring awareness to transgender people and their identities as well as recognize those who helped fight for rights for transgender people"],
"24/10" : ["Intersex Awareness Day","26 October","Celebrated in October to commemorate the first intersex protest, which took place in Boston, MA"],
"6/11" : ["Intersex Day of Remembrance (Intersex Solidarity Day)","8 November","Birthday of Herculine Barbin"],
"21/5" : ["Irish Marriage Referendum","22 May","Ireland became the first country to legalize marriage equality through plebiscite on this day."],
"24/4" : ["Lesbian Visibility Day","26 April","Annual day to celebrate, recognize, and bring visibility to lesbians"],
"28/9" : ["LGBT History Month (USA & Canada)","October","First celebrated in 1994 in October. It was declared a national History month by President Barack Obama in 2009. The month was created with the intent to encourage openness and education about LGBT history and rights."],
"28/1" : ["LGBT History Month (UK)","February","Celebrated throughout February since 2005. Founded by Schools OUT UK - The LGBT+ Education Charity."],
"28/5" : ["LGBT Pride Month","June","June is celebrated as Pride in honor of the Stonewall Riots, though Pride events occur all year round. It also marks the month that same-sex marriage was legalized in the United States."],
"9/10" : ["National Coming Out Day","11 October","1988"],
"6/7" : ["Non-Binary Week","Week surrounding 14th July, Monday-Sunday","A week by, for, and about non-binary people, that includes celebrating non-binary people, non-binary advocacy, and educating and raising awareness about non-binary experiences and needs."],
"5/7" : ["Nonbinary Awareness Week","12 July","A week to spread awareness and visibility about nonbinary genders for both cis and binary trans communities. Started by Jay Genesis, gndrqr98 on Twitter."],
"22/5" : ["Pansexual & Panromantic Awareness Day","24 May","Annual day to promote awareness of and celebrate pansexual & panromantic identities."],
"10/6" : ["Pulse Night of Remembrance","12 June","Annual day of US remembrance for the loss of 49 LGBT men and women in the Pulse Nightclub shooting in Orlando, FL"],
"7/10" : ["Queer Day","9 October","Annual Day of Queer loudness and celebration. We are here we are queer get use to it! Initiative of three queer friends, Karen Offerein, Daan Smeelen and Aneta Leta who feel it is important to keep on raising awareness of need for tolerance and inclusion."],
"13/10" : ["Spirit Day","Third Thursday in October","Support for LGBTQ+ youth who are the victims of bullying, as well as to honor LGBTQ+ victims of bullying-related suicide."],
"26/6" : ["Stonewall Riots Anniversary","28 June","Day to remember the Stonewall Riots which are described as the start of the Trans and Gay Liberation Movement in the United States. It's a day for people to remember the biracial lesbian and drag king Stormé DeLarverie whose scuffle with the police started the rebellion."],
"29/10" : ["Trans Parent Day","First Sunday in November","A day that celebrates life and the love between transgender parents and their children, and between parents and their transgender children."],
"5/11" : ["Transgender Awareness Week","Typically second week of November","Week to educate about transgender and gender non-conforming people and the issues associated with their transition or identity."],
"18/11" : ["Transgender Day of Remembrance","20 November","Day to memorialize those who have been murdered as a result of transphobia"],
"25/8" : ["Wear it Purple Day","final Friday of August","Awareness day especially for young people, based in Australia"],
"29/11" : ["World AIDS Day","1 December","Recognized in 1988 by the United Nations"],
"27/2" : ["Zero Discrimination Day","1 March","""#ZeroDiscrimination Day is observed to bring awareness that you can't get sick from interacting with people who have AIDS, that everybody should have "access health care safely and live life fully with dignity", as per Michel Sidibé, UNAIDS Executive Director". The day is also used to bring attention to acceptance of non-straight fellow humans and not marginalise, discriminate or act cruelly against them, yet to instruct oneself, e.g. the gender continuum."""]}

mybot = telegram.Bot(TOKEN)
PORT = int(os.environ.get('PORT', 5000))


def check_event():
    while True:
        lastdate = requests.get("http://rajma.pythonanywhere.com/retreve?uname=pride_date&method=r").text
        dateinfo = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        date = str(dateinfo.date())
        DD,MM = int(date.split("-")[2]),int(date.split("-")[1])
        today = f"{DD}/{MM}"
        #if date == today:
        if today in datelst and today != lastdate:
            datalst = event[today]
            for i in group:
                mybot.sendMessage(i,f"*UPCOMING EVENT ALERT*\n\n*Event* - {datalst[0]}\n\n*When* - {datalst[1]}\n\n*Description* - {datalst[2]}",parse_mode="Markdown")
            requests.get(f"http://rajma.pythonanywhere.com/retreve?uname=pride_date&method=w&data={today}")

def id(bot,update):
    update.message.reply_text(f"The id is {update.message.chat_id}")

def near_event(bot,update):
    global datelst
    #print(datelst)
    dateinfo = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    date = str(dateinfo.date())
    DD,MM = int(date.split("-")[2]),int(date.split("-")[1])
    today = f"{DD}/{MM}"
    #print(today)
    nearevent = []
    #DD,MM = 2,11
    futureevent = []
    for dates in datelst:
        e_dd = int(dates.split("/")[0])
        e_mm = int(dates.split("/")[1])

        if e_dd > DD and e_mm == MM and e_dd - DD <= 30:
            nearevent.append(f"{e_dd}/{e_mm}")

    if nearevent == []:
        print("here")
        MM = MM+1
        if MM > 12:
            MM = 0
            DD = 0

        for dates in datelst:
            e_dd = int(dates.split("/")[0])
            e_mm = int(dates.split("/")[1])

            if e_dd > DD and e_mm == MM:# and e_dd - DD <= 10:
                nearevent.append(f"{e_dd}/{e_mm}")

    localdatelst = []
    for date in nearevent:
        localdatelst.append(int(date.split("/")[0]))

    localdatelst.sort()
    for d in localdatelst:
        for date in nearevent:
            if d == int(date.split("/")[0]):
                futureevent.append(date)

          
    eventstr = ""
    for date in futureevent:
        eventstr = f"{eventstr}*{event[date][1]}* - {event[date][0]}\n\n"
    update.message.reply_text("*Here's a list of event/s for next 30 days*\n\n"+eventstr,parse_mode="Markdown")

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("near_event", near_event))
dp.add_handler(CommandHandler("id", id))
threading.Thread(target=check_event).start()
#updater.start_polling()
updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
updater.bot.setWebhook('https://pridecave.herokuapp.com/' + TOKEN)
updater.idle()
