from datetime import datetime

# file to log messages to
log_file = "../private/chatlog.txt"


def log(message):
    # open the file in write only mode
    chat_log = open(log_file, "a")

    # get the current time, formatted
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # log each message with time + the authors discord id + the message
    # example: 2018-05-06 18:13:19 <@95573075541622784> "test"
    # a blank message.content might mean a message was deleted or is an image etc
    log_msg = time + " " + "{0.author.mention}".format(message) + " \"" + message.content + "\""

    # print to console
    print(str(log_msg))

    # write to the logfile
    chat_log.write(str(log_msg)+"\n")

    # close logfile and save to disk
    chat_log.close()
