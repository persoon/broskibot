from datetime import datetime

# file to log messages to
log_file = "../private/chatlog.txt"


def log(message):
    # open the file in write only mode
    chat_log = open(log_file, "a")

    # get the current time, formatted
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # log each message with date + time + author + author id + channel + message
    # example: 2018-05-06 18:13:19 Name#1234 <@95573075541622784> "game" "test"
    # a blank message.content might mean a message was deleted or is an image etc.
    log_msg = time + " "
    log_msg += str(message.author) + " "
    log_msg += "{0.author.mention}".format(message) + " "
    log_msg += "\"" + str(message.channel) + "\" "
    log_msg += "\"" + message.content + "\""

    # print to console
    print(str(log_msg))

    # write to the logfile
    chat_log.write(str(log_msg)+"\n")

    # close logfile and save to disk
    chat_log.close()
